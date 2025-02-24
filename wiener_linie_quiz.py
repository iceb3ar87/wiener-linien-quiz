import streamlit as st
import random

# Titel der Web-App
st.title("🚋 Wiener Linien & Bezirke Lern-Modus")

st.write("Lerne alle Wiener Straßenbahnlinien, U-Bahn-Linien und Bezirke schrittweise!")

# Definition der Daten
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

ubahn_lines = {
    "U1": "Oberlaa ↔ Leopoldau",
    "U2": "Seestadt ↔ Karlsplatz",
    "U3": "Ottakring ↔ Simmering",
    "U4": "Hütteldorf ↔ Heiligenstadt",
    "U6": "Siebenhirten ↔ Floridsdorf",
}

districts = {
    "1": "Innere Stadt", "2": "Leopoldstadt", "3": "Landstraße", "4": "Wieden",
    "5": "Margareten", "6": "Mariahilf", "7": "Neubau", "8": "Josefstadt",
    "9": "Alsergrund", "10": "Favoriten", "11": "Simmering", "12": "Meidling",
    "13": "Hietzing", "14": "Penzing", "15": "Rudolfsheim-Fünfhaus", "16": "Ottakring",
    "17": "Hernals", "18": "Währing", "19": "Döbling", "20": "Brigittenau",
    "21": "Floridsdorf", "22": "Donaustadt", "23": "Liesing",
}

# Session-State zur Speicherung der aktuellen Lernfrage
if "current_item" not in st.session_state:
    st.session_state.current_item = None
    st.session_state.current_answer = None

# Funktion zum Neuauswählen eines zufälligen Lerninhalts
def new_item():
    category = random.choice(["tram", "ubahn", "district"])
    if category == "tram":
        st.session_state.current_item = random.choice(list(tram_lines.keys()))
        st.session_state.current_answer = tram_lines[st.session_state.current_item]
    elif category == "ubahn":
        st.session_state.current_item = random.choice(list(ubahn_lines.keys()))
        st.session_state.current_answer = ubahn_lines[st.session_state.current_item]
    else:
        st.session_state.current_item = random.choice(list(districts.keys()))
        st.session_state.current_answer = districts[st.session_state.current_item]

# Button zum Starten oder Wechseln des Lerninhalts
if st.button("🔄 Neue Linie / Bezirk lernen"):
    new_item()

# Falls ein Lerninhalt aktiv ist, zeige ihn an
if st.session_state.current_item:
    st.write("### ❓ Was gehört zu dieser Nummer oder Linie?")
    st.write(f"**{st.session_state.current_item}**")

    if st.button("💡 Antwort anzeigen"):
        st.write(f"### ✅ {st.session_state.current_answer}")

st.write("📚 Viel Erfolg beim Lernen! 🚋🚇🏙️")
