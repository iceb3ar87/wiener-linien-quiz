import streamlit as st

# Titel der Web-App
st.title("🚋 Wiener Linien Quiz & Zuordnungsübung")

st.write("Teste dein Wissen über die Wiener Linien!")

# --------------------- Quiz --------------------- #
st.header("📝 Quiz: Welche Linie fährt wohin?")

quiz_questions = {
    "Welche Linie fährt von Stefan-Fadinger-Platz nach Prater, Hauptallee?": ["1", "2", "5", "6"],
    "Welche Linie fährt von Friedrich-Engels-Platz nach Dornbach?": ["1", "2", "10", "18"],
    "Welche Linie fährt von Praterstern nach Westbahnhof?": ["5", "6", "9", "11"],
    "Welche Linie fährt von Burggasse-Stadthalle nach Geiereckstraße?": ["6", "9", "18", "25"],
    "Welche Linie fährt von Gersthof, Wallrißstraße nach Westbahnhof?": ["9", "10", "18", "31"],
    "Welche Linie fährt von Dornbach nach Unter St. Veit, Hummelgasse?": ["10", "11", "18", "26"],
    "Welche Linie fährt von Otto-Probst-Platz nach Kaiserebersdorf, Zinnergasse?": ["11", "25", "26", "30"],
    "Welche Linie fährt von Burggasse-Stadthalle nach Schlachthausgasse?": ["18", "26", "30", "31"],
    "Welche Linie fährt von Oberdorfstraße nach Floridsdorf?": ["25", "26", "30", "33"],
    "Welche Linie fährt von Strebersdorf, Edmund-Hawranek-Platz nach Hausfeldstraße?": ["26", "30", "31", "33"],
}

correct_answers = {
    "Welche Linie fährt von Stefan-Fadinger-Platz nach Prater, Hauptallee?": "1",
    "Welche Linie fährt von Friedrich-Engels-Platz nach Dornbach?": "2",
    "Welche Linie fährt von Praterstern nach Westbahnhof?": "5",
    "Welche Linie fährt von Burggasse-Stadthalle nach Geiereckstraße?": "6",
    "Welche Linie fährt von Gersthof, Wallrißstraße nach Westbahnhof?": "9",
    "Welche Linie fährt von Dornbach nach Unter St. Veit, Hummelgasse?": "10",
    "Welche Linie fährt von Otto-Probst-Platz nach Kaiserebersdorf, Zinnergasse?": "11",
    "Welche Linie fährt von Burggasse-Stadthalle nach Schlachthausgasse?": "18",
    "Welche Linie fährt von Oberdorfstraße nach Floridsdorf?": "25",
    "Welche Linie fährt von Strebersdorf, Edmund-Hawranek-Platz nach Hausfeldstraße?": "26",
}

quiz_score = 0
quiz_answers = {}

for question, options in quiz_questions.items():
    user_answer = st.selectbox(question, options, key=question)
    quiz_answers[question] = user_answer

# Button zur Überprüfung
if st.button("Quiz auswerten"):
    for question, answer in quiz_answers.items():
        if answer == correct_answers[question]:
            quiz_score += 1
    st.write(f"✅ Du hast {quiz_score}/{len(quiz_questions)} Fragen richtig!")

# --------------------- Zuordnungsübung --------------------- #
st.header("🔄 Zuordnungsübung: Linie → Endstation")

matching_lines = {
    "1": "Prater, Hauptallee",
    "2": "Dornbach",
    "5": "Westbahnhof",
    "6": "Geiereckstraße",
    "9": "Westbahnhof",
    "10": "Unter St. Veit, Hummelgasse",
    "11": "Kaiserebersdorf, Zinnergasse",
    "18": "Schlachthausgasse",
    "25": "Floridsdorf",
    "26": "Hausfeldstraße",
}

matching_options = list(matching_lines.values())
matching_answers = {}
matching_score = 0

for line in matching_lines.keys():
    matching_answers[line] = st.selectbox(f"Linie {line} →", matching_options, key=line)

if st.button("Zuordnung auswerten"):
    for line, endstation in matching_answers.items():
        if endstation == matching_lines[line]:
            matching_score += 1
    st.write(f"✅ Du hast {matching_score}/{len(matching_lines)} Zuordnungen richtig!")

st.write("Viel Erfolg beim Lernen! 🚋")
