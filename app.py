import streamlit as st
import json
import os
from groq import Groq

st.set_page_config(
    page_title="MIT Space Scientist Launchpad",
    page_icon="🚀",
    layout="wide"
)

# Deep Space Canvas CSS + Glassmorphic Styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(10, 10, 26, 0.88), rgba(10, 10, 26, 0.88)), 
                    url("https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?q=80&w=2000&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    @keyframes rocketLaunch {
        0% { transform: translateY(30px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }

    .header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 20px 0;
        animation: rocketLaunch 1.2s ease-out;
    }

    .mit-logo-svg {
        width: 140px;
        margin-bottom: 15px;
        filter: drop-shadow(0px 0px 12px rgba(163, 31, 52, 0.9));
    }

    .main-title {
        color: #00d4ff;
        font-family: 'Trebuchet MS', sans-serif;
        font-size: 2.8em;
        font-weight: 800;
        letter-spacing: 2px;
        text-shadow: 0 0 15px rgba(0, 212, 255, 0.6);
        margin: 0;
    }

    .sub-title {
        color: #e0e0e0;
        font-size: 1.1em;
        margin-top: 5px;
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.4);
    }

    div[data-testid="stExpander"] {
        background: rgba(20, 24, 45, 0.65);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 10px;
        backdrop-filter: blur(5px);
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="header-container">
    <svg class="mit-logo-svg" viewBox="0 0 321 166" xmlns="http://www.w3.org/2000/svg">
        <path d="M0 166V0h33v166H0zm55 0V0h33v110H55v56zm55 0V0h33v166h-33zm55 0V56h33v110h-33zm0-110V0h33v56h-33zm55 110V0h33v166h-33zm56 0V56h32v110h-32z" fill="#A31F34"/>
    </svg>
    <h1 class="main-title">MIT SPACE SCIENTIST LAUNCHPAD</h1>
    <div class="sub-title">🚀 Your Interactive 4-Year Mission to MIT & Astrophysics</div>
</div>
""", unsafe_allow_html=True)

DATA_FILE = "user_mission_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {"checked": {}, "links": [], "ideas": [], "chat_history": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

if "chat_history" not in data:
    data["chat_history"] = [
        {"role": "assistant", "content": "Yo bro! 😎 I'm **Rai**, your personal AI Copilot! I can answer literally anything about Python 🐍, Astrophysics 🌌, Math 🧪, or your MIT Roadmap 🎯. What are we building today?"}
    ]

# Fetch Groq Key from Render Environment
groq_key = os.environ.get("GROQ_API_KEY", "")

menu = st.sidebar.radio("Navigation", ["🎯 Roadmap Tracker", "🤖 Rai - AI Copilot", "🔗 Resource & Link Manager", "💡 Space Vision & Idea Board"])

# 1. ROADMAP TRACKER
if menu == "🎯 Roadmap Tracker":
    st.header("🎯 Complete 4-Year Academic & Technical Roadmap")
    
    roadmap = {
        "🛠️ Year 8 (Current – Late 2026): Launching the Rocket": [
            ("Begin Python Coding", "Start a free Python foundational course on Codecademy or Kaggle to analyze telescope data."),
            ("Master Advanced Algebra", "Use Khan Academy to master algebra and geometry ahead of your school curriculum."),
            ("Explore Real Space Data", "Study cosmic coordinates and star light tracking through NASA's Hubble Site."),
            ("MIT AI 101 Overview", "Complete the free MIT AI 101 basic concepts overview to understand core terminology.")
        ],
        "🌌 Year 9 (2027) — Foundation & Advanced Skills": [
            ("Master Data Science in Python", "Complete advanced programming tracks on DataCamp or Coursera focused on data analysis."),
            ("Academic Excellence", "Achieve a 98%+ average in school Mathematics and secure a spot in the highest accelerated math pathway."),
            ("Math Olympiad Training", "Enter the Australian Mathematics Competition (AMC) at school; aim for 'Prize' or 'High Distinction'."),
            ("Free Robotic Telescopes", "Create a free account on the Harvard MicroObservatory to control real robotic telescopes online."),
            ("Google AI Micro-Course", "Complete '
   
