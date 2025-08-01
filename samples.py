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
        st.write(f"WUUHUUUU it's someone's birthday today... and who's that someone?? IT'S YOUUU {name}, Yes Ms. Nivedita Phadke (Ms. Jellyfish and all the other names that I call you hehehehe)!!! Happy birthday girll!!!!")
        st.image("english.gif", width=600)
        st.snow()
        st.balloons()

    elif language == "Gujarati":
        st.success("જન્મદિવસ ની હાર્દિક શુભેચ્છાઓ સુંદરી!")
        st.write(f"WUUHUUUU, આજે કોઈનો જન્મદિવસ છે... અને કોણ છે?? તે તમે છો {name}, હા શ્રીમતી નિવેદિતા ફડકે (શ્રીમતી જેલીફિશ અને બીજા બધા નામો જે હું તમને બોલાવું છું, હેહેહેહે)!!! જન્મદિવસની શુભેચ્છાઓ, લેડી!!!!")
        st.image("guj.gif", width=600)
        st.snow()
        st.balloons()

    elif language == "German":
        st.success("Alles Gute zum Geburtstag, schöne!")
        st.write(f"WUUHUUUU, heute hat jemand Geburtstag ... und wer ist dieser Jemand?? DU BIST ES {name}, ja, Ms. Nivedita Phadke (Ms. Jellyfish und all die anderen Namen, mit denen ich dich nenne, hehehehe)!!! Alles Gute zum Geburtstag, Mädchen!!!!")
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
        "🌟 T ZERO 🌟")
    st.write(
        "It's here It's finally here WUHUUUU, YOUR DAY!!!"
        "The day the universe gave this world its most most mosttt precious creation YOU"
        "And if i could i would write your name across the sky in stars, i would bottle everything that i've ever felt and pour it into your hands"
        "But yk sacchai ye hai ki ye aasman, ye poetry, ya naye naye janam bhi try kru toh vo kam padega"
        "So, its not just you Birthday but its the anniversary of the day the universe decided the world needed someone"
        "someone magical, someone who would bring laughter where there was silence, love, where there was fear, and warmth where there was cold"
        "and that someone is YOU!!"
        "You are more than just beautiful, you are light (ujalaaaaaa lee aaye naye jaisi safedi😂), your are comfort, chaos and calm, all in perfect balance"
        "Every little thing about you, your nind vali awaaz, aapk vo soft soft jhalak (jhalak dikhalaja),every every thing stays with me"
        "I want a hundred more of your birthdays so i can celebrate you again and again, in a million little ways."
        "Not just with flowers or gifts or words… but with presence. With holding you when words aren’t needed, with standing by your side through every season, and with loving you the way stars love the night quietly, endlessly, without fail"
        "I am proud of who you are. koi rahe na rahe mai hamesha rahunga keep that in mind samjhe kya jellyfish"
        "So, more to come but ye yahi end krrau by saying... Happy Birthday Ms. Jellyfish💖 and ufff still a TEEN in your age😂😂😂😂😂😂"
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




