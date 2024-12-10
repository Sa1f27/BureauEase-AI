import streamlit as st
import requests
from datetime import datetime, timedelta

GNEWS_API_KEY = st.secrets["api_keys"]["gnews_api_key"]

def fetch_news(query):
    """
    Fetch news articles using GNews API
    """
    base_url = "https://gnews.io/api/v4/search"

    params = {
        "apikey": GNEWS_API_KEY,
        "q": query,
        "lang": "en",
        "country": "in",
        "max": 50,
        "sortby": "publishedAt"
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API Request Failed. Status Code: {response.status_code}")
            st.write(response.text)
            return None

    except Exception as e:
        st.error(f"Error fetching news: {e}")
        return None

def display_articles_grid(articles):
    """
    Display news articles in a 3-column grid format
    """
    # Create rows of 3 articles each
    for i in range(0, len(articles), 5):
        # Create 3 columns
        cols = st.columns(5)
        
        # Fill each column with an article
        for col_idx in range(5):
            article_idx = i + col_idx
            
            # Check if we still have articles to display
            if article_idx < len(articles):
                article = articles[article_idx]
                
                with cols[col_idx]:
                    # Container for each article
                    with st.container():
                        # Image
                        if article.get('image'):
                            st.image(article['image'], use_container_width=True)
                        else:
                            st.image('https://via.placeholder.com/300x200.png?text=No+Image', use_container_width=True)
                        
                        # Title - using markdown for better control over text size
                        st.markdown(f"### {article.get('title', 'No Title')}")
                        
                        # Description - truncated for better grid layout
                        description = article.get('description', '')
                        if description:
                            if len(description) > 100:
                                description = description[:100] + '...'
                            st.write(description)
                        
                        # Source and date in compact format
                        source_name = article.get('source', {}).get('name', 'Unknown Source')
                        
                        # Format date
                        if article.get('publishedAt'):
                            try:
                                pub_date = datetime.fromisoformat(article['publishedAt'].replace('Z', '+00:00'))
                                date_str = pub_date.strftime('%Y-%m-%d')
                            except Exception:
                                date_str = 'Date Not Available'
                        else:
                            date_str = 'Date Not Available'
                        
                        st.write(f"**{source_name}** | {date_str}")
                        
                        # Read more button
                        st.markdown(f"[Read More]({article['url']})")
                        
                        # Add some spacing between articles
                        st.markdown("---")

def main():
    st.set_page_config(
        page_title="Government Schemes",
        page_icon="📰",
        layout="wide"
    )

    st.title("Government Schemes")

    schemes = {
        "Student Welfare": [
            "National Education Policy"
            "PM Scholarship Scheme",
            "Student Financial Assistance",
            "Education Loan Schemes",
            "Skill Development for Students",
        ],
        "Government Schemes for People": [
            "PM Jan Dhan Yojana",
            "Ayushman Bharat",
            "Public Welfare Schemes",
            "Social Security Schemes",
            "Digital India Program"
        ],
        "Rural Farmers Support": [
            "PM Kisan Samman Nidhi",
            "Agricultural Loan Schemes",
            "Farmer Welfare Programs",
            "Pradhan Mantri Fasal Bima Yojana",
            "Rural Infrastructure Development"
        ]
    }

    col1, col2 = st.columns(2)

    with col1:
        category = st.selectbox(
            "Select News Category",
            list(schemes.keys())
        )

    with col2:
        query = st.selectbox(
            "Select Specific Query",
            schemes[category]
        )

    fetch_button = st.button("Fetch News")

    if fetch_button:
        news_data = fetch_news(query)

        if news_data and news_data.get('articles'):
            articles = news_data['articles']
            articles_with_images = [
                article for article in articles
                if article.get('image')
            ]

            if articles_with_images:
                st.success(f"Found {len(articles_with_images)} articles for '{query}'")
                display_articles_grid(articles_with_images[:21])  # Limit to 21 articles (7 rows of 3)
            else:
                st.warning("No articles found with images.")
        else:
            st.error("Unable to retrieve news articles.")

    st.markdown("---")
    st.info(
        "📍 Focused on Indian Government Schemes"
    )

if __name__ == "__main__":
    main()