import streamlit as st
import base64


def home():
    
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Abhishek Varma",
        page_icon="🍕",
    )

    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/photo.png", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/Resume.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    
    # Top title
    st.write(f"""<div class="title"><strong>Hi! My name is</strong> Dasaraju Abhishek Varma👋</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Enric Domingo">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True)

    # Alternative image (static and rounded) uncomment it if you prefer this one
    # st.write(f"""
    # <div style="display: flex; justify-content: center;">
    #    <img src="{img}" alt="Enric Domingo" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    # </div>
    # """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Computer Vision Engineer</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "Kaggle": ["https://www.kaggle.com/dasarajuabhishek", "https://www.kaggle.com/static/images/site-logo.svg"],
        "LinkedIn": ["https://www.linkedin.com/in/dasaraju-abhishek-varma-01babb1b9/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/abhishekvarma12345", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 I am a **Computer Vision Engineer intern** @ [SIPA s.p.a](https://www.sipa.it/it/) working on PET preform defects classification project.

    - ❤️ I am passionate about **Machine Learning/Deep Learning, Computer Vision, GenerativeAI technologies**, and more!
    
    - 🤖 I enojoy developing projects such as [Sensor fault detection(heavy duty vehicles)](https://github.com/abhishekvarma12345/sensor-fault-detection-main) and participating at platforms like [Kaggle](https://www.kaggle.com/dasarajuabhishek) 📈
    
    - 🏂 I like to travel, play cricket and chess.
    
    - 📫 How to reach me: abhishekvarmadasaraju@gmail.com
    
    - 🏠 Vittorio Veneto, Italy
    """)

    st.write("##")

    # Download CV button
    st.download_button(
        label="📄 Download my Resume",
        data=pdf_bytes,
        file_name="Abhishek_Varma_cv.pdf",
        mime="application/pdf",
    )

    st.write("##")
    
    st.write(f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects in the navigation menu! (Coming soon...)</div>""", unsafe_allow_html=True)




if __name__ == "__main__":

    home()