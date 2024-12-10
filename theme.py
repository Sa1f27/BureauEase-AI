def apply_dark_theme():
    return (
        "<style>"
        # Base styles with refined cream background
        "body {"
        "    background: linear-gradient(135deg, #F5F1E3 0%, #E8E4D5 100%);"
        "    color: #2C3639;"
        "    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;"
        "}"
        ".main { padding: 0rem 1rem; }"
        
        # Elevated and modern button design
        ".stButton>button {"
        "    width: 100%;"
        "    padding: 0.75rem 1rem;"
        "    font-size: 1rem;"
        "    border-radius: 12px;"
        "    background: linear-gradient(145deg, #708D61, #5F7A52);"
        "    color: #F5F1E3;"
        "    border: 1px solid #708D61;"
        "    box-shadow: 0 4px 15px rgba(112, 141, 97, 0.2);"
        "    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);"
        "}"
        ".stButton>button:hover {"
        "    transform: translateY(-3px);"
        "    box-shadow: 0 6px 20px rgba(112, 141, 97, 0.4);"
        "    background: linear-gradient(145deg, #5F7A52, #4A6141);"
        "}"
        
        # Card styles with soft shadows
        ".card {"
        "    background: rgba(245, 241, 227, 0.9);"
        "    border: 1px solid rgba(112, 141, 97, 0.2);"
        "    border-radius: 15px;"
        "    box-shadow: 0 10px 25px rgba(44, 54, 57, 0.08);"
        "    padding: 1.5rem;"
        "    margin-bottom: 1rem;"
        "    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);"
        "}"
        ".card:hover {"
        "    transform: scale(1.02);"
        "    box-shadow: 0 15px 35px rgba(112, 141, 97, 0.15);"
        "}"
        
        # Enhanced typography with olive accents
        "h1, h2, h3, h4, h5, h6 {"
        "    color: #4A6141;"
        "    font-weight: 700;"
        "}"
        "h1 { font-size: 2.75em; letter-spacing: -0.025em; }"
        "h2 { font-size: 2.25em; letter-spacing: -0.02em; }"
        "p { line-height: 1.6; color: #2C3639; }"
        
        # Form elements with clean design
        ".stTextInput>div>div>input,"
        ".stTextArea>div>div>textarea,"
        ".stSelectbox>div>div>select {"
        "    background: rgba(245, 241, 227, 0.9);"
        "    border: 1px solid rgba(112, 141, 97, 0.3);"
        "    color: #2C3639;"
        "    border-radius: 10px;"
        "    transition: all 0.2s ease;"
        "}"
        ".stTextInput>div>div>input:focus,"
        ".stTextArea>div>div>textarea:focus {"
        "    border-color: #708D61;"
        "    box-shadow: 0 0 0 3px rgba(112, 141, 97, 0.2);"
        "}"
        
        # File uploader
        ".stFileUploader>div>button {"
        "    background: rgba(245, 241, 227, 0.9);"
        "    color: #4A6141;"
        "    border: 1px dashed #708D61;"
        "    border-radius: 8px;"
        "}"
        ".stFileUploader>div>button:hover {"
        "    border-color: #5F7A52;"
        "    background: rgba(232, 228, 213, 0.9);"
        "}"
        
        # Expander
        ".streamlit-expanderHeader {"
        "    background: rgba(245, 241, 227, 0.9);"
        "    color: #2C3639;"
        "    border-radius: 8px;"
        "}"
        ".streamlit-expanderContent {"
        "    background: rgba(245, 241, 227, 0.7);"
        "    border: 1px solid rgba(112, 141, 97, 0.2);"
        "    border-radius: 0 0 8px 8px;"
        "}"
        
        # Tabs
        ".stTabs [data-baseweb='tab-list'] {"
        "    gap: 30px;"
        "    background: rgba(245, 241, 227, 0.9);"
        "    padding: 1.5rem;"
        "    border-radius: 8px;"
        "}"
        ".stTabs [data-baseweb='tab'] {"
        "    height: 40px;"
        "    padding: 1.5rem;"
        "    background: rgba(232, 228, 213, 0.9);"
        "    border-radius: 8px;"
        "    color: #2C3639;"
        "    border: 1px solid rgba(112, 141, 97, 0.3);"
        "}"
        ".stTabs [aria-selected='true'] {"
        "    background: #708D61;"
        "    color: #F5F1E3;"
        "}"
        
        # Chat elements
        ".chat-message {"
        "    padding: 1rem;"
        "    margin: 0.5rem 0;"
        "    border-radius: 8px;"
        "    background: rgba(245, 241, 227, 0.9);"
        "    border: 1px solid rgba(112, 141, 97, 0.2);"
        "}"
        ".user-message {"
        "    background: rgba(232, 228, 213, 0.9);"
        "    border-color: rgba(112, 141, 97, 0.3);"
        "}"
        
        # Scroll bar
        "::-webkit-scrollbar {"
        "    width: 10px;"
        "    background: rgba(245, 241, 227, 0.5);"
        "}"
        "::-webkit-scrollbar-thumb {"
        "    background: linear-gradient(145deg, #708D61, #5F7A52);"
        "    border-radius: 10px;"
        "}"
        
        # Status indicators
        ".status-badge {"
        "    display: inline-block;"
        "    padding: 0.25rem 0.75rem;"
        "    border-radius: 9999px;"
        "    font-size: 0.875rem;"
        "    font-weight: 500;"
        "    text-align: center;"
        "}"
        ".status-success { background-color: #D1E7DD; color: #0F5132; }"
        ".status-warning { background-color: #FFF3CD; color: #664D03; }"
        ".status-error { background-color: #F8D7DA; color: #842029; }"
        
        # Subtle animations
        "@keyframes subtleFloat {"
        "    0% { transform: translateY(0); }"
        "    50% { transform: translateY(-5px); }"
        "    100% { transform: translateY(0); }"
        "}"
        ".animate-float { animation: subtleFloat 3s infinite; }"
        "</style>"
    )

def show_page_header(title, description=None):
    header_html = (
        "<div style='background: linear-gradient(135deg, rgba(245, 241, 227, 0.9) 0%, rgba(232, 228, 213, 0.9) 100%); "+
        "padding: 2rem; border-radius: 15px; margin-bottom: 2rem; "+
        "box-shadow: 0 10px 25px rgba(44, 54, 57, 0.08);'>"+
        f"<h1 style='color: #4A6141; margin-bottom: 0.5rem;'>{title}</h1>"
    )
    if description:
        header_html += (
            f"<p style='color: #2C3639; font-size: 1.1em; opacity: 0.9;'>{description}</p>"
        )
    header_html += "</div>"
    return header_html

def show_footer():
    return (
        "<div style='background: linear-gradient(135deg, rgba(245, 241, 227, 0.9) 0%, rgba(232, 228, 213, 0.9) 100%); "+
        "text-align: center; color: #2C3639; padding: 2rem 1rem; margin-top: 2rem; "+
        "border-top: 1px solid rgba(112, 141, 97, 0.2); "+
        "box-shadow: 0 -10px 25px rgba(44, 54, 57, 0.08); border-radius: 15px 15px 0 0;'>"
        "    <p>Need help? Contact our support team</p>"
        "    <p style='font-size: 0.8em; margin-top: 0.5rem; opacity: 0.7;'>"
        "        DocHub-AI © 2024"
        "    </p>"
        "</div>"
    )