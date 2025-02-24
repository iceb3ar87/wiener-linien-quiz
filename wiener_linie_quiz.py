import streamlit as st

# Titel der Web-App
st.title("🚋 Wiener Linien & Bezirke Quiz")

st.write("Teste dein Wissen über die Wiener Bezirke und das Wiener Öffi-Netz!")

# --------------------- Bezirks-Quiz --------------------- #
st.header("🏙️ Quiz: Welcher Bezirk hat welche Nummer?")

districts_quiz = {
    "Welcher Bezirk hat die Nummer 1?": ["Innere Stadt", "Leopoldstadt", "Favoriten", "Donaustadt"],
    "Welcher Bezirk hat die Nummer 10?": ["Josefstadt", "Favoriten", "Penzing", "Hietzing"],
    "Welcher Bezirk hat die Nummer 21?": ["Brigittenau", "Liesing", "Floridsdorf", "Neubau"],
    "Welcher Bezirk hat die Nummer 5?": ["Margareten", "Landstraße", "Alsergrund", "Hernals"],
    "Welcher Bezirk hat die Nummer 14?": ["Penzing", "Ottakring", "Meidling", "Simmering"]
}

correct_district_answers = {
    "Welcher Bezirk hat die Nummer 1?": "Innere Stadt",
    "Welcher Bezirk hat die Nummer 10?": "Favoriten",
    "Welcher Bezirk hat die Nummer 21?": "Floridsdorf",
    "Welcher Bezirk hat die Nummer 5?": "Margareten",
    "Welcher Bezirk hat die Nummer 14?": "Penzing"
}

district_score = 0
district_answers = {}

for question, options in districts_quiz.items():
    user_answer = st.selectbox(question, options, key=question)
    district_answers[question] = user_answer

if st.button("Bezirks-Quiz auswerten"):
    for question, answer in district_answers.items():
        if answer == correct_district_answers[question]:
            district_score += 1
    st.write(f"✅ Du hast {district_score}/{len(districts_quiz)} Bezirke richtig!")

# --------------------- U-Bahn-Quiz --------------------- #
st.header("🚇 Quiz: Welche Endstationen gehören zu welcher U-Bahn?")

ubahn_quiz = {
    "Welche Endstationen gehören zur U1?": ["Oberlaa - Leopoldau", "Hütteldorf - Heiligenstadt", "Siebenhirten - Floridsdorf", "Ottakring - Simmering"],
    "Welche Endstationen gehören zur U3?": ["Oberlaa - Leopoldau", "Hütteldorf - Heiligenstadt", "Ottakring - Simmering", "Seestadt - Karlsplatz"],
    "Welche Endstationen gehören zur U4?": ["Hütteldorf - Heiligenstadt", "Siebenhirten - Floridsdorf", "Ottakring - Simmering", "Seestadt - Karlsplatz"],
    "Welche Endstationen gehören zur U6?": ["Siebenhirten - Floridsdorf", "Oberlaa - Leopoldau", "Hütteldorf - Heiligenstadt", "Seestadt - Karlsplatz"],
}

correct_ubahn_answers = {
    "Welche Endstationen gehören zur U1?": "Oberlaa - Leopoldau",
    "Welche Endstationen gehören zur U3?": "Ottakring - Simmering",
    "Welche Endstationen gehören zur U4?": "Hütteldorf - Heiligenstadt",
    "Welche Endstationen gehören zur U6?": "Siebenhirten - Floridsdorf",
}

ubahn_score = 0
ubahn_answers = {}

for question, options in ubahn_quiz.items():
    user_answer = st.selectbox(question, options, key=question)
    ubahn_answers[question] = user_answer

if st.button("U-Bahn-Quiz auswerten"):
    for question, answer in ubahn_answers.items():
        if answer == correct_ubahn_answers[question]:
            ubahn_score += 1
    st.write(f"✅ Du hast {ubahn_score}/{len(ubahn_quiz)} U-Bahn-Fragen richtig!")

st.write("Viel Erfolg beim Lernen! 🚋")
