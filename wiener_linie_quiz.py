import streamlit as st
import random

# Titel der Web-App
st.title("🚋 Wiener Linien, U-Bahn & Bezirke Lern-Quiz")

st.write("Lerne alle wichtigen Infos zu den Wiener Bezirken, U-Bahn- und Straßenbahnlinien auf interaktive Weise!")

# --------------------- Bezirks-Quiz --------------------- #
st.header("🏙️ Bezirks-Quiz: Nummer & Name zuordnen")

districts = {
    "1": "Innere Stadt", "2": "Leopoldstadt", "3": "Landstraße", "4": "Wieden",
    "5": "Margareten", "6": "Mariahilf", "7": "Neubau", "8": "Josefstadt",
    "9": "Alsergrund", "10": "Favoriten", "11": "Simmering", "12": "Meidling",
    "13": "Hietzing", "14": "Penzing", "15": "Rudolfsheim-Fünfhaus", "16": "Ottakring",
    "17": "Hernals", "18": "Währing", "19": "Döbling", "20": "Brigittenau",
    "21": "Floridsdorf", "22": "Donaustadt", "23": "Liesing"
}

district_options = list(districts.values())
random.shuffle(district_options)
district_quiz = {num: st.selectbox(f"Welcher Bezirk ist Nummer {num}?", district_options, key=f"district_{num}") for num in districts.keys()}

if st.button("Bezirks-Quiz auswerten"):
    score = sum(1 for num, ans in district_quiz.items() if districts[num] == ans)
    st.write(f"✅ Du hast {score}/{len(districts)} Bezirke richtig!")

# --------------------- U-Bahn-Quiz --------------------- #
st.header("🚇 U-Bahn-Quiz: Welche Endstationen gehören zusammen?")

ubahn_lines = {
    "U1": "Oberlaa - Leopoldau",
    "U2": "Seestadt - Karlsplatz",
    "U3": "Ottakring - Simmering",
    "U4": "Hütteldorf - Heiligenstadt",
    "U6": "Siebenhirten - Floridsdorf"
}

ubahn_options = list(ubahn_lines.values())
random.shuffle(ubahn_options)
ubahn_quiz = {line: st.selectbox(f"Welche Endstationen gehören zur {line}?", ubahn_options, key=f"ubahn_{line}") for line in ubahn_lines.keys()}

if st.button("U-Bahn-Quiz auswerten"):
    score = sum(1 for line, ans in ubahn_quiz.items() if ubahn_lines[line] == ans)
    st.write(f"✅ Du hast {score}/{len(ubahn_lines)} U-Bahn-Fragen richtig!")

# --------------------- Straßenbahn-Quiz --------------------- #
st.header("🚋 Straßenbahn-Quiz: Linie & Endstationen")

tram_lines = {
    "D": "Nußdorf, Beethovengang",
    "2": "Dornbach",
    "5": "Westbahnhof",
    "6": "Geiereckstraße",
    "9": "Westbahnhof",
    "10": "Unter St. Veit, Hummelgasse",
    "11": "Kaiserebersdorf, Zinnergasse",
    "18": "Schlachthausgasse",
    "25": "Floridsdorf",
    "26": "Hausfeldstraße",
    "30": "Stammersdorf",
    "31": "Stammersdorf",
    "33": "Friedrich-Engels-Platz",
    "37": "Hohe Warte",
    "38": "Grinzing",
    "40": "Herbeckstraße",
    "41": "Pötzleinsdorf",
    "42": "Antonigasse",
    "43": "Neuwaldegg",
    "44": "Maroltingergasse",
    "46": "Joachimsthalerplatz",
    "49": "Hütteldorf, Bujattigasse",
    "52": "Baumgarten",
    "60": "Rodaun",
    "62": "Lainz, Wolkersbergenstraße",
    "71": "Kaiserebersdorf, Zinnergasse",
    "O": "Bruno-Marek-Allee"
}

tram_options = list(tram_lines.values())
random.shuffle(tram_options)
tram_quiz = {line: st.selectbox(f"Welche Endstation gehört zur Linie {line}?", tram_options, key=f"tram_{line}") for line in tram_lines.keys()}

if st.button("Straßenbahn-Quiz auswerten"):
    score = sum(1 for line, ans in tram_quiz.items() if tram_lines[line] == ans)
    st.write(f"✅ Du hast {score}/{len(tram_lines)} Straßenbahn-Fragen richtig!")

st.write("📚 Viel Erfolg beim Lernen! 🚋🚇🏙️")
