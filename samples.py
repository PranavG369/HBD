import streamlit as st
from deep_translator import GoogleTranslator

# Function to display birthday wishes with effects
def display_birthday_wish(name, language):
    if language == "Hindi":
        st.success("जन्मदिन की हार्दिक शुभकामनाएँ सुंदरी!")
        st.write(f"WUUHUUUU आज किसी का जन्मदिन है... और वो कौन है?? ये आप {name} हैं, हाँ सुश्री निवेदिता फड़के (सुश्री जेलीफ़िश और बाकी सारे नाम जिनसे मैं आपको पुकारता हूँ, हेहेहेहे)!!! जन्मदिन मुबारक हो, महिला")
        st.image("hindi.gif", width=600)
        st.balloons()
        st.snow()

    elif language == "English":
        st.success("Happy Birthday Beautiful!")
        st.write(f"WUUHUUUU it's someone's birthday today... and who's that someone?? IT'S YOUUU, Yes Ms. Nivedita Phadke (Ms. Jellyfish and all the other names that I call you hehehehe)!!! Happy birthday girll!!!!")
        st.image("english.gif", width=600)
        st.snow()
        st.balloons()

    elif language == "Gujarati":
        st.success("જન્મદિવસ ની હાર્દિક શુભેચ્છાઓ સુંદરી!")
        st.write(f"WUUHUUUU, આજે કોઈનો જન્મદિવસ છે... અને કોણ છે?? તે તમે છો, હા શ્રીમતી નિવેદિતા ફડકે (શ્રીમતી જેલીફિશ અને બીજા બધા નામો જે હું તમને બોલાવું છું, હેહેહેહે)!!! જન્મદિવસની શુભેચ્છાઓ, લેડી!!!!")
        st.image("guj.gif", width=600)
        st.snow()
        st.balloons()

    elif language == "German":
        st.success("Alles Gute zum Geburtstag, schöne!")
        st.write(f"WUUHUUUU, heute hat jemand Geburtstag ... und wer ist dieser Jemand?? DU BIST ES, ja, Ms. Nivedita Phadke (Ms. Jellyfish und all die anderen Namen, mit denen ich dich nenne, hehehehe)!!! Alles Gute zum Geburtstag, Mädchen!!!!")
        st.image("ger.gif", width=600)
        st.snow()
        st.balloons()

# Optional: Translate any sentence to English
def translate_to_english(sentence, source_lang):
    try:
        return GoogleTranslator(source=source_lang, target='en').translate(sentence)
    except Exception as e:
        return f"Translation failed: {e}"

def main():
    st.title("Hmmmm kya hai ye??🤔")
    st.subheader("What this might be?? AREY SOCHO MAT, DEKHO SIDHA! BWAHAHAHAHAA 😎🥂")
    st.write(
        "Well, there's a lot to write and I can go on for days if you'd be listening patiently 😆, "
        "which you won't because ufff your patience i know kitna hai vo 😆 "
        "so ye app pe kuch likh leta hu aur baaki toh texts pe mil hi janay teko hehehehe. "
        "You really some anokha chiz I must say ha... chal chal ab niche ek ek krke click kr aur maza dekh 😎"
    )
    st.image(["ITT.jpg"], caption=["Upgrade version 2.0"], width=900)

    # Language checkboxes
    st.write("🎂 Choose how you want your birthday wish:")
    hindi_wish = st.checkbox("Hindi")
    english_wish = st.checkbox("English")
    gujarati_wish = st.checkbox("Gujarati")
    german_wish = st.checkbox("German")

    # Name input
    name = st.text_input("👩‍💻 Enter your name:")

    if name:
        if hindi_wish:
            display_birthday_wish(name, "Hindi")
        if english_wish:
            display_birthday_wish(name, "English")
        if gujarati_wish:
            display_birthday_wish(name, "Gujarati")
        if german_wish:
            display_birthday_wish(name, "German")
    else:
        st.warning("👀 Enter your name to unlock the surprise!")

if __name__ == "__main__":
    main()




