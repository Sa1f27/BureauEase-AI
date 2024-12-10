import streamlit as st
from theme import apply_dark_theme, show_page_header, show_footer
from utils import initialize_session_state

# Page config
st.set_page_config(
    page_title="Document Chat |  DocHub-AI",
    page_icon="💬",
    layout="centered",
    # initial_sidebar_state="collapsed",

)

# Apply dark theme
st.markdown(apply_dark_theme(), unsafe_allow_html=True)

def document_chat_page():
    # Initialize states
    initialize_session_state()
    
    # Header
    st.markdown(show_page_header(
        "💬 Document Chat",
        "Get instant answers about your documents"
    ), unsafe_allow_html=True)
    
    if st.session_state.chat_engines:
        # Document selector - Mobile friendly
        st.markdown(
            "<div class='card'>"
            "<h4>Select Document</h4>",
            unsafe_allow_html=True
        )
        
        doc_names = list(st.session_state.chat_engines.keys())
        selected_doc = st.selectbox(
            "Choose a document to discuss:",
            doc_names,
            key="doc_selector",
            format_func=lambda x: f"📄 {x}"
        )
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if selected_doc:
            # Document preview
            with st.expander("📄 Document Content", expanded=False):
                if selected_doc in st.session_state.analyses:
                    st.markdown(
                        f"<div class='card'>{st.session_state.analyses[selected_doc]['analysis']}</div>",
                        unsafe_allow_html=True
                    )
            
            # Initialize chat history for selected document
            if 'messages' not in st.session_state:
                st.session_state.messages = [
                    {"role": "assistant", "content": f"Hello! I'm here to help you understand {selected_doc}. What would you like to know?"}
                ]
            
            # Display chat messages
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
            
            
            # Chat input
            if prompt := st.chat_input("Type your question here..."):
                handle_user_input(prompt, selected_doc)
            
            # Clear chat button
            if len(st.session_state.messages) > 1:
                if st.button("🗑️ Clear Chat", use_container_width=True):
                    # Reset to initial welcome message
                    st.session_state.messages = [
                    {"role": "assistant", "content": f"Hello! I'm here to help you understand {selected_doc}. What would you like to know?"}
                    ]
                    for message in st.session_state.messages:
                        with st.chat_message(message["role"]):
                            st.write(message["content"])
                            st.rerun()
    
    else:
        # No documents message
        st.markdown(
            "<div class='card' style='text-align: center;'>"
            "<h3>No Documents Available</h3>"
            "<p>Please analyze some documents first to start chatting.</p>"
            "<div style='margin-top: 1rem;'>",
            unsafe_allow_html=True
        )
        
        if st.button("📝 Go to Document Analysis", use_container_width=True):
            st.switch_page("pages/1_📝_Document_Analysis.py")
        
        st.markdown("</div></div>", unsafe_allow_html=True)

def handle_user_input(prompt, selected_doc):
    """Handle user input with loading states and error handling"""
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    from groq import Groq
    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # try:
            #     chat_engine = st.session_state.chat_engines[selected_doc]
            #     response = chat_engine.chat(prompt)
            #     assistant_response = response.response
                
            #     # Add assistant response to messages
            #     st.session_state.messages.append({
            #         "role": "assistant",
            #         "content": assistant_response
            #     })
                
            #     # Display response
            #     st.write(assistant_response)
            
            # except Exception as e:
            #     error_message = f"Sorry, I encountered an error: {str(e)}"
            #     st.error(error_message)
            #     st.session_state.messages.append({
            #         "role": "assistant",
            #         "content": error_message
            #     })

            groq_api_key = st.secrets["api_keys"]["groq_api_key"]
            client = Groq(api_key=groq_api_key)

            try:
                # Construct the prompt
                prompt = f"You are an AI assistant presenting my app. Here is the input: {prompt} give response related to this docs {selected_doc}"
                
                # Make a request to the Groq client
                response = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},  # System context
                        {"role": "user", "content": prompt},  # User input
                    ],
                    model="llama-3.1-8b-instant",  # Model name
                )

                # Extract the assistant's response correctly
                assistant_response = response.choices[0].message.content

                # Add the assistant's response to messages
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_response
                })

                # Display the response in the Streamlit app
                st.markdown(assistant_response)

            except Exception as e:
                # Handle errors and display in Streamlit
                error_message = f"Error getting AI insights: {str(e)}"
                st.error(error_message)

                # Add the error message to messages
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message
                })



if __name__ == "__main__":
    document_chat_page()