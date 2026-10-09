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
            ("Math Olympiad Training", "Enter the Australian Mathematics Competition (AMC) at school; aim for Prize or High Distinction."),
            ("Free Robotic Telescopes", "Create a free account on the Harvard MicroObservatory to control real robotic telescopes online."),
            ("Google AI Micro-Course", "Complete Google AI for Anyone to understand how data models are built.")
        ],
        "🧪 Year 10 (2028) — National Competitions & Research": [
            ("BHP Science & Engineering Awards", "Use free NASA data to build an astronomy research project (100% free entry)."),
            ("Citizen Science Contributions", "Join Galaxy Zoo on Zooniverse to help professional astronomers classify deep-space galaxies."),
            ("Intermediate Olympiad", "Sit the Australian Intermediate Mathematics Olympiad (AIMO) at school."),
            ("HSC Subject Selection", "Select top-level courses: Physics, Chemistry, Math Advanced, Math Extension 1, and Math Extension 2.")
        ],
        "📝 Year 11 (2029) — International Standards": [
            ("Australian Physics Olympiad (ASO)", "Sit the national exam; aim for a Gold Medal and Australian Science Olympiad Summer School invitation."),
            ("Free SAT Preparation", "Use Khan Academy's Official SAT Prep daily. Target 1560–1600 total score (perfect 800 Math)."),
            ("IELTS Academic Test", "Achieve an overall band score of 8.0 or 9.0 (check for fee waivers with school counsellor)."),
            ("University Physics Outreach", "Email physics professors at local universities (e.g., UQ) for reading materials or mentorship.")
        ],
        "🎓 Year 12 (2030) — The Pinnacle": [
            ("Perfect Australian Rank", "Graduate with an ATAR of 99.50 to 99.95 using study groups and library resources."),
            ("HSC Top Achiever", "Place on the official NSW Top Achievers list for Physics or Extension Mathematics."),
            ("Free MIT Application", "Apply to MIT via admissions portal by Nov 1, 2030 (request application fee waiver)."),
            ("Submit CSS Profile for Financial Aid", "Provide income details so MIT applies full tuition discounts under financial aid policies.")
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

# 2. RAI - PERSONAL AI COPILOT
elif menu == "🤖 Rai - AI Copilot":
    col_title, col_btn = st.columns([4, 1])
    with col_title:
        st.header("🤖 Rai — High-End Personal AI Copilot")
        st.caption("⚡ Powered by Groq Engine (Ultra Fast & Daily Requests!)")
    with col_btn:
        if st.button("🗑️ Clear Memory"):
            data["chat_history"] = [
                {"role": "assistant", "content": "Yo bro! 😎 Memory reset complete. What new topic are we exploring today?"}
            ]
            save_data(data)
            st.rerun()
    
    if not groq_key:
        st.warning("⚠️ GROQ_API_KEY environment variable not found in Render settings!")
    
    # Display Chat History
    for msg in data["chat_history"]:
        avatar = "🤖" if msg["role"] == "assistant" else "🧑‍🚀"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])
            
    # User Input
    if user_prompt := st.chat_input("Ask Rai anything (Python, physics, homework, or MIT roadmap!)..."):
        with st.chat_message("user", avatar="🧑‍🚀"):
            st.markdown(user_prompt)
        data["chat_history"].append({"role": "user", "content": user_prompt})
        
        system_instruction = (
            "You are Rai, a high-end personal AI copilot built by a brilliant 14-year-old aspiring MIT astrophysics student. "
            "You are cool, casual, highly encouraging, and super intelligent. Speak in simple, clear English with emojis. "
            "You excel at explaining Python coding, solving physics/math problems step-by-step, and giving MIT roadmap advice. "
            "Never repeat generic boilerplate text; give fully custom, detailed, and direct answers to every prompt."
        )
        
        history_context = ""
        recent_turns = data["chat_history"][:-1][-10:]
        for msg in recent_turns:
            sender = "User" if msg["role"] == "user" else "Rai"
            history_context += f"{sender}: {msg['content']}\n"
        
        response = None
        
        if groq_key:
            try:
                client = Groq(api_key=groq_key)
                
                # Query Groq to fetch currently available models automatically
                available_models = [m.id for m in client.models.list().data if "whisper" not in m.id and "guard" not in m.id]
                
                last_err = ""
                for target_model in available_models:
                    try:
                        completion = client.chat.completions.create(
                            model=target_model,
                            messages=[
                                {"role": "system", "content": system_instruction},
                                {"role": "user", "content": f"Memory context:\n{history_context}\n\nQuestion: {user_prompt}"}
                            ]
                        )
                        response = completion.choices[0].message.content
                        break
                    except Exception as e:
                        last_err = str(e)
                        continue
                
                if not response:
                    response = f"⚠️ **Rai Connection Alert**: None of the available models worked. (Error: {last_err})"
            except Exception as e:
                response = f"⚠️ **Rai Connection Alert**: Failed to list models from Groq. (Error: {str(e)})"
        else:
            response = "🔑 **Rai System Note**: Please add GROQ_API_KEY in Render Environment Variables to wake up Rai!"
            
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(response)
        data["chat_history"].append({"role": "assistant", "content": response})
        
        save_data(data)
        st.rerun()

# 3. LINK & RESOURCE MANAGER
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

# 4. VISION & IDEA BOARD
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

   
