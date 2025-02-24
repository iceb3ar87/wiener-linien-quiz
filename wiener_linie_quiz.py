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

# --------------------- Straßenbahn-Quiz --------------------- #
st.header("🚋 Straßenbahn-Quiz")

tram_lines = {
    "1": "Stefan-Fadinger-Platz ↔ Prater, Hauptallee",
    "2": "Friedrich-Engels-Platz ↔ Dornbach",
    "5": "Praterstern ↔ Westbahnhof",
    "6": "Burggasse-Stadthalle ↔ Geiereckstraße",
    "9": "Gersthof, Wallrißstraße ↔ Westbahnhof",
}

for line, correct_answer in tram_lines.items():
    options = [correct_answer, "Ring ↔ Volkstheater", "Simmering ↔ Ottakring"]
    user_answer = st.radio(f"Welche Endstationen gehören zur Linie {line}?", options, key=f"tram_{line}")
    if user_answer:
        if user_answer == correct_answer:
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
}

for line, correct_answer in ubahn_lines.items():
    options = [correct_answer, "Heiligenstadt ↔ Hütteldorf", "Seestadt ↔ Simmering"]
    user_answer = st.radio(f"Welche Endstationen gehören zur {line}?", options, key=f"ubahn_{line}")
    if user_answer:
        if user_answer == correct_answer:
            st.markdown('<p class="correct">✅ Richtig!</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="incorrect">❌ Falsch! Richtige Antwort: {correct_answer}</p>', unsafe_allow_html=True)

# --------------------- Bezirks-Quiz --------------------- #
st.header("🏙️ Bezirks-Quiz")

districts = {
    "1": "Innere Stadt", "2": "Leopoldstadt", "3": "Landstraße", "4": "Wieden",
    "5": "Margareten", "6": "Mariahilf", "7": "Neubau", "8": "Josefstadt",
}

for num, correct_answer in districts.items():
    options = [correct_answer, "Favoriten", "Hietzing"]
    user_answer = st.radio(f"Welcher Bezirk ist Nummer {num}?", options, key=f"district_{num}")
    if user_answer:
        if user_answer == correct_answer:
            st.markdown('<p class="correct">✅ Richtig!</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="incorrect">❌ Falsch! Richtige Antwort: {correct_answer}</p>', unsafe_allow_html=True)

# --------------------- Reset-Funktion --------------------- #
if st.button("🔄 Quiz zurücksetzen"):
    st.experimental_rerun()

st.write("📚 Viel Erfolg beim Lernen! 🚋🚇🏙️")
