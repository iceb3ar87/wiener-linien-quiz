import streamlit as st
import random

# Titel der Web-App
st.title("🚋 Wiener Linien & Bezirke Lern-Quiz")

st.write("Lerne alle wichtigen Infos zu den Wiener Straßenbahnlinien, U-Bahn-Linien und Bezirken!")

# Session-State für falsche Antworten speichern und neu abfragen
if "incorrect_answers" not in st.session_state:
    st.session_state.incorrect_answers = {"tram": {}, "ubahn": {}, "district": {}}

# --------------------- Straßenbahn-Quiz --------------------- #
st.header("🚋 Straßenbahn-Quiz")

tram_lines = {
    "1": "Stefan-Fadinger-Platz ↔ Prater, Hauptallee",
    "2": "Friedrich-Engels-Platz ↔ Dornbach",
    "5": "Praterstern ↔ Westbahnhof",
    "6": "Burggasse-Stadthalle ↔ Geiereckstraße",
    "9": "Gersthof, Wallrißstraße ↔ Westbahnhof",
    "10": "Dornbach ↔ Unter St.Veit, Hummelgasse",
    "11": "Otto-Probst-Platz ↔ Kaiserebersdorf, Zinnergasse",
    "18": "Burggasse-Stadthalle ↔ Schlachthausgasse",
    "25": "Oberdorfstraße ↔ Floridsdorf",
    "26": "Strebersdorf, Edmund-Hawranek-Platz ↔ Hausfeldstraße",
    "30": "Floridsdorf ↔ Stammersdorf",
    "31": "Schottenring ↔ Stammersdorf",
    "33": "Josefstädter Straße ↔ Friedrich-Engels-Platz",
    "37": "Schottentor ↔ Hohe Warte",
    "38": "Schottentor ↔ Grinzing",
    "40": "Schottentor ↔ Herbeckstraße",
    "41": "Schottentor ↔ Pötzleinsdorf",
    "42": "Schottentor ↔ Antonigasse",
    "43": "Schottentor ↔ Neuwaldegg",
    "44": "Schottentor ↔ Maroltingergasse",
    "46": "Ring, Volkstheater ↔ Joachimsthalerplatz",
    "49": "Ring, Volkstheater ↔ Hütteldorf, Bujattigasse",
    "52": "Westbahnhof ↔ Baumgarten",
    "60": "Westbahnhof ↔ Rodaun",
    "62": "Oper, Karlsplatz ↔ Lainz, Wolkersbergenstraße",
    "71": "Börse ↔ Kaiserebersdorf, Zinnergasse",
    "D": "Absberggasse ↔ Nußdorf, Beethovengang",
    "O": "Raxstraße/Rudolfshügelgasse ↔ Bruno-Marek-Allee"
}

tram_options = list(tram_lines.values())
random.shuffle(tram_options)

tram_quiz = {}
for line, answer in tram_lines.items():
    tram_quiz[line] = st.selectbox(f"Welche Endstationen gehören zur Linie {line}?", tram_options, key=f"tram_{line}")

if st.button("Straßenbahn-Quiz auswerten"):
    st.session_state.incorrect_answers["tram"] = {line: ans for line, ans in tram_quiz.items() if tram_lines[line] != ans}
    correct = len(tram_lines) - len(st.session_state.incorrect_answers["tram"])
    st.write(f"✅ Du hast {correct}/{len(tram_lines)} Straßenbahn-Fragen richtig!")

# --------------------- U-Bahn-Quiz --------------------- #
st.header("🚇 U-Bahn-Quiz")

ubahn_lines = {
    "U1": "Oberlaa ↔ Leopoldau",
    "U2": "Seestadt ↔ Karlsplatz",
    "U3": "Ottakring ↔ Simmering",
    "U4": "Hütteldorf ↔ Heiligenstadt",
    "U6": "Siebenhirten ↔ Floridsdorf"
}

ubahn_options = list(ubahn_lines.values())
random.shuffle(ubahn_options)

ubahn_quiz = {}
for line, answer in ubahn_lines.items():
    ubahn_quiz[line] = st.selectbox(f"Welche Endstationen gehören zur {line}?", ubahn_options, key=f"ubahn_{line}")

if st.button("U-Bahn-Quiz auswerten"):
    st.session_state.incorrect_answers["ubahn"] = {line: ans for line, ans in ubahn_quiz.items() if ubahn_lines[line] != ans}
    correct = len(ubahn_lines) - len(st.session_state.incorrect_answers["ubahn"])
    st.write(f"✅ Du hast {correct}/{len(ubahn_lines)} U-Bahn-Fragen richtig!")

# --------------------- Bezirks-Quiz --------------------- #
st.header("🏙️ Bezirks-Quiz")

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

district_quiz = {}
for num, answer in districts.items():
    district_quiz[num] = st.selectbox(f"Welcher Bezirk ist Nummer {num}?", district_options, key=f"district_{num}")

if st.button("Bezirks-Quiz auswerten"):
    st.session_state.incorrect_answers["district"] = {num: ans for num, ans in district_quiz.items() if districts[num] != ans}
    correct = len(districts) - len(st.session_state.incorrect_answers["district"])
    st.write(f"✅ Du hast {correct}/{len(districts)} Bezirke richtig!")

# --------------------- Wiederholung der falschen Antworten --------------------- #
st.header("🔄 Wiederholung falscher Antworten")

if any(st.session_state.incorrect_answers.values()):
    st.write("⚠️ Die folgenden Fragen wurden falsch beantwortet. Versuche sie noch einmal!")

    for category, questions in st.session_state.incorrect_answers.items():
        for key, wrong_answer in questions.items():
            correct_answer = (tram_lines if category == "tram" else ubahn_lines if category == "ubahn" else districts)[key]
            st.write(f"❌ {key}: {wrong_answer} ❌ → Richtige Antwort: {correct_answer}")

# --------------------- Reset-Funktion --------------------- #
if st.button("🔄 Quiz zurücksetzen"):
    st.session_state.incorrect_answers = {"tram": {}, "ubahn": {}, "district": {}}
    st.experimental_rerun()

st.write("📚 Viel Erfolg beim Lernen! 🚋🚇🏙️")
