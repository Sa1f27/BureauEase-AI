import streamlit as st
from theme import custom_css
import requests
from datetime import datetime, timedelta
from theme import html_code
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="DocHub-AI",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="auto"
)

def render_header():
    """Render the main header with a gradient background."""
    st.markdown(custom_css(), unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            <div class="header-container" style="text-align: center; padding: 50px; background-color: #808000; border-radius: 10px;">
                <h1 style="font-size: 2.5rem; color: #D4C6B4; margin-bottom: 15px;">🏛️ DocHub-AI</h1>
                <p style="font-size: 1.25rem; color: #D4C6B4; margin-bottom: 5px;">Your Intelligent Companion for Smarter Government Documentation</p>
                <p style="font-size: 1rem; color: #D4C6B4;">Streamline, simplify, and supercharge your document management like never before!</p>
            </div>


            """, unsafe_allow_html=True)

        with col2:
            try:
                st.components.v1.html(html_code, height=300)
            except Exception as e:
                st.error(f"Error loading HTML: {e}")
def render_quick_actions():
    """Render quick action buttons with modern styling."""
    st.markdown("### 🚀 Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📝 Document Analysis", use_container_width=True):
            st.switch_page("pages/1_📝_Document_Analysis.py")
    
    with col2:
        if st.button("✍️ Writing Assistant", use_container_width=True):
            st.switch_page("pages/3_✍️_Writing_Assistant.py")
    
    with col3:
        if st.button("💬 Document Chat", use_container_width=True):
            st.switch_page("pages/2_💬_Document_Chat.py")
    
    with col4:
        if st.button("🧞 Guide Genie", use_container_width=True):
            st.switch_page("pages/0_🧞_Guider_Genie.py")

def render_features():
    """Render features in a grid with modern card design."""
    st.markdown("### 🌟 Key Features")
    
    features = [
        {
            "icon": "📑",
            "title": "Document Analysis",
            "description": "Advanced AI-powered document understanding with instant insights and comprehensive analysis."
        },
        {
            "icon": "✍️",
            "title": "Writing Assistant",
            "description": "Intelligent document creation tools for RTI, legal notices, and various government communications."
        },
        {
            "icon": "💬",
            "title": "Interactive Help",
            "description": "Real-time, context-aware guidance for navigating complex government procedures."
        },
        {
            "icon": "📚",
            "title": "Document Management",
            "description": "Secure, efficient document storage with version tracking and quick retrieval."
        }
    ]
    
    cols = st.columns(4)
    
    for i, feature in enumerate(features):
        with cols[i]:
            st.markdown(f"""
            <div class='feature-card'>
                <h3><span>{feature['icon']}</span>{feature['title']}</h3>
                <p>{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)

def render_workflow():
    """Render workflow steps with progress indicators."""
    st.markdown("### 🔄 How It Works")
    
    workflow_steps = [
        {"title": "Upload Documents", "description": "Securely upload your government documents", "progress": 25},
        {"title": "AI Processing", "description": "Our AI analyzes and interprets your documents", "progress": 50},
        {"title": "Insights & Guidance", "description": "Receive clear explanations and actionable insights", "progress": 75},
        {"title": "Take Action", "description": "Confidently proceed with recommended steps", "progress": 100}
    ]
    
    cols = st.columns(4)
    
    for i, step in enumerate(workflow_steps):
        with cols[i]:
            st.markdown(f"""
            <div class='feature-card'>
                <h4>{step['title']}</h4>
                <p>{step['description']}</p>
                <div class='progress-container'>
                    <div class='progress-bar' style='width: {step["progress"]}%'></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def render_target_audience():
    """Render target audience and security information."""
    st.markdown("### 🎯 Who Can Benefit")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Target Audience
        - Citizens navigating government procedures
        - RTI applicants and activists
        - Legal professionals
        - Government service seekers
        - Individuals requiring document assistance
        """)
    
    with col2:
        st.markdown("""
        #### Security & Privacy
        - End-to-end encryption
        - Secure document processing
        - No permanent document storage
        - Privacy-first approach
        - Regular security updates
        """)

#============SCHEMES====================#
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
                            st.image('https://via.placeholder.com/300x200.png?text=No+Image', use_column_width=True)
                        
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

def scheme():
    st.title("Government Schemes")

    # Default values for fetching news at the beginning
    default_category = "Student Welfare"
    default_query = "National Education Policy"

    # Schemes for dropdown options
    schemes = {
        "Student Welfare": [
            "National Education Policy",
            "PM Scholarship Scheme",
            "Student Financial Assistance",
            "Education Loan Schemes",
            "Skill Development for Students"
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

    # Create layout for category and query filters
    col1, col2 = st.columns(2)

    with col1:
        category = st.selectbox(
            "Select News Category",
            list(schemes.keys()),
            index=list(schemes.keys()).index(default_category)
        )

    with col2:
        query = st.selectbox(
            "Select Specific Query",
            schemes[category],
            index=schemes[default_category].index(default_query)
        )

    # Fetch and display news by default
    if "default_articles" not in st.session_state:
        st.session_state.default_articles = fetch_news(default_query)

    # Button to fetch filtered news
    fetch_button = st.button("Fetch News")

    # Load default or filtered articles
    if fetch_button:
        news_data = fetch_news(query)
    else:
        news_data = st.session_state.default_articles

    if news_data and news_data.get('articles'):
        articles = news_data['articles']
        articles_with_images = [
            article for article in articles if article.get('image')
        ]

        if articles_with_images:
            st.success(
                f"Found {len(articles_with_images)} articles for '{query}'"
            )
            display_articles_grid(articles_with_images[:21])  # Limit to 21 articles (7 rows of 3)
        else:
            st.warning("No articles found with images.")
    else:
        st.error("Unable to retrieve news articles.")

    st.markdown("---")
    st.info("📍 Focused on Indian Government Schemes")


def main():
    render_header()
    render_quick_actions()
    render_features()
    render_workflow()
    render_target_audience()
    scheme()
if __name__ == "__main__":
    main()