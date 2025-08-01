import streamlit as st
from deep_translator import GoogleTranslator

# Function to display birthday wishes with effects
def display_birthday_wish(name, language):
    if language == "Hindi":
        st.success("जन्मदिन की हार्दिक शुभकामनाएँ सुंदरी!")
        st.write(f"WUUHUUUU आज किसी का जन्मदिन है... और वो कौन है?? ये आप {name} हैं, हाँ सुश्री निवेदिता फड़के (सुश्री जेलीफ़िश और बाकी सारे नाम जिनसे मैं आपको पुकारता हूँ, हेहेहेहे)!!! जन्मदिन मुबारक हो, महिला")
        st.write("नरम सी तुझसे जुड़ी हर बात लगती है ख़ास,")
        st.write("इशारे तेरे, जैसे चाँदनी का मधुर एहसास।")
        st.write("वादे नहीं, पर तेरा साथ हर पल में है,")
        st.write("एक पल भी तुझसे दूर रहना आसान नहीं है।")
        st.write("दिल की हर धड़कन तुझमें ही खो जाती है,")
        st.write("इश्क़ मेरा तेरी मुस्कान में झलकती है।")
        st.write("तू ही तो है जो रंग भरती है हर एक शाम में,")
        st.write("आज भी तू पास हो, तो दुनिया लगती है एक आरामगाह में।")
        st.image("hindi.gif", width=600)
        st.balloons()
        st.snow()

    elif language == "Marathi":
        st.success("वाढदिवसाच्या हार्दिक शुभेच्छा सुंदरी!")
        st.write(f"आज कोणाचा तरी वाढदिवस आहे... आणि ती व्यक्ती कोण आहे?? हे तूच {name} आहेस, हो सुश्री निवेदिता फडके (सुश्री जेलीफिश आणि मी तुला ज्या नावांनी हाक मारतो ती सर्व नावे)!!! वाढदिवसाच्या शुभेच्छा मुली")
        st.write("निवांत क्षणी तू मला ऊब देतेस,")
        st.write("निवांत क्षणी तू मला ऊब देतेस....")
        st.write("इतक्या गोड शब्दांनी तू मनात गुंतवतेस.")
        st.write("वेडं वाऱ्यासारखं तू हळूच स्पर्श करतेस,")
        st.write("वेडं वाऱ्यासारखं तू हळूच स्पर्श करतेस....")
        st.write("एकटक प्रेमाने माझं जग सजवतेस.....")
        st.write("दिवस थांबतो, जेव्हा हसून तू बघतेस,")
        st.write("दिवस थांबतो, जेव्हा हसून तू बघतेस....")
        st.write("इंद्रधनूसारखी तू माझं आभाळ रंगवतेस......")
        st.write("तुझ्या नावातच प्रेमाची कविता उमटते,")
        st.write("तुझ्या नावातच प्रेमाची कविता उमटते....")
        st.write("आयुष्यभरासाठी तुझं अस्तित्वच माझ्या जगात दरवळते....")
        st.image("marathi.gif", width=600)
        st.snow()
        st.balloons()

    elif language == "English":
        st.success("Happy Birthday Beautiful!")
        st.write(f"WUUHUUUU it's someone's birthday today... and who's that someone?? IT'S YOUUU {name}, Yes Ms. Nivedita Phadke (Ms. Jellyfish and all the other names that I call you hehehehe)!!! Happy birthday girll!!!!")
        st.write("Night falls softer when your name echoes in my heart.")
        st.write("I see galaxies in your eyes, a world I never want to part.")
        st.write("Vows unspoken still dance in the silence we share.")
        st.write("Every heartbeat I own whispers that you’re rare.")
        st.write("Dreams blur gently into memories of your smile.")
        st.write("In your presence, time halts and rests awhile.")
        st.write("Touches of yours linger like stardust on skin.")
        st.write("And in every lifetime, I’d choose you again and again..")
        st.image("english.gif", width=600)
        st.snow()
        st.balloons()

    elif language == "Gujarati":
        st.success("જન્મદિવસ ની હાર્દિક શુભેચ્છાઓ સુંદરી!")
        st.write(f"WUUHUUUU, આજે કોઈનો જન્મદિવસ છે... અને કોણ છે?? તે તમે છો {name}, હા શ્રીમતી નિવેદિતા ફડકે (શ્રીમતી જેલીફિશ અને બીજા બધા નામો જે હું તમને બોલાવું છું, હેહેહેહે)!!! જન્મદિવસની શુભેચ્છાઓ, લેડી!!!!")
        st.write("નમ્રતાથી તું મારા જીવનમાં પ્રવેશી ગઈ")
        st.write("ઇચ્છાઓને તારા સ્પર્શથી શાંતિ મળી ગઈ।")
        st.write("વર્ષોમાંએક તારો સ્મિત એ મારા માટે આખું વિશ્વ છે,")
        st.write("એકલપના કરતાં પણ વધુ તું મારી લાગણીઓનું કેન્દ્ર છે।")
        st.write("દિવસનું તેજ તારી આંખોમાં ઝળહળે છે,")
        st.write("ઇમદ્ર સ્વરથી તું મન ભીંજવે છે।")
        st.write("તૂં આ જિંદગીનો સૌથી મીઠો રહસ્ય છે,")
        st.write("આખા યુગો સુધી પણ તું મારે માટે નવી લાગશે।")
        st.write("**MEANING**")
        st.write("नरमी से तुम मेरे जीवन में प्रवेश कर गई,")
        st.write("इच्छाओं को तुम्हारे स्पर्श से शांति मिल गई।")
        st.write("वर्षों में एक तुम्हारी मुस्कान ही मेरे लिए पूरा संसार है,")
        st.write("ए कलपनाओं से भी ज़्यादा, तुम मेरी भावनाओं का केंद्र हो")
        st.write("दिन का उजाला तुम्हारी आँखों में चमकता है")
        st.write("इ मधुर स्वर से तुम मन को भीगा देती हो।")
        st.write("तुम इस ज़िंदगी का सबसे मीठा रहस्य हो,")
        st.write("आखिरी साँस तक भी तुम मेरे लिए नई ही लगोगी।")
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
    st.write("It's here It's finally here WUHUUUU, YOUR DAY!!!")
    st.write("The day the universe gave this world its most most mosttt precious creation YOU")
    st.write("And if i could i would write your name across the sky in stars, i would bottle everything that i've ever felt and pour it into your hands")
    st.write("But yk sacchai ye hai ki ye aasman, ye poetry, ya naye naye janam bhi try kru toh vo kam padega")
    st.write"So, its not just you Birthday but its the anniversary of the day the universe decided the world needed someone")
    st.write("someone magical, someone who would bring laughter where there was silence, love, where there was fear, and warmth where there was cold")
    st.write("And that someone is YOU!!")
    st.write("You are more than just beautiful, you are light (ujalaaaaaa lee aaye naye jaisi safedi😂), your are comfort, chaos and calm, all in perfect balance")
    st.write("Every little thing about you, your nind vali awaaz, aapk vo soft soft jhalak (jhalak dikhalaja),every every thing stays with me")
    st.write("I want a hundred more of your birthdays so i can celebrate you again and again, in a million little ways.")
    st.write("Not just with flowers or gifts or words… but with presence. With holding you when words aren’t needed, with standing by your side through every season, and with loving you the way stars love the night quietly, endlessly, without fail")
    st.write("I am proud of who you are. koi rahe na rahe mai hamesha rahunga keep that in mind samjhe kya jellyfish")
    st.write("So, more to come but ye yahi end krrau by saying... Happy Birthday Ms. Jellyfish💖 and ufff still a TEEN in your age😂😂😂😂😂😂")
    
    st.image(["ITT.jpg"], caption=["Upgrade version 2.0 of that It Takes Two jiska mai bolra tha hehehe, ohh btw version 3.0 baki hai ha 😂😁"], width=900)

    # Language checkboxes
    st.write("🎂 Choose konse language me aapko chahiye aapka birthday wish bwahahaha")
    st.write("P.S: ek time pe ek hi choose krna ji 😂😂")
    hindi_wish = st.checkbox("Hindi")
    marathi_wish = st.checkbox("Marathi")
    english_wish = st.checkbox("English")
    gujarati_wish = st.checkbox("Gujarati")
    german_wish = st.checkbox("German")

    # Name input
    name = st.text_input("👩‍💻 Enter your name: (toh ye raha aapka naam aapke screen par)")

    if name:
        if hindi_wish:
            display_birthday_wish(name, "Hindi")
        if marathi_wish:
            display_birthday_wish(name, "Marathi")
        if english_wish:
            display_birthday_wish(name, "English")
        if gujarati_wish:
            display_birthday_wish(name, "Gujarati")
        if german_wish:
            display_birthday_wish(name, "German")
    else:
        st.warning("👀 Enter your name to unlock the surprise ji!")

if __name__ == "__main__":
    main()




