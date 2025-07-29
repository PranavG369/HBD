import streamlit as st
from googletrans import Translator

# Function to display birthday wishes with effects
def display_birthday_wish(name, language):
    if language == "Hindi":
        st.success("जन्मदिन की हार्दिक शुभकामनाएँ सुंदरी!")
        st.write(f"वाह, आज किसी का जन्मदिन है... और वह कौन है? हाँ, वह {name} हैं! हाँ श्रीमती नंदी (नंदिनीम)! जन्मदिन की ढेर सारी शुभकामनाएँ महिला!!")
        st.image("hindi.gif")
        st.balloons()
        st.snow()

    elif language == "English":
        st.success("Happy Birthday Beautiful!")
        st.write(f"Woohoo its someone's birthday today... and who's that someone?? ITS YOUUU, Yes Ms. Nandy (Nandinem)!!! Happy birthday girll!!!!")
        st.image("english.gif")
        st.snow()
        st.balloons()
    elif language == "Gujarati":
        st.success("જન્મદિવસ ની હાર્દિક શુભેચ્છાઓ સુંદરી!")
        st.write(f"Woohoo આજ કોઈનો જન્મદિવસ છે... અને તે કોણ છે?? હા, તું છે! હાઁ Ms. Nandy (Nandinem)!!! Happy birthday છોકરી!!!!")
        st.image("guj.gif")
        st.snow()
        st.balloons()
    elif language == "German":
        st.success("Alles Gute zum Geburtstag schöne!")
        st.write(f"Woohoo heute hat jemand Geburtstag... und wer ist das?? ES BIST DU, Ja Ms. Nandy (Nandinem)!!! Alles Gute zum Geburtstag Mädchen!!!!")
        st.image("ger.gif")
        st.snow()
        st.balloons()

def translate_to_english(sentence, language):
    translator = Translator()
    translated_text = translator.translate(sentence, src=language, dest="en")
    return translated_text.text

def main():
    st.title("Hmmmm kya hai ye??🤔")
    st.subheader("what this might be??, AREY SOCHO MAT DEKHO SIDHA BWAHAHAHAHAA MELODY KHAO KHUD JAAN JAAO 😎🥂")
    st.write("Well, there's a lot to write and I can go on for days if you'd be listening patiently 😆, which you won't because ufff your patience i know kitna hai vo😆so ye app pe kuch likh leta hu aur baki toh texts pe mil hi janay teko hehehehe. You really some anokha chiz i must say ha, hmmmm aur kya kya bolke yaha time nikalu tera..... 🤔 chal chal ab niche ek ek krke click kr aur maza dekh😎")

    # Toggle boxes for selecting language
    hindi_wish = st.checkbox("Hindi")
    english_wish = st.checkbox("English")
    gujarati_wish = st.checkbox("Gujarati")
    german_wish = st.checkbox("German")
    malayalam_wish = st.checkbox("Malayalam")

    # Get user's name
    name = st.text_input("Enter your name:")

    # Display birthday wish and effects based on selected language
    if hindi_wish:
        display_birthday_wish(name, "Hindi")
    if english_wish:
        display_birthday_wish(name, "English")
    if gujarati_wish:
        display_birthday_wish(name, "Gujarati")
    if german_wish:
        display_birthday_wish(name, "German")
        
if __name__ == "__main__":
    main()
