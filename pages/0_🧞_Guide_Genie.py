import os
import streamlit as st
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import PyPDF2
import io
from langdetect import detect
from groq import Groq
from typing import List, Dict, Optional
import validators
import json
from urllib.parse import urljoin, urlparse
import concurrent.futures
import time
import asyncio
from functools import partial
from theme import apply_dark_theme, show_page_header

# Set Streamlit theme to dark mode
st.set_page_config(
    page_title="GovGuide",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a bug': "https://www.example.com/bug",
        'About': "#Your Government Document Assistant"
    }

)

# Force dark theme
st.markdown("""
    <script>
        var elements = window.parent.document.getElementsByTagName('iframe');
        for (var i = 0; i < elements.length; i++) {
            elements[i].setAttribute('data-theme', 'dark');
        }
    </script>
    """, unsafe_allow_html=True)
# Apply dark theme
st.markdown(apply_dark_theme(), unsafe_allow_html=True)

# Load API keys from Streamlit secrets
GROQ_API_KEY = st.secrets["api_keys"]["groq_api_key"]
SERPER_API_KEY = st.secrets["api_keys"]["serper_api_key"]

# Initialize Groq client
groq_client = Groq(api_key=GROQ_API_KEY)

class DocumentSearchTool:
    def __init__(self):
        # Use the SERPER_API_KEY loaded from Streamlit secrets
        self.serper_api_key = SERPER_API_KEY
        self.visited_urls = set()
        self.pdf_docs = []
        self.search_timeout = 30
        self.max_pdfs = 3
        self.max_pages = 2

    def search_google(self, query: str, max_results: int = 5) -> List[Dict]:
        try:
            headers = {
                "X-API-KEY": self.serper_api_key,
                "Content-Type": "application/json"
            }
            payload = {
                "q": query,
                "num": max_results
            }
            response = requests.post(
                "https://google.serper.dev/search",
                headers=headers,
                json=payload,
                timeout=10
            )
            return response.json().get('organic', [])[:max_results]
        except Exception as e:
            st.warning(f"Search error: {str(e)}")
            return []

    def process_url_with_timeout(self, url: str, timeout: int = 10) -> Dict:
        try:
            if url.lower().endswith('.pdf'):
                content = self.extract_pdf_content(url)
                doc_type = "pdf"
            else:
                content = self.scrape_webpage(url)
                doc_type = "webpage"

            if content:
                return {
                    "url": url,
                    "title": url.split('/')[-1],
                    "content": content[:1000],
                    "type": doc_type
                }
        except Exception as e:
            st.warning(f"Error processing {url}: {str(e)}")
        return None

    def scrape_webpage(self, url: str) -> str:
        if not validators.url(url):
            return ""
        
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = ' '.join([p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'li'])])
            return text[:2000]
        except Exception:
            return ""

    def extract_pdf_content(self, pdf_url: str) -> Optional[str]:
        try:
            response = requests.get(pdf_url, timeout=5)
            pdf_file = io.BytesIO(response.content)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            return ' '.join([page.extract_text() for page in pdf_reader.pages[:3]])
        except Exception:
            return None

class SearchAssistant:
    # [Previous SearchAssistant class implementation remains the same]
    def __init__(self):
        self.search_tool = DocumentSearchTool()

    async def translate_text(self, text: str, target_language: str) -> str:
        try:
            prompt = f"Translate the following text to {target_language}:\n\n{text}"
            
            chat_completion = groq_client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192",
                temperature=0.3,
                max_tokens=1000,
                timeout=10
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            st.error(f"Translation error: {str(e)}")
            return text

    def process_query(self, query: str, language: str, country: str) -> Dict:
        start_time = time.time()
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        enhanced_query = f"{query} {country} government documents"
        
        status_text.text("Searching for relevant documents...")
        search_results = self.search_tool.search_google(enhanced_query)
        progress_bar.progress(0.2)
        
        documents = []
        processed_count = 0
        total_urls = min(len(search_results), 5)

        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            future_to_url = {
                executor.submit(
                    self.search_tool.process_url_with_timeout, 
                    result.get('link', '')
                ): result.get('link', '')
                for result in search_results[:total_urls]
            }

            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    doc = future.result(timeout=10)
                    if doc:
                        documents.append(doc)
                except Exception:
                    continue
                
                processed_count += 1
                progress = 0.2 + (0.4 * (processed_count / total_urls))
                progress_bar.progress(progress)
                status_text.text(f"Processing document {processed_count}/{total_urls}...")
                
                if time.time() - start_time > 30:
                    break

        progress_bar.progress(0.7)
        status_text.text("Analyzing information...")

        docs_text = "\n\n".join([
            f"Document: {doc['title']}\nType: {doc['type']}\nURL: {doc['url']}\nContent: {doc['content']}"
            for doc in documents
        ])

        prompt = f"""
        Query: {query}
        Country: {country}
        
        Based on the available information, provide a concise response that includes:
        1. Key requirements and documents needed
        2. Basic steps to follow
        3. Relevant official links
        
        If the information is incomplete, please indicate what might be missing.
        
        Available Information:
        {docs_text}
        """

        try:
            chat_completion = groq_client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192",
                temperature=0.3,
                max_tokens=1000
            )
            response_content = chat_completion.choices[0].message.content

            if language != "English":
                status_text.text("Translating response...")
                response_content = asyncio.run(self.translate_text(response_content, language))

        except Exception as e:
            st.error(f"Error processing response: {str(e)}")
            response_content = "Could not process the complete response. Here's what we found in our initial search:"
            for doc in documents:
                response_content += f"\n\n- {doc['title']}: {doc['content'][:200]}..."

        progress_bar.progress(1.0)
        status_text.empty()
        
        return {
            "response": response_content,
            "documents": documents,
            "search_time": f"{time.time() - start_time:.1f} seconds"
        }

def ask_link():
    st.title("Guide Genie")
    
    # Language selection
    languages = {
        "English": "en",
        "Hindi": "hi",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Urdu": "ur"
    }
    selected_language = st.selectbox("Select Language", list(languages.keys()))
    
    # Country selection with search
    default_countries = [
        "India", "United States", "United Kingdom", "Canada", "Australia",
        "Germany", "France", "Spain", "Brazil", "Japan"
    ]
    country = st.text_input("Enter Country", key="country_input")
    if not country:
        country = st.selectbox("Or select from common countries", default_countries)
    
    # Search query input
    query = st.text_input("What information are you looking for?", key="query_input")
    
    if st.button("Search") and query and country:
        try:
            search_assistant = SearchAssistant()
            
            results = search_assistant.process_query(query, languages[selected_language], country)
            
            st.info(f"Search completed in {results['search_time']}")
            
            st.subheader("Results")
            st.write(results["response"])
            
            if results["documents"]:
                st.subheader("Sources")
                for doc in results["documents"]:
                    with st.expander(f"📄 {doc['title'][:50]}..."):
                        st.write(f"Type: {doc['type']}")
                        st.write(f"URL: {doc['url']}")
            else:
                st.warning("No detailed sources found, but we've provided the best available information.")
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please try again with a different query or check your internet connection.")

if __name__ == "__main__":
    ask_link()
