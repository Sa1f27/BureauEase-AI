import streamlit as st
from googletrans import Translator

# Import your dark theme, header, and footer functions
from theme import apply_dark_theme, show_page_header, show_footer


class TranslationManager:
    def __init__(self):
        self.translator = Translator()
        self.languages = {
            "English": "en",
            "Hindi": "hi",
            "Telugu (తెలుగు)": "te",
            "Malayalam": "ml",
            "Tamil": "ta",
            "Kannada": "kn",
            "Marathi": "mr",
            "Bengali": "bn",
            "Gujarati": "gu",
        }
        self.selected_language = "en"

    def translate_text(self, text):
        """
        Translates a given text to the currently selected language.
        """
        if self.selected_language == "en":
            return text  # No need to translate for English
        try:
            return self.translator.translate(text, dest=self.selected_language).text
        except Exception as e:
            return text  # Fallback to original text in case of errors


class MainApp:
    def __init__(self, translator: TranslationManager):
        self.translator = translator

    def render_header(self):
        """
        Render the page header with translation.
        """
        st.markdown(
            show_page_header(
                f"<div style='text-align: center;'>{self.translator.translate_text('🏛️ CiviDoc AI')}",
                f"<div style='text-align: center;'>{self.translator.translate_text('Your AI-powered companion for all government document needs')}",
            ),
            unsafe_allow_html=True,
        )

    def render_quick_access_section(self):
        """
        Render the quick access section with translation.
        """
        st.markdown(
            f"<div class='grid'>"
            f"<div class='card' onclick='void(0)'>"
            f"<div style='text-align: center;'>"
            f"<h3>{self.translator.translate_text('📝 Document Analysis')}</h3>"
            f"<p>{self.translator.translate_text('Upload and understand government documents instantly')}</p>"
            f"<div class='status-badge status-success'>{self.translator.translate_text('Ready to Use')}</div>"
            f"</div></div>"
            f"<div class='card' onclick='void(0)'>"
            f"<div style='text-align: center;'>"
            f"<h3>{self.translator.translate_text('✍️ Writing Assistant')}</h3>"
            f"<p>{self.translator.translate_text('Create professional government documents effortlessly')}</p>"
            f"<div class='status-badge status-success'>{self.translator.translate_text('Ready to Use')}</div>"
            f"</div></div>"
            f"<div class='card' onclick='void(0)'>"
            f"<div style='text-align: center;'>"
            f"<h3>{self.translator.translate_text('💬 Document Chat')}</h3>"
            f"<p>{self.translator.translate_text('Get instant answers about your documents')}</p>"
            f"<div class='status-badge status-success'>{self.translator.translate_text('Ready to Use')}</div>"
            f"</div></div>"
            f"</div>",
            unsafe_allow_html=True,
        )

    def render_buttons(self):
        """
        Render quick action buttons with translation.
        """
        st.markdown("<div class='touch-spacing'>", unsafe_allow_html=True)
        if st.button(self.translator.translate_text("📝 Start Document Analysis"), use_container_width=True):
            st.switch_page("pages/1_📝_Document_Analysis.py")
        if st.button(self.translator.translate_text("✍️ Create New Document"), use_container_width=True):
            st.switch_page("pages/3_✍️_Writing_Assistant.py")
        if st.button(self.translator.translate_text("💬 Open Document Chat"), use_container_width=True):
            st.switch_page("pages/2_💬_Document_Chat.py")
        st.markdown("</div>", unsafe_allow_html=True)

    def render_footer(self):
        """
        Render the footer with translation.
        """
        st.markdown(show_footer(), unsafe_allow_html=True)

    def main(self):
        # Apply dark theme
        st.markdown(apply_dark_theme(), unsafe_allow_html=True)

        # Language Selector in Sidebar
        st.sidebar.title("🌐 Language Settings")
        selected_language = st.sidebar.selectbox(
            "Select Language", options=list(self.translator.languages.keys())
        )
        self.translator.selected_language = self.translator.languages[selected_language]

        # Render content
        self.render_header()
        self.render_quick_access_section()
        self.render_buttons()
        self.render_footer()


if __name__ == "__main__":
    # Initialize translation manager
    translator = TranslationManager()
    # Run the app
    app = MainApp(translator)
    app.main()
