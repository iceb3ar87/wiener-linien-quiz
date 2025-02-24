import streamlit as st

# Titel der Web-App
st.title("🚋 Wiener Linien & Bezirke Lern-Quiz")

st.write("Lerne alle wichtigen Infos zu den Wiener Straßenbahnlinien, U-Bahn-Linien und Bezirken!")

# CSS für mobile Darstellung und Farbmarkierung
st.markdown(
    '''
    <style>
    .correct { color: green; font-weight: bold; font-size: 18px; }
    .incorrect { color: red; font-weight: bold; font-size: 18px; }
    </style>
    ''',
    unsafe_allow_html=True,
)

# Session-State für Antwortspeicherung
if "answers" not in st.session_state:
    st.session_state.answers = {}

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
    "O": "Raxstraße/Rudolfshügelgasse ↔ Bruno-Marek-Allee",
}

for line, correct_answer in tram_lines.items():
    options = [correct_answer, "Floridsdorf ↔ Simmering", "Hütteldorf ↔ Karlsplatz"]
    user_answer = st.selectbox(f"Welche Endstationen gehören zur Linie {line}?", options, key=f"tram_{line}")
    st.session_state.answers[f"tram_{line}"] = user_answer

# --------------------- U-Bahn-Quiz --------------------- #
st.header("🚇 U-Bahn-Quiz")

ubahn_lines = {
    "U1": "Oberlaa ↔ Leopoldau",
    "U2": "Seestadt ↔ Karlsplatz",
    "U3": "Ottakring ↔ Simmering",
    "U4": "Hütteldorf ↔ Heiligenstadt",
    "U6": "Siebenhirten ↔ Floridsdorf",
}

for line, correct_answer in ubahn_lines.items():
    options = [correct_answer, "Schottentor ↔ Hütteldorf", "Brigittenau ↔ Währing"]
    user_answer = st.selectbox(f"Welche Endstationen gehören zur {line}?", options, key=f"ubahn_{line}")
    st.session_state.answers[f"ubahn_{line}"] = user_answer

# --------------------- Bezirks-Quiz --------------------- #
st.header("🏙️ Bezirks-Quiz")

districts = {
    "1": "Innere Stadt", "2": "Leopoldstadt", "3": "Landstraße", "4": "Wieden",
    "5": "Margareten", "6": "Mariahilf", "7": "Neubau", "8": "Josefstadt",
    "9": "Alsergrund", "10": "Favoriten", "11": "Simmering", "12": "Meidling",
    "13": "Hietzing", "14": "Penzing", "15": "Rudolfsheim-Fünfhaus", "16": "Ottakring",
    "17": "Hernals", "18": "Währing", "19": "Döbling", "20": "Brigittenau",
    "21": "Floridsdorf", "22": "Donaustadt", "23": "Liesing",
}

for num, correct_answer in districts.items():
    options = [correct_answer, "Favoriten", "Penzing"]
    user_answer = st.selectbox(f"Welcher Bezirk ist Nummer {num}?", options, key=f"district_{num}")
    st.session_state.answers[f"district_{num}"] = user_answer

# --------------------- Auswertung --------------------- #
if st.button("📝 Antworten auswerten"):
    correct_count = 0
    total_questions = len(tram_lines) + len(ubahn_lines) + len(districts)

    for line, correct_answer in tram_lines.items():
        if st.session_state.answers[f"tram_{line}"] == correct_answer:
            st.markdown(f'<p class="correct">✅ Linie {line}: Richtig!</p>', unsafe_allow_html=True)
            correct_count += 1
        else:
            st.markdown(f'<p class="incorrect">❌ Linie {line}: Falsch! Richtige Antwort: {correct_answer}</p>', unsafe_allow_html=True)

    for line, correct_answer in ubahn_lines.items():
        if st.session_state.answers[f"ubahn_{line}"] == correct_answer:
            st.markdown(f'<p class="correct">✅ {line}: Richtig!</p>', unsafe_allow_html=True)
            correct_count += 1
        else:
            st.markdown(f'<p class="incorrect">❌ {line}: Falsch! Richtige Antwort: {correct_answer}</p>', unsafe_allow_html=True)

    for num, correct_answer in districts.items():
        if st.session_state.answers[f"district_{num}"] == correct_answer:
            st.markdown(f'<p class="correct">✅ Bezirk {num}: Richtig!</p>', unsafe_allow_html=True)
            correct_count += 1
        else:
            st.markdown(f'<p class="incorrect">❌ Bezirk {num}: Falsch! Richtige Antwort: {correct_answer}</p>', unsafe_allow_html=True)

    st.write(f"🎯 Dein Ergebnis: **{correct_count}/{total_questions} richtig**")

# --------------------- Reset-Funktion --------------------- #
if st.button("🔄 Quiz zurücksetzen"):
    st.session_state.answers = {}
    st.experimental_rerun()

st.write("📚 Viel Erfolg beim Lernen! 🚋🚇🏙️")
