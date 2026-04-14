import streamlit as st
import streamlit.components.v1 as components
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="I'm So Sorry! 🥺", page_icon="💖", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700&display=swap');

    .stApp {
        background-color: #fff0f5;
        font-family: 'Quicksand', sans-serif;
    }
    
    div.stImage > img {
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- MAIN APP UI ---
st.markdown("<h1 style='color: #ff4b91; text-align: center; font-size: 2.5rem;'>I'm So Sorry Baby! 🥺</h1>", unsafe_allow_html=True)

col_image, col_text = st.columns([1, 1.2], gap="medium")

with col_image:
    # UPDATED PATH: Using the specific path you provided
    image_path = "forgiveness.png"
    
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.error(f"File not found at: {image_path}. Double check the username in your folder path!")

with col_text:
    st.markdown(f"""
        <div style="background: white; padding: 20px; border-radius: 20px; border: 2px dashed #ffb6c1; color: #555; text-align: center;">
            <p style="font-size: 1.05em; line-height: 1.5;">
                bbb im so sorry for forgetting that detail about ur phone. 
                i really didnt think of it on the spot, and oso i didnt know whether u even received the money for dat. 
                <br><br>
                i do enjoy talking to u baby. please dont think i dont enjoy talking to u. 
                You mean the world to me, and I promise to be more attentive. 
                pwease don't be mad! ✨
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- THE SLIPPERY BUTTON COMPONENT ---
components.html(
    """
    <div id="game-container" style="text-align: center; font-family: 'Quicksand', sans-serif; height: 500px; position: relative;">
        <h3 id="question-text" style="color: #ff1493; margin-bottom: 40px;">Will u forgive me?</h3>
        
        <div id="button-area" style="display: flex; justify-content: center; gap: 50px; align-items: center;">
            <button id="yes-btn" style="
                background-color: #ff4b91; 
                color: white; 
                border: none; 
                padding: 15px 50px; 
                border-radius: 50px; 
                font-weight: bold; 
                cursor: pointer;
                font-size: 18px;">
                YES! 💖
            </button>
            
            <button id="no-btn" style="
                background-color: #aaaaaa; 
                color: white; 
                border: none; 
                padding: 15px 50px; 
                border-radius: 50px; 
                font-weight: bold; 
                position: relative;
                cursor: pointer;
                font-size: 18px;
                z-index: 1000;">
                No. 😤
            </button>
        </div>

        <div id="celebration" style="display: none; margin-top: 20px;">
            <h1 style="color: #32CD32;">YAY! I LOVE YOU! 🎀</h1>
            <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHBndXh4ZzBxdXN4ZzBxdXN4ZzBxdXN4ZzBxdXN4ZzBxdXN4ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDJ9IbxxvDUQM/giphy.gif" style="width: 80%; border-radius: 20px;">
            <p style="color: #228B22; font-weight: bold; margin-top: 15px;"> pwease dont be mad at me baby i will be more attentiveee</p>
        </div>
    </div>

    <script>
        const noBtn = document.getElementById('no-btn');
        const yesBtn = document.getElementById('yes-btn');
        const questionText = document.getElementById('question-text');
        const buttonArea = document.getElementById('button-area');
        const celebration = document.getElementById('celebration');

        function moveButton() {
            // Using viewport dimensions to ensure it jumps across the whole screen area
            const maxX = window.innerWidth - noBtn.offsetWidth - 50;
            const maxY = 400 - noBtn.offsetHeight;
            noBtn.style.position = 'fixed';
            noBtn.style.left = Math.random() * maxX + 'px';
            noBtn.style.top = Math.random() * maxY + 'px';
        }

        document.addEventListener('mousemove', (e) => {
            const btnRect = noBtn.getBoundingClientRect();
            const distance = Math.sqrt(Math.pow(e.clientX - (btnRect.left + btnRect.width/2), 2) + Math.pow(e.clientY - (btnRect.top + btnRect.height/2), 2));
            if (distance < 90) moveButton();
        });

        noBtn.addEventListener('mouseover', moveButton);

        yesBtn.addEventListener('click', () => {
            questionText.style.display = 'none';
            buttonArea.style.display = 'none';
            celebration.style.display = 'block';
        });
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
    """,
    height=600,
)