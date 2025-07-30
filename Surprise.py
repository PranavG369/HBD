import streamlit as st
from PIL import Image

# List of (photo_filename, caption) — make sure these images are in the same folder!
photos_with_captions = [
    ("photo1.jpg", "The day you looked at me like the whole galaxy was inside me."),
    ("photo2.jpg", "Our cutest little memory ever!"),
    ("photo3.jpg", "Just you being you, stealing my heart again."),
    ("photo4.jpg", "That time you laughed and I knew I was home."),
    ("photo5.jpg", "Your eyes, your smile — I fall every time."),
]

# Poem at the end
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

# App title
st.title("🎉 Happy Birthday My Love 💖")
st.markdown("#### Let's go on a small memory lane journey...")

# CSS to center images and buttons
st.markdown("""
    <style>
        .centered { display: flex; justify-content: center; align-items: center; flex-direction: column; }
        .stButton>button { font-size: 18px; padding: 10px 20px; border-radius: 12px; background-color: #ff4b4b; color: white; }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'photo_step' not in st.session_state:
    st.session_state.photo_step = 0

# Main display
def main():
    step = st.session_state.photo_step

    if step < len(photos_with_captions):
        photo, caption = photos_with_captions[step]
        st.markdown("<div class='centered'>", unsafe_allow_html=True)

        try:
            image = Image.open(photo)
            st.image(image, use_column_width=True)
        except Exception as e:
            st.warning(f"Couldn't load image: `{photo}`. Did you forget to add it to your repo?")
        
        st.markdown(f"**_{caption}_**", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("Next ➡️"):
            st.session_state.photo_step += 1
            st.experimental_rerun()

    else:
        st.balloons()
        st.markdown("### 🥹 You've reached the end of our little journey...")
        st.markdown("#### But here's a little something from me to you 💌")
        st.markdown(final_poem)

main()
