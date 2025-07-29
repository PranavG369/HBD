import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Happy Birthday Nivedita 💖", layout="centered", page_icon="🎂")

# --- Styling ---
st.markdown("""
    <style>
    body {
        background-color: #ffe6f0;
    }
    .big-text {
        font-size: 30px;
        text-align: center;
        color: #ff3399;
    }
    .heart-button button {
        background-color: #ff3399;
        color: white;
        font-size: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("💗 Happy Birthday, Ms. Jellyfish 💗")
st.markdown("<div class='big-text'>Here's a little surprise for you 🥹💕</div>", unsafe_allow_html=True)

# --- Gallery with messages ---
photos_with_captions = [
    ("photo1.jpg", "From the moment we met, the world began to shimmer."),
    ("photo2.jpg", "Your laughter, my favorite melody."),
    ("photo3.jpg", "Every photo, a memory I hold close."),
    ("photo4.jpg", "You make the ordinary feel magical."),
]

if "photo_step" not in st.session_state:
    st.session_state.photo_step = 0

if st.session_state.photo_step < len(photos_with_captions):
    photo, msg = photos_with_captions[st.session_state.photo_step]
    image = Image.open(photo)
    st.image(image, use_column_width=True)
    st.markdown(f"<div class='big-text'>{msg}</div>", unsafe_allow_html=True)
    if st.button("Next Memory ➡️"):
        st.session_state.photo_step += 1
        st.experimental_rerun()
else:
    # --- Poem Section ---
    if "poem_shown" not in st.session_state:
        st.session_state.poem_shown = False

    if not st.session_state.poem_shown:
        if st.button("📜 Read Poem"):
            st.session_state.poem_shown = True
            st.experimental_rerun()
    else:
        st.markdown("""
        ### A Poem for You 💕
        Roses are red, violets are blue,  
        You lit my world the moment I found you.  
        With every smile, every glance you send,  
        I found in you my love, my friend.  

        You're the jellyfish of joy in my sea,  
        The hydrogen atom completing me.  
        So here’s my heart, so full and true,  
        I’ve been waiting to say this to you... 💗
        """)
        if st.button("Done Reading 🥹"):
            st.session_state["poem_done"] = True
            st.experimental_rerun()

# --- YES Game ---
if st.session_state.get("poem_done"):
    if "click_count" not in st.session_state:
        st.session_state.click_count = 0

    st.markdown("<br><hr><br>", unsafe_allow_html=True)
    st.markdown("### Ready for the final surprise? 💞")

    if st.button("CLICK ME 💌"):
        st.session_state.click_count += 1
        time.sleep(0.3)
        st.experimental_rerun()

    count = st.session_state.click_count

    if count < 3:
        st.markdown(f"<div class='big-text'>NO 😝</div>", unsafe_allow_html=True)
    elif count == 3:
        st.markdown(f"<div class='big-text' style='font-size:50px;'>CLICK ME! 😤</div>", unsafe_allow_html=True)
    elif count >= 4:
        st.markdown(f"""
        <div class='big-text' style='font-size:60px;'>
        YES 💍💖<br><br>
        I’ve been yours from the moment you asked — and forever after. 🥺<br>
        Happy Birthday Nivedita 💫
        </div>
        """, unsafe_allow_html=True)

# --- Bonus Ideas Section ---
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.markdown("### 💡 Bonus Love Bits:")
with st.expander("📖 Love Timeline"):
    st.markdown("""
    - 🌟 **Day 1**: We met — and my world flipped.
    - 💬 **First Words**: You made me nervous and smiley.
    - 💑 **Our First 'Us' Moment**: I knew this was different.
    - 🥹 **You Said Yes**: And it was the beginning of everything.
    """)

with st.expander("🎁 Why I Love You"):
    st.markdown("""
    - You're thoughtful in a way no one else is.
    - You see the little things.
    - You make me laugh when I don’t want to smile.
    - You’re my calm and my chaos, all in one.
    """)

with st.expander("🌌 What's Next?"):
    st.markdown("""
    - More cuddles, more chaos, and a lifetime of silly love.
    - Adventures, poems, late-night talks.
    - Someday, maybe even our own little planet of love. 🪐💕
    """)
