pl0nd1 = {0: "blockid", 1: "company", 2: "plantname", 3: "plz", 4: "place", 5: "street", 6: "federalstate", 7: "blockname", 8: "initialop", 9: "state", 10: "e1", 11: "e2", 12: "e3", 13: "energysource", 14: "eeg", 15: "chp", 16: "power"}

names_dict = {'MaStR-Nr. der Stromerzeugungseinheit': "blockid",  'Kraftwerksnummer der Bundesnetzagentur': "bnaid", 'Anlagenbetreiber': "company", 'Anzeige-Name der Stromerzeugungseinheit': "plantname", 'PLZ der Einheit': "plz", 'Ort der Einheit': "place", 'Straße der Einheit': "street", 'Hausnummer der Einheit': "streetnum", 'Bundesland der Einheit': "federalstate", 'Datum der erstmaligen Inbetriebnahme der Einheit': "initialop", 'Kraftwerksstatus der Einheit': "state", 'Energieträger': "e1", 'Hauptbrennstoff': "e2", 'Auswertung Energieträger': "energysource", 'Förderberechtigt nach EEG\n(ja/nein)': "eeg", 'Wärmeauskopplung (KWK)\n(ja/nein)': "chp", 'Erneuerbarer Energieträger\n(ja/nein)': "ee", 'Ist die Stromerzeugungseinheit ein Bestandteil eines Grenzkraftwerkes?': "border", 'Bruttoleistung in MW': "grosspower", 'Nettonennleistung (elektrische Wirkleistung) in MW': "power", 'Ist die Stromerzeugungseinheit ein Bestandteil eines Grenzkraftwerkes?: ja \nNettonennleistung der Einspeisung in ein deutsches Netz:': "gerpower", 'Technologie der Stromerzeugung': "tech", 'Volleinspeisung oder Teileinspeisung?': "fullsupply", 'Anschlussnetzbetreiber': "TSO", 'Spannungsebene': "voltagelevel", 'Wenn Energieträger Speicher: Nutzbare Speicherkapazität in Mwh': "storage"}

names_dict_retired = {'MaStR-Nr. der Stromerzeugungseinheit': "blockid",  'Kraftwerksnummer der Bundesnetzagentur': "bnaid", 'Anlagenbetreiber': "company", 'Anzeige-Name der Stromerzeugungseinheit': "plantname", 'PLZ der Einheit': "plz", 'Ort der Einheit': "place", 'Straße der Einheit': "street", 'Hausnummer der Einheit': "streetnum", 'Bundesland der Einheit': "federalstate", 'Datum der erstmaligen Inbetriebnahme der Einheit (Datum/Jahr)': "initialop", 'Datum der endgültigen Stilllegung der Einheit (Datum/Jahr)': "endop", 'Kraftwerksstatus der Einheit': "state", 'Energieträger': "e1", 'Hauptbrennstoff': "e2", 'Auswertung Energieträger': "energysource", 'Förderberechtigt nach EEG\n(ja/nein)': "eeg", 'Wärmeauskopplung (KWK)\n(ja/nein)': "chp", 'Erneuerbarer Energieträger\n(ja/nein)': "ee", 'Ist die Stromerzeugungseinheit ein Bestandteil eines Grenzkraftwerkes?': "border", 'Bruttoleistung in MW': "grosspower", 'Nettonennleistung (elektrische Wirkleistung) in MW': "power", 'Ist die Stromerzeugungseinheit ein Bestandteil eines Grenzkraftwerkes?: ja \nNettonennleistung der Einspeisung in ein deutsches Netz:': "gerpower", 'Technologie der Stromerzeugung': "tech", 'Volleinspeisung oder Teileinspeisung?': "fullsupply", 'Anschlussnetzbetreiber': "TSO", 'Spannungsebene': "voltagelevel", 'Wenn Energieträger Speicher: Nutzbare Speicherkapazität in Mwh': "storage"}

def get_renamed_blocks2(pl0):
    pl0nd2 = {}
    for idx, new, old in list(zip(pl0nd1.keys(), pl0nd1.values(), list(pl0))):
        pl0nd2[old] = new
    plt = pl0.rename(columns=pl0nd2)
    return plt

def get_renamed_blocks(pl0):
    plt = pl0.rename(columns=names_dict)
    return plt

def get_renamed_blocks3(pl0):
    plt = pl0.rename(columns=names_dict_retired)
    return plt
