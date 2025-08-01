import streamlit as st
from PIL import Image
import time

# --- Session State Initialization ---
if "ready_phase" not in st.session_state:
    st.session_state.ready_phase = "ask"
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0
if "countdown" not in st.session_state:
    st.session_state.countdown = 10
if "photo_step" not in st.session_state:
    st.session_state.photo_step = 0
if "show_poem" not in st.session_state:
    st.session_state.show_poem = False

# --- Photo Memory List ---
photos_with_captions = [
    ("photo1.jpg", "The day you looked at me like the whole galaxy was inside me."),
    ("photo2.jpg", "Our cutest little memory ever!"),
    ("photo3.jpg", "Just you being you, stealing my heart again."),
    ("photo4.jpg", "That time you laughed and I knew I was home."),
]

# --- Poem ---
final_poem = """
**My Jellyfish, My Universe**

In stardust whispers and moonlit hue,  
Every breath I take remembers you.  
From silly selfies to silent stares,  
You’ve made magic out of mundane airs.

For every photo, every frame,  
There’s a heartbeat whispering your name.  
So here’s my heart — not just today —  
But forevermore, come what may.  
"""

# --- Step 1: ARE YOU READY Phase ---
if st.session_state.ready_phase == "ask":
    st.markdown("## 💖 Are you ready????")
    st.markdown("#### (No cheating, click only when you truly are 😉)")

    no_font_size = 16 + st.session_state.no_clicks * 10
    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💫"):
            st.session_state.ready_phase = "countdown"
            st.experimental_rerun()
    with col2:
        if st.session_state.no_clicks < 3:
            if st.button(f"<span style='font-size:{no_font_size}px'>NO 😝</span>", unsafe_allow_html=True):
                st.session_state.no_clicks += 1
                st.experimental_rerun()
        else:
            if st.button("OK FINE YES 😤"):
                st.session_state.ready_phase = "countdown"
                st.experimental_rerun()

# --- Step 2: Countdown Phase ---
elif st.session_state.ready_phase == "countdown":
    if st.session_state.countdown > 0:
        st.markdown(f"### ⏳ Get ready in... `{st.session_state.countdown}`")
        time.sleep(1)
        st.session_state.countdown -= 1
        st.experimental_rerun()
    else:
        st.session_state.ready_phase = "memories"
        st.experimental_rerun()

# --- Step 3: Memory Phase ---
elif st.session_state.ready_phase == "memories":
    step = st.session_state.photo_step

    if step < len(photos_with_captions):
        photo, caption = photos_with_captions[step]
        try:
            image = Image.open(photo)
            st.image(image, use_column_width=True)
        except Exception:
            st.warning(f"Could not load image: {photo}")
        st.markdown(f"**_{caption}_**")
        if st.button("Next ➡️"):
            st.session_state.photo_step += 1
            st.experimental_rerun()
    else:
        st.balloons()
        st.markdown("### 🥹 You've reached the end of our little journey...")
        st.markdown("#### But here's a little something from me to you 💌")
        st.markdown(final_poem)

        if not st.session_state.show_poem:
            if st.button("💗 Show Hearts 💗"):
                st.session_state.show_poem = True
                st.experimental_rerun()

        if st.session_state.show_poem:
            heart_row = ["❤️", "💖", "💘", "💕", "💞", "💓", "💗", "💝"]
            for i in range(8):
                st.markdown(
                    f"<h1 style='text-align: center;'>{heart_row[i % len(heart_row)]}</h1>",
                    unsafe_allow_html=True,
                )
                time.sleep(0.3)
