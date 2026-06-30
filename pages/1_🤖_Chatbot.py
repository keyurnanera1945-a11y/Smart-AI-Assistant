import logging
import os

import streamlit as st

from src.chat import (
    ensure_model_pulled,
    generate_response_streaming,
    get_embedding_model,
)
from src.constants import OLLAMA_MODEL_NAME
from src.utils import setup_logging

# ======================================================
# Logger
# ======================================================

setup_logging()
logger = logging.getLogger(__name__)

# ======================================================
# Page Config
# ======================================================

st.set_page_config(
    page_title="Smart AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ======================================================
# Custom CSS
# ======================================================

st.markdown(
    """
<style>

/* Hide Streamlit menu & footer */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* App Background */

.stApp{
    background:#F8FAFC;
}

/* Main Padding */

.block-container{
    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;
    padding-bottom:1rem;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#FFFFFF;
    border-right:1px solid #E5E7EB;
}

/* Sidebar title */

.sidebar-title{
    text-align:center;
    color:#1D4ED8;
    font-size:28px;
    font-weight:bold;
    margin-top:10px;
}

.sidebar-subtitle{
    text-align:center;
    color:#6B7280;
    font-size:15px;
    margin-bottom:20px;
}

/* Dashboard */

.main-title{
    text-align:center;
    margin-bottom:30px;
}

.main-title h1{
    color:#1E3A8A;
    font-size:50px;
    margin-bottom:5px;
}

.main-title p{
    color:#6B7280;
    font-size:18px;
}

/* Welcome Card */

.card{
    background:white;
    border:1px solid #E5E7EB;
    border-radius:16px;
    padding:22px;
    box-shadow:0 4px 12px rgba(0,0,0,0.05);
}

/* Chat Bubble */

.stChatMessage{
    border-radius:15px;
}

/* Chat Input */

.stChatInput{
    margin-top:10px;
}

/* Buttons */

.stButton > button{
    width:100%;
    border-radius:10px;
    height:42px;
    font-weight:600;
}

/* Footer */

.footer{
    text-align:center;
    color:#9CA3AF;
    font-size:13px;
}

</style>
""",
    unsafe_allow_html=True,
)

# ======================================================
# Sidebar
# ======================================================

with st.sidebar:

    logo_path = "images/assistant_logo.png"

    if os.path.exists(logo_path):
        st.image(logo_path, width=170)
    else:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
            width=170,
        )

    st.markdown(
        '<div class="sidebar-title">🤖 Smart AI Assistant</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-subtitle">Your Intelligent Local AI Chatbot</div>',
        unsafe_allow_html=True,
    )

    st.divider()

    st.success("🟢 Online")

    st.info("🧠 Model : Llama 3.2")

    st.info("⚡ Engine : Ollama")

    st.divider()
# ======================================================
# Load AI Models
# ======================================================

if "models_loaded" not in st.session_state:

    with st.spinner("Loading AI Model..."):

        get_embedding_model()
        ensure_model_pulled(OLLAMA_MODEL_NAME)

        st.session_state.models_loaded = True

        logger.info("AI model loaded successfully.")

# ======================================================
# Chat History
# ======================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ======================================================
# Sidebar Controls
# ======================================================

with st.sidebar:

    if st.button("🗑 Clear Conversation", use_container_width=True):

        st.session_state.chat_history = []
        st.rerun()

    st.divider()

    user_messages = sum(
        1
        for msg in st.session_state.chat_history
        if msg["role"] == "user"
    )

    assistant_messages = sum(
        1
        for msg in st.session_state.chat_history
        if msg["role"] == "assistant"
    )

    total_messages = len(st.session_state.chat_history)

    st.markdown("### 📊 Chat Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("User", user_messages)

    with col2:
        st.metric("AI", assistant_messages)

    st.metric("Total Messages", total_messages)

# ======================================================
# Dashboard Header
# ======================================================

st.markdown(
    """
<div class="main-title">
    <h1>🤖 Smart AI Assistant</h1>
    <p>Your Intelligent Local AI Chatbot</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="card">

### 👋 Welcome

Ask any question and Smart AI Assistant will generate intelligent
responses using your locally running Llama 3.2 model powered by Ollama.

</div>
""",
    unsafe_allow_html=True,
)

st.write("")
# ======================================================
# Display Previous Chat Messages
# ======================================================

for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ======================================================
# Chat Input
# ======================================================

prompt = st.chat_input("💬 Ask Smart AI Assistant...")

if prompt:

    # Save user message

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    # Display user message

    with st.chat_message("user"):
        st.markdown(prompt)

    logger.info(f"User: {prompt}")

    # Assistant response

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        response_text = ""

        with st.spinner("Thinking..."):

            try:

                response_stream = generate_response_streaming(
                    query=prompt,
                    temperature=0.7,
                    chat_history=st.session_state.chat_history,
                )

                if response_stream is not None:

                    for chunk in response_stream:

                        token = ""

                        # Ollama Python Client (0.6+)

                        if hasattr(chunk, "message"):

                            if hasattr(chunk.message, "content"):
                                token = chunk.message.content or ""

                        # Older versions

                        elif isinstance(chunk, dict):

                            token = (
                                chunk.get("message", {})
                                .get("content", "")
                            )

                        response_text += token

                        response_placeholder.markdown(
                            response_text + "▌"
                        )

                else:

                    response_text = "⚠ Unable to generate response."

            except Exception as e:

                logger.exception(e)

                response_text = f"❌ Error:\n\n{str(e)}"

        # Final response

        response_placeholder.markdown(response_text)

    # Save assistant response

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": response_text,
        }
    )

    logger.info("Assistant response completed.")
# ======================================================
# Welcome Message (Shown Before First Chat)
# ======================================================

if len(st.session_state.chat_history) == 0:

    st.markdown("")

    st.info(
        """
### 👋 Welcome to Smart AI Assistant

Start chatting by typing your question below.

Your assistant is running locally using **Ollama** and **Llama 3.2**.
"""
    )

# ======================================================
# Footer
# ======================================================

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;color:#6B7280;padding:10px;">

<b>🤖 Smart AI Assistant</b><br>

<small>Powered by Ollama • Llama 3.2 • Streamlit</small>

</div>
""",
    unsafe_allow_html=True,
)
        