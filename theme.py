def apply_dark_theme():
    return (
        "<style>"
        # Base styles with refined background and typography
        "body {"
        "    background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);"
        "    color: #E2E8F0;"
        "    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;"
        "}"
        ".main { padding: 0rem 1rem; }"
        
        # Elevated and modern button design
        ".stButton>button {"
        "    width: 100%;"
        "    padding: 0.75rem 1rem;"
        "    font-size: 1rem;"
        "    border-radius: 12px;"
        "    background: linear-gradient(145deg, #1E293B, #2D3748);"
        "    color: #E2E8F0;"
        "    border: 1px solid #3B82F6;"
        "    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.2);"
        "    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);"
        "}"
        ".stButton>button:hover {"
        "    transform: translateY(-3px);"
        "    box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);"
        "    background: linear-gradient(145deg, #2D3748, #3B82F6);"
        "}"
        
        # Card styles with glassmorphism
        ".card {"
        "    backdrop-filter: blur(10px);"
        "    background: rgba(30, 41, 59, 0.7);"
        "    border: 1px solid rgba(59, 130, 246, 0.2);"
        "    border-radius: 15px;"
        "    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);"
        "    padding: 1.5rem;"
        "    margin-bottom: 1rem;"
        "    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);"
        "}"
        ".card:hover {"
        "    transform: scale(1.02);"
        "    box-shadow: 0 15px 35px rgba(59, 130, 246, 0.3);"
        "}"
        
        # Enhanced typography with refined hierarchy
        "h1, h2, h3, h4, h5, h6 {"
        "    background: linear-gradient(90deg, #60A5FA, #3B82F6);"
        "    -webkit-background-clip: text;"
        "    -webkit-text-fill-color: transparent;"
        "    font-weight: 700;"
        "}"
        "h1 { font-size: 2.75em; letter-spacing: -0.025em; }"
        "h2 { font-size: 2.25em; letter-spacing: -0.02em; }"
        "p { line-height: 1.6; }"
        
        # Form elements with modern, clean design
        ".stTextInput>div>div>input,"
        ".stTextArea>div>div>textarea,"
        ".stSelectbox>div>div>select {"
        "    background: rgba(30, 41, 59, 0.6);"
        "    backdrop-filter: blur(5px);"
        "    border: 1px solid rgba(59, 130, 246, 0.3);"
        "    color: #E2E8F0;"
        "    border-radius: 10px;"
        "    transition: all 0.2s ease;"
        "}"
        ".stTextInput>div>div>input:focus,"
        ".stTextArea>div>div>textarea:focus {"
        "    border-color: #3B82F6;"
        "    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);"
        "}"
        
        # File uploader
        ".stFileUploader>div>button {"
        "    background: rgba(30, 41, 59, 0.6);"
        "    color: #E2E8F0;"
        "    border: 1px dashed #3B82F6;"
        "    border-radius: 8px;"
        "    backdrop-filter: blur(5px);"
        "}"
        ".stFileUploader>div>button:hover {"
        "    border-color: #60A5FA;"
        "    background: rgba(45, 55, 72, 0.8);"
        "}"
        
        # Expander
        ".streamlit-expanderHeader {"
        "    background: rgba(30, 41, 59, 0.7);"
        "    color: #E2E8F0;"
        "    border-radius: 8px;"
        "    backdrop-filter: blur(5px);"
        "}"
        ".streamlit-expanderContent {"
        "    background: rgba(30, 41, 59, 0.6);"
        "    border: 1px solid rgba(45, 55, 72, 0.5);"
        "    border-radius: 0 0 8px 8px;"
        "}"
        
        # Tabs
        ".stTabs [data-baseweb='tab-list'] {"
        "    gap: 30px;"
        "    background: rgba(30, 41, 59, 0.7);"
        "    padding: 1.5rem;"
        "    border-radius: 8px;"
        "    backdrop-filter: blur(5px);"
        "}"
        ".stTabs [data-baseweb='tab'] {"
        "    height: 40px;"
        "    padding: 1.5rem;"
        "    background: rgba(45, 55, 72, 0.6);"
        "    border-radius: 8px;"
        "    color: #E2E8F0;"
        "    border: 1px solid rgba(59, 130, 246, 0.3);"
        "}"
        ".stTabs [aria-selected='true'] {"
        "    background: #3B82F6;"
        "}"
        
        # Chat elements
        ".chat-message {"
        "    padding: 1rem;"
        "    margin: 0.5rem 0;"
        "    border-radius: 8px;"
        "    background: rgba(30, 41, 59, 0.7);"
        "    border: 1px solid rgba(45, 55, 72, 0.5);"
        "    backdrop-filter: blur(5px);"
        "}"
        ".user-message {"
        "    background: rgba(45, 55, 72, 0.8);"
        "    border-color: rgba(59, 130, 246, 0.3);"
        "}"
        
        # Scroll bar with modern aesthetic
        "::-webkit-scrollbar {"
        "    width: 10px;"
        "    background: rgba(30, 41, 59, 0.5);"
        "}"
        "::-webkit-scrollbar-thumb {"
        "    background: linear-gradient(145deg, #3B82F6, #60A5FA);"
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
        ".status-success { background-color: #065F46; color: #6EE7B7; }"
        ".status-warning { background-color: #92400E; color: #FCD34D; }"
        ".status-error { background-color: #991B1B; color: #FCA5A5; }"
        
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
        "<div style='background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(45, 55, 72, 0.8) 100%); "+
        "backdrop-filter: blur(10px); padding: 2rem; "+
        "border-radius: 15px; margin-bottom: 2rem; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);'>"+
        "<h1 style='background: linear-gradient(90deg, #60A5FA, #3B82F6); "+
        "-webkit-background-clip: text; -webkit-text-fill-color: transparent; "+
        "margin-bottom: 0.5rem;'>" + title + "</h1>"
    )
    if description:
        header_html += (
            "<p style='color: #E2E8F0; font-size: 1.1em; opacity: 0.9;'>" + description + "</p>"
        )
    header_html += "</div>"
    return header_html

def show_footer():
    return (
        "<div style='background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(45, 55, 72, 0.8) 100%); "+
        "backdrop-filter: blur(10px); text-align: center; color: #94A3B8; "+
        "padding: 2rem 1rem; margin-top: 2rem; border-top: 1px solid rgba(45, 55, 72, 0.5); "+
        "box-shadow: 0 -10px 25px rgba(0, 0, 0, 0.1); border-radius: 15px 15px 0 0;'>"
        "    <p>Need help? Contact our support team</p>"
        "    <p style='font-size: 0.8em; margin-top: 0.5rem; opacity: 0.7;'>"
        "        CiviDoc AI © 2024"
        "    </p>"
        "</div>"
    )