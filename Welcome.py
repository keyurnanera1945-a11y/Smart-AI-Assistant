import os
import logging
import streamlit as st

from src.utils import setup_logging

# ======================================================
# Logger
# ======================================================

setup_logging()
logger = logging.getLogger(__name__)

# ======================================================
# Page Configuration
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

/* Hide Streamlit menu */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Background */

.stApp{
    background:#F8FAFC;
}

/* Main Container */

.block-container{
    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;
    padding-bottom:2rem;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#FFFFFF;
    border-right:1px solid #E5E7EB;
}

/* Sidebar Title */

.sidebar-title{
    text-align:center;
    color:#2563EB;
    font-size:28px;
    font-weight:bold;
    margin-top:10px;
}

.sidebar-subtitle{
    text-align:center;
    color:#6B7280;
    font-size:15px;
    margin-bottom:15px;
}

/* Dashboard Title */

.main-title{
    text-align:center;
    margin-top:15px;
}

.main-title h1{
    color:#1E3A8A;
    font-size:52px;
    margin-bottom:5px;
}

.main-title p{
    color:#6B7280;
    font-size:18px;
}

/* Cards */

.card{
    background:white;
    border:1px solid #E5E7EB;
    border-radius:15px;
    padding:22px;
    box-shadow:0 3px 10px rgba(0,0,0,.05);
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

    st.success("🟢 Status : Online")

    st.info("🧠 Model : Llama 3.2")

    st.info("⚡ Engine : Ollama")
# ======================================================
# Main Dashboard
# ======================================================

st.markdown(
    """
<div class="main-title">
    <h1>🤖 Smart AI Assistant</h1>
    <p>Your Personal Local AI Chatbot</p>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# ======================================================
# Welcome Card
# ======================================================

st.markdown(
    """
<div class="card">

<h2>👋 Welcome</h2>

<p style="font-size:17px; line-height:1.8; color:#4B5563;">

Welcome to <b>Smart AI Assistant</b>.

This application lets you interact with a powerful AI assistant running
completely on your local machine using <b>Ollama</b> and <b>Llama 3.2</b>.

Ask questions, generate content, write code, summarize text, and have
natural conversations with your own private AI.

</p>

</div>
""",
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# ======================================================
# Feature Section
# ======================================================

st.markdown("## ✨ Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
<div class="card">

<h3>⚡ Fast Responses</h3>

<p>
Generate answers quickly with a locally running AI model.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

with col2:

    st.markdown(
        """
<div class="card">

<h3>🔒 Private</h3>

<p>
Everything runs on your own computer.
Your conversations stay private.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

with col3:

    st.markdown(
        """
<div class="card">

<h3>🤖 AI Powered</h3>

<p>
Powered by Ollama and Llama 3.2 for intelligent conversations.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

st.write("")
# ======================================================
# Get Started Section
# ======================================================

st.markdown("---")

st.markdown(
    """
<div style="text-align:center; padding:20px;">

<h2 style="color:#2563EB;">
🚀 Get Started
</h2>

<p style="font-size:18px; color:#6B7280;">

Open the <b>Chatbot</b> page from the sidebar and start
chatting with your Smart AI Assistant.

</p>

</div>
""",
    unsafe_allow_html=True,
)

# ======================================================
# About the Assistant
# ======================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
<div class="card">

<h3>💡 What can it do?</h3>

<ul>
<li>Answer questions</li>
<li>Generate code</li>
<li>Explain concepts</li>
<li>Write content</li>
<li>Summarize text</li>
<li>Brainstorm ideas</li>
</ul>

</div>
""",
        unsafe_allow_html=True,
    )

with col2:

    st.markdown(
        """
<div class="card">

<h3>🛠 Technology Stack</h3>

<ul>
<li>Python</li>
<li>Streamlit</li>
<li>Ollama</li>
<li>Llama 3.2</li>
<li>Sentence Transformers</li>
</ul>

</div>
""",
        unsafe_allow_html=True,
    )

# ======================================================
# Footer
# ======================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    """
<div class="footer">

<b>🤖 Smart AI Assistant</b>

<br><br>

Your Personal Local AI Chatbot powered by
<strong>Ollama</strong> and <strong>Llama 3.2</strong>.

</div>
""",
    unsafe_allow_html=True,
)    