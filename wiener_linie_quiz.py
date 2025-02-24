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

# Session-State für Antwortüberprüfung speichern
if "answers_checked" not in st.session_state:
    st.session_state.answers_checked = {}

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
}

for line, correct_answer in tram_lines.items():
    options = [correct_answer, "Falsche Option 1", "Falsche Option 2"]
    user_answer = st.radio(f"Welche Endstationen gehören zur Linie {line}?", options, key=f"tram_{line}")
    
    if user_answer and f"tram_{line}" not in st.session_state.answers_checked:
        st.session_state.answers_checked[f"tram_{line}"] = user_answer

    if f"tram_{line}" in st.session_state.answers_checked:
        if st.session_state.answers_checked[f"tram_{line}"] == correct_answer:
            st.markdown('<p class="correct">✅ Richtig!</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="incorrect">❌ Falsch! Richtige Antwort: {correct_answer}</p>', unsafe_allow_html=True)

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
    options = [correct_answer, "Falsche Option 1", "Falsche Option 2"]
    user_answer = st.radio(f"Welche Endstationen gehören zur {line}?", options, key=f"ubahn_{line}")
    
    if user_answer and f"ubahn_{line}" not in st.session_state.answers_checked:
        st.session_state.answers_checked[f"ubahn_{line}"] = user_answer

    if f"ubahn_{line}" in st.session_state.answers_checked:
        if st.session_state.answers_checked[f"ubahn_{line}"] == correct_answer:
            st.markdown('<p class="correct">✅ Richtig!</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="incorrect">❌ Falsch! Richtige Antwort: {correct_answer}</p>', unsafe_allow_html=True)

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

for num, correct_answer in districts.items():
    options = [correct_answer, "Falsche Option 1", "Falsche Option 2"]
    user_answer = st.radio(f"Welcher Bezirk ist Nummer {num}?", options, key=f"district_{num}")
    
    if user_answer and f"district_{num}" not in st.session_state.answers_checked:
        st.session_state.answers_checked[f"district_{num}"] = user_answer

    if f"district_{num}" in st.session_state.answers_checked:
        if st.session_state.answers_checked[f"district_{num}"] == correct_answer:
            st.markdown('<p class="correct">✅ Richtig!</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="incorrect">❌ Falsch! Richtige Antwort: {correct_answer}</p>', unsafe_allow_html=True)

# --------------------- Reset-Funktion --------------------- #
if st.button("🔄 Quiz zurücksetzen"):
    st.session_state.answers_checked = {}
    st.experimental_rerun()

st.write("📚 Viel Erfolg beim Lernen! 🚋🚇🏙️")
