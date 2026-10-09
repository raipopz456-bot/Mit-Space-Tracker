import streamlit as st
import json
import os

st.set_page_config(
    page_title="MIT Space Scientist Launchpad",
    page_icon="🚀",
    layout="wide"
)

# Deep Space Canvas CSS + MIT Emblem Styling
st.markdown("""
<style>
    /* Deep space background */
    .stApp {
        background: linear-gradient(rgba(10, 10, 26, 0.85), rgba(10, 10, 26, 0.85)), 
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

    .mit-logo {
        width: 140px;
        margin-bottom: 15px;
        filter: drop-shadow(0px 0px 12px rgba(163, 31, 52, 0.8));
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

    /* Translucent glass container effect for content */
    div[data-testid="stVerticalBlock"] > div {
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Header Section with MIT Seal & Title
st.markdown("""
<div class="header-container">
    <img class="mit-logo" src="https://upload.wikimedia.org/wikipedia/commons/0/0c/MIT_logo_2003-2023.svg" alt="MIT Emblem">
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
    return {"checked": {}, "links": [], "ideas": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["🎯 Roadmap Tracker", "🔗 Resource & Link Manager", "💡 Space Vision & Idea Board"])

# 1. ROADMAP TRACKER
if menu == "🎯 Roadmap Tracker":
    st.header("🎯 4-Year Academic & Technical Roadmap")
    
    roadmap = {
        "🛠️ Year 8 (Current – Late 2026): Launching the Rocket": [
            ("Begin Python Coding", "Start a free Python foundational course on Codecademy or Kaggle."),
            ("Master Advanced Algebra", "Use Khan Academy to master algebra and geometry ahead of school."),
            ("Explore Real Space Data", "Study cosmic coordinates through NASA's Hubble Site."),
            ("MIT AI 101 Overview", "Complete free MIT AI 101 basic concepts overview.")
        ],
        "🌌 Year 9 (2027) — Foundation & Advanced Skills": [
            ("Master Data Science in Python", "Complete advanced programming tracks on DataCamp or Coursera."),
            ("Academic Excellence", "Achieve a 98%+ average in school Mathematics."),
            ("Math Olympiad Training", "Enter the Australian Mathematics Competition (AMC)."),
            ("Free Robotic Telescopes", "Control real robotic telescopes via Harvard MicroObservatory.")
        ],
        "🧪 Year 10 (2028) — Competitions & Research": [
            ("BHP Science & Engineering Awards", "Build an astronomy research project using open NASA data."),
            ("Citizen Science Contributions", "Classify deep-space galaxies on Zooniverse Galaxy Zoo."),
            ("Intermediate Olympiad", "Sit the Australian Intermediate Mathematics Olympiad (AIMO).")
        ],
        "📝 Year 11 (2029) — International Standards": [
            ("Australian Physics Olympiad", "Sit the national exam at school for summer school invitation."),
            ("SAT Preparation", "Target 1560-1600 total score (perfect 800 Math)."),
            ("IELTS Academic Test", "Achieve an overall band score of 8.0+")
        ],
        "🎓 Year 12 (2030) — The Pinnacle": [
            ("Perfect Australian Rank", "Graduate with an ATAR of 99.50+."),
            ("Apply to MIT", "Submit MIT undergraduate application via admissions portal by Nov 1.")
        ]
    }
    
    total_tasks = sum(len(items) for items in roadmap.values())
    completed = sum(1 for v in data["checked"].values() if v)
    progress = int((completed / total_tasks) * 100) if total_tasks > 0 else 0
    
    st.progress(progress / 100)
    st.write(f"**Overall Progress:** {progress}% ({completed}/{total_tasks} Tasks Completed)")
    
    for section, tasks in roadmap.items():
        with st.expander(section, expanded=True):
            for title, desc in tasks:
                is_checked = data["checked"].get(title, False)
                chk = st.checkbox(f"**{title}**: {desc}", value=is_checked, key=title)
                if chk != is_checked:
                    data["checked"][title] = chk
                    save_data(data)
                    st.rerun()

# 2. LINK & RESOURCE MANAGER
elif menu == "🔗 Resource & Link Manager":
    st.header("🔗 Project Links & Resource Vault")
    st.write("Save websites, GitHub repositories, and space research bookmarks here!")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        link_title = st.text_input("Link Name (e.g., My Hubble Data Script)")
        link_url = st.text_input("URL (e.g., https://github.com/...)")
        if st.button("➕ Add Link"):
            if link_title and link_url:
                data["links"].append({"name": link_title, "url": link_url})
                save_data(data)
                st.success("Link added!")
                st.rerun()
    
    with col2:
        st.subheader("Saved Links")
        for idx, item in enumerate(data["links"]):
            st.markdown(f"- [**{item['name']}**]({item['url']})")

# 3. VISION & IDEA BOARD
elif menu == "💡 Space Vision & Idea Board":
    st.header("💡 Imagine & Design Your Projects")
    
    new_idea = st.text_area("Write down project ideas, research questions, or space hypotheses:")
    if st.button("🚀 Save Idea"):
        if new_idea:
            data["ideas"].append(new_idea)
            save_data(data)
            st.success("Idea logged into your mission file!")
            st.rerun()
            
    st.subheader("Your Brainstorm Log")
    for idx, idea in enumerate(data["ideas"]):
        st.info(f"**Idea #{idx+1}:** {idea}")
