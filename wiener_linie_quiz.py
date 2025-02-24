import streamlit as st
import random

# Titel der Web-App
st.title("🚋 Wiener Linien & Bezirke Lern-Modus")

st.write("Wähle, was du lernen möchtest:")

# Definition der Daten
tram_lines = {
    "1": "Stefan-Fadinger-Platz ↔ Prater, Hauptallee",
    "2": "Friedrich-Engels-Platz ↔ Dornbach",
    "5": "Praterstern ↔ Westbahnhof",
    "6": "Burggasse-Stadthalle ↔ Geiereckstraße",
    "9": "Gersthof, Wallrißstraße ↔ Westbahnhof",
    "10": "Dornbach ↔ Unter St.Veit, Hummelgasse",
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
}

# Session-State zur Speicherung der Auswahl und Lernfortschritt
if "current_category" not in st.session_state:
    st.session_state.current_category = None
    st.session_state.current_item = None
    st.session_state.current_answer = None
    st.session_state.learned_items = {"tram": set(), "ubahn": set(), "district": set()}

# Buttons für die Auswahl des Lernmodus
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🚇 U-Bahn lernen"):
        st.session_state.current_category = "ubahn"
with col2:
    if st.button("🚋 Straßenbahn lernen"):
        st.session_state.current_category = "tram"
with col3:
    if st.button("🏙️ Bezirke lernen"):
        st.session_state.current_category = "district"

# Funktion zum Neuauswählen eines zufälligen Lerninhalts, wobei bereits gelernte Inhalte seltener gewählt werden
def new_item(category):
    all_items = list(ubahn_lines.keys() if category == "ubahn" else tram_lines.keys() if category == "tram" else districts.keys())
    not_learned = [item for item in all_items if item not in st.session_state.learned_items[category]]
    if not_learned:
        st.session_state.current_item = random.choice(not_learned)
    else:
        st.session_state.current_item = random.choice(all_items)  # Falls alles gelernt wurde, wiederhole zufällig
    st.session_state.current_answer = ubahn_lines.get(st.session_state.current_item, tram_lines.get(st.session_state.current_item, districts.get(st.session_state.current_item)))

# Falls eine Kategorie gewählt wurde, zeige eine Frage
if st.session_state.current_category:
    if st.button("🔄 Neue Frage anzeigen"):
        new_item(st.session_state.current_category)

    if st.session_state.current_item:
        st.write("### ❓ Was gehört zu dieser Nummer oder Linie?")
        st.write(f"**{st.session_state.current_item}**")

        if st.button("💡 Antwort anzeigen"):
            st.write(f"### ✅ {st.session_state.current_answer}")

            if st.button("✅ Ich wusste es!"):
                st.session_state.learned_items[st.session_state.current_category].add(st.session_state.current_item)

            if st.button("❌ Ich wusste es nicht"):
                st.session_state.learned_items[st.session_state.current_category].discard(st.session_state.current_item)

# Reset-Button zum Neustart des Lernens
if st.button("🔄 Gesamtes Lernen zurücksetzen"):
    st.session_state.learned_items = {"tram": set(), "ubahn": set(), "district": set()}
    st.session_state.current_item = None
    st.session_state.current_answer = None
    st.session_state.current_category = None
    st.experimental_rerun()

st.write("📚 Viel Erfolg beim Lernen! 🚋🚇🏙️")
