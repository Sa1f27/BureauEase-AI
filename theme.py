def apply_dark_theme():
    return (
        "<style>"
        # Base styling with a cream and olive color palette
        "body {"
        "    background: linear-gradient(135deg, #FAF3E0 0%, #E8E1C8 100%);"
        "    color: #556B2F;"  # Olive green for text
        "    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;"
        "}"
        ".main { padding: 0rem 1rem; }"
        
        # Buttons with a gradient olive theme
        ".stButton>button {"
        "    width: 100%;"
        "    padding: 0.75rem 1rem;"
        "    font-size: 1rem;"
        "    border-radius: 12px;"
        "    background: linear-gradient(145deg, #A6C48A, #556B2F);"
        "    color: #FAF3E0;"
        "    border: 1px solid #6B8E23;"
        "    box-shadow: 0 4px 15px rgba(107, 142, 35, 0.2);"
        "    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);"
        "}"
        ".stButton>button:hover {"
        "    transform: translateY(-3px);"
        "    box-shadow: 0 6px 20px rgba(107, 142, 35, 0.4);"
        "    background: linear-gradient(145deg, #556B2F, #8BA978);"
        "}"
        
        # Card design with cream and olive highlights
        ".card {"
        "    backdrop-filter: blur(10px);"
        "    background: rgba(248, 244, 228, 0.7);"
        "    border: 1px solid rgba(107, 142, 35, 0.3);"
        "    border-radius: 15px;"
        "    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);"
        "    padding: 1.5rem;"
        "    margin-bottom: 1rem;"
        "    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);"
        "}"
        ".card:hover {"
        "    transform: scale(1.02);"
        "    box-shadow: 0 15px 35px rgba(107, 142, 35, 0.3);"
        "}"
        
        # Typography adjustments for readability and aesthetics
        "h1, h2, h3, h4, h5, h6 {"
        "    background: linear-gradient(90deg, #6B8E23, #556B2F);"
        "    -webkit-background-clip: text;"
        "    -webkit-text-fill-color: transparent;"
        "    font-weight: 700;"
        "}"
        "h1 { font-size: 2.75em; letter-spacing: -0.025em; }"
        "h2 { font-size: 2.25em; letter-spacing: -0.02em; }"
        "p { line-height: 1.6; color: #556B2F; }"
        
        # Input fields with a subtle cream-olive tone
        ".stTextInput>div>div>input,"
        ".stTextArea>div>div>textarea,"
        ".stSelectbox>div>div>select {"
        "    background: rgba(248, 244, 228, 0.8);"
        "    border: 1px solid rgba(107, 142, 35, 0.3);"
        "    color: #556B2F;"
        "    border-radius: 10px;"
        "    transition: all 0.2s ease;"
        "}"
        ".stTextInput>div>div>input:focus,"
        ".stTextArea>div>div>textarea:focus {"
        "    border-color: #556B2F;"
        "    box-shadow: 0 0 0 3px rgba(107, 142, 35, 0.2);"
        "}"
        
        # File uploader styling
        ".stFileUploader>div>button {"
        "    background: rgba(248, 244, 228, 0.8);"
        "    color: #556B2F;"
        "    border: 1px dashed #6B8E23;"
        "    border-radius: 8px;"
        "}"
        ".stFileUploader>div>button:hover {"
        "    border-color: #556B2F;"
        "    background: rgba(255, 239, 219, 0.9);"
        "}"
        
        # Scrollbar improvements
        "::-webkit-scrollbar {"
        "    width: 10px;"
        "    background: rgba(248, 244, 228, 0.5);"
        "}"
        "::-webkit-scrollbar-thumb {"
        "    background: linear-gradient(145deg, #6B8E23, #556B2F);"
        "    border-radius: 10px;"
        "}"
        
        "</style>"
    )


def custom_css():
    return """
    <style>
        /* Global Styles */
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
            background: linear-gradient(135deg, #FAF3E0 0%, #E8E1C8 100%);
            color: #556B2F;
        }
        
        /* Header Styling */
        .header-container {
            background: linear-gradient(135deg, #556B2F 0%, #8BA978 100%);
            color: #FAF3E0;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 15px 25px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .header-container h1 {
            margin-bottom: 0.5rem;
            font-weight: 700;
        }
        
        /* Feature Card Styling */
        .feature-card {
            background-color: rgba(248, 244, 228, 0.7);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 8px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            height: 100%;
            border: 1px solid rgba(107, 142, 35, 0.3);
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 12px 20px rgba(0,0,0,0.15);
        }
        
        .feature-card h3 {
            color: #556B2F;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
        }
        
        .feature-card h3 span {
            margin-right: 10px;
            font-size: 1.5rem;
        }
        
        /* Progress Bar Styling */
        .progress-container {
            background-color: rgba(248, 244, 228, 0.8);
            border-radius: 10px;
            height: 8px;
            margin-top: 1rem;
            overflow: hidden;
        }
        
        .progress-bar {
            background-color: #556B2F;
            height: 100%;
            border-radius: 10px;
            transition: width 0.7s cubic-bezier(0.25, 0.1, 0.25, 1);
        }
        
        /* Action Buttons */
        .stButton>button {
            background-color: #8BA978 !important;
            color: #FAF3E0 !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 12px 24px !important;
            transition: all 0.3s ease !important;
            font-weight: 600 !important;
        }
        
        .stButton>button:hover {
            background-color: #556B2F !important;
            transform: scale(1.05) !important;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1) !important;
        }
        
        /* Section Headings */
        h3 {
            color: #556B2F;
            border-bottom: 2px solid #8BA978;
            padding-bottom: 10px;
            margin-top: 2rem;
            margin-bottom: 1.5rem;
        }
    </style>
    """

html_code = """
<script src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs" type="module"></script>
<dotlottie-player src="https://lottie.host/ee7099f5-a693-4f40-9a81-b4a4dadc3ae9/LO7PLNgptk.lottie" background="transparent" speed="1" style="width: 300px; height: 300px" loop autoplay></dotlottie-player>
"""

def show_page_header(title, description=None):
    header_html = (
        "<div style='"
        "background: rgba(248, 244, 228, 0.8); "
        "backdrop-filter: blur(10px); "
        "padding: 2rem; "
        "border-radius: 15px; "
        "margin-bottom: 2rem; "
        "box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);'>"
        "<h1 style='"
        "background: linear-gradient(90deg, #6B8E23, #556B2F); "
        "-webkit-background-clip: text; "
        "-webkit-text-fill-color: transparent; "
        "margin-bottom: 0.5rem; "
        "font-size: 2em;'>"
        + title +
        "</h1>"
    )
    if description:
        header_html += (
            "<p style='"
            "color: #556B2F; "
            "font-size: 1.1em; "
            "opacity: 0.9;'>"
            + description +
            "</p>"
        )
    header_html += "</div>"
    return header_html


def show_footer():
    return (
        "<div style='"
        "background: rgba(248, 244, 228, 0.8); "
        "backdrop-filter: blur(10px); "
        "text-align: center; "
        "color: #556B2F; "
        "padding: 2rem 1rem; "
        "margin-top: 2rem; "
        "border-top: 1px solid rgba(107, 142, 35, 0.3); "
        "box-shadow: 0 -10px 25px rgba(0, 0, 0, 0.1); "
        "border-radius: 15px 15px 0 0;'>"
        "    <p style='margin: 0;'>Need help? Contact our support team</p>"
        "    <p style='font-size: 0.8em; margin-top: 0.5rem; opacity: 0.7;'>"
        "        BureauEase-AI © 2024"
        "    </p>"
        "</div>"
    )
