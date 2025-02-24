import streamlit as st

# Titel der Web-App
st.title("🚋 Wiener Linien & Bezirke Lern-Modus")

st.write("Lerne alle Wiener Straßenbahnlinien, U-Bahn-Linien und Bezirke der Reihe nach!")

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

# Reihenfolge der Abfrage definieren
all_items = (
    [(key, "tram", tram_lines[key]) for key in tram_lines] +
    [(key, "ubahn", ubahn_lines[key]) for key in ubahn_lines] +
    [(key, "district", districts[key]) for key in districts]
)

# Session-State zur Speicherung des aktuellen Fortschritts
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

# Falls alle Fragen beantwortet wurden, Option zum Neustart anbieten
if st.session_state.current_index >= len(all_items):
    st.write("🎉 Du hast alle Linien und Bezirke gelernt!")
    if st.button("🔄 Wieder von vorne starten"):
        st.session_state.current_index = 0
        st.experimental_rerun()
else:
    # Nächste Frage anzeigen
    current_item, category, answer = all_items[st.session_state.current_index]

    st.write("### ❓ Was gehört zu dieser Nummer oder Linie?")
    st.write(f"**{current_item}**")

    if st.button("💡 Antwort anzeigen"):
        st.write(f"### ✅ {answer}")

    # Weiter zur nächsten Frage
    if st.button("➡️ Nächste Frage"):
        st.session_state.current_index += 1
        st.experimental_rerun()

st.write("📚 Viel Erfolg beim Lernen! 🚋🚇🏙️")
