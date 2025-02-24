import streamlit as st

# Titel der Web-App
st.title("🚋 Wiener Linien & Bezirke Übersicht")

st.write("Wähle aus, welche Informationen du anzeigen möchtest:")

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

# Auswahl-Optionen für die Anzeige
option = st.selectbox("Wähle eine Kategorie:", ["Straßenbahnlinien", "U-Bahn-Linien", "Bezirke"])

# Anzeige der entsprechenden Liste
if option == "Straßenbahnlinien":
    st.header("🚋 Straßenbahnlinien in Wien")
    for line, stations in tram_lines.items():
        st.write(f"**Linie {line}:** {stations}")

elif option == "U-Bahn-Linien":
    st.header("🚇 U-Bahn-Linien in Wien")
    for line, stations in ubahn_lines.items():
        st.write(f"**{line}:** {stations}")

elif option == "Bezirke":
    st.header("🏙️ Bezirke in Wien")
    for num, name in districts.items():
        st.write(f"**Bezirk {num}:** {name}")

st.write("📚 Viel Erfolg beim Lernen! 🚋🚇🏙️")
