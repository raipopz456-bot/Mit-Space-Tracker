import streamlit as st
import json
import os

st.set_page_config(
    page_title="MIT Space Scientist Launchpad",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for Rocket Animations and Glowing Dark Theme
st.markdown("""
<style>
    @keyframes rocketLaunch {
        0% { transform: translateY(50px); opacity: 0; }
        50% { transform: translateY(-10px); opacity: 1; }
        100% { transform: translateY(0); opacity: 1; }
    }
    .main-title {
        text-align: center;
        color: #00d4ff;
        font-family: 'Trebuchet MS', sans-serif;
        animation: rocketLaunch 1.5s ease-out;
        font-size: 3em;
        font-weight: bold;
    }
    .rocket-icon {
        font-size: 4em;
        text-align: center;
        animation: rocketLaunch 2s infinite alternate;
    }
</style>
""", unsafe_allow_html=True)

# Animated Intro Banner
st.markdown('<div class="rocket-icon">🚀</div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">MIT SPACE SCIENTIST LAUNCHPAD</h1>', unsafe_allow_html=True)
st.caption("<p style='text-align: center;'>Your Interactive 4-Year Mission to MIT & Astrophysics</p>", unsafe_allow_html=True)

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
            st.markdown(f"-[**{item['name']}**]({item['url']})")

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
