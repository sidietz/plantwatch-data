import re

pl0nd1 = {0: "blockid", 1: "company", 2: "plantname", 3: "plz", 4: "place", 5: "street", 6: "federalstate", 7: "blockname", 8: "initialop", 9: "state", 10: "e1", 11: "e2", 12: "e3", 13: "energysource", 14: "eeg", 15: "chp", 16: "power"}

names_dict = {'MaStR-Nr. der Stromerzeugungseinheit': "blockid",  'Kraftwerksnummer der Bundesnetzagentur': "bnaid", 'Anlagenbetreiber': "company", 'Anzeige-Name der Stromerzeugungseinheit': "plantname", 'PLZ der Einheit': "plz", 'Ort der Einheit': "place", 'Straße der Einheit': "street", 'Hausnummer der Einheit': "streetnum", 'Bundesland der Einheit': "federalstate", 'Datum der erstmaligen Inbetriebnahme der Einheit': "initialop", 'Jahr der Inbetriebnahme der Einheit': 'initialopYear', 'Kraftwerksstatus der Einheit': "state", 'Energieträger': "e1", 'Hauptbrennstoff': "e2", 'Auswertung Energieträger': "energysource", 'Förderberechtigt nach EEG\n(ja/nein)': "eeg", 'Wärmeauskopplung (KWK)\n(ja/nein)': "chp", 'Erneuerbarer Energieträger\n(ja/nein)': "ee", 'Ist die Stromerzeugungseinheit ein Bestandteil eines Grenzkraftwerkes?': "border", 'Bruttoleistung in MW': "grosspower", 'Nettonennleistung (elektrische Wirkleistung) in MW': "power", 'Ist die Stromerzeugungseinheit ein Bestandteil eines Grenzkraftwerkes?: ja \nNettonennleistung der Einspeisung in ein deutsches Netz:': "gerpower", 'Technologie der Stromerzeugung': "tech", 'Volleinspeisung oder Teileinspeisung?': "fullsupply", 'Anschlussnetzbetreiber': "TSO", 'Spannungsebene': "voltagelevel", 'Wenn Energieträger Speicher: Nutzbare Speicherkapazität in Mwh': "storage"}

names_dict_retired = {'MaStR-Nr. der Stromerzeugungseinheit': "blockid",  'Kraftwerksnummer der Bundesnetzagentur': "bnaid", 'Anlagenbetreiber': "company", 'Anzeige-Name der Stromerzeugungseinheit': "plantname", 'PLZ der Einheit': "plz", 'Ort der Einheit': "place", 'Straße der Einheit': "street", 'Hausnummer der Einheit': "streetnum", 'Bundesland der Einheit': "federalstate", 'Datum der erstmaligen Inbetriebnahme der Einheit (Datum/Jahr)': "initialop", 'Datum der endgültigen Stilllegung der Einheit (Datum/Jahr)': "endop", 'Kraftwerksstatus der Einheit': "state", 'Energieträger': "e1", 'Hauptbrennstoff': "e2", 'Auswertung Energieträger': "energysource", 'Förderberechtigt nach EEG\n(ja/nein)': "eeg", 'Wärmeauskopplung (KWK)\n(ja/nein)': "chp", 'Erneuerbarer Energieträger\n(ja/nein)': "ee", 'Ist die Stromerzeugungseinheit ein Bestandteil eines Grenzkraftwerkes?': "border", 'Bruttoleistung in MW': "grosspower", 'Nettonennleistung (elektrische Wirkleistung) in MW': "power", 'Ist die Stromerzeugungseinheit ein Bestandteil eines Grenzkraftwerkes?: ja \nNettonennleistung der Einspeisung in ein deutsches Netz:': "gerpower", 'Technologie der Stromerzeugung': "tech", 'Volleinspeisung oder Teileinspeisung?': "fullsupply", 'Anschlussnetzbetreiber': "TSO", 'Spannungsebene': "voltagelevel", 'Wenn Energieträger Speicher: Nutzbare Speicherkapazität in Mwh': "storage"}

names_dict4 = {'Datensatztyp*': 'datatype', 'EinheitMastrNummer': "blockid", 'Anlagenbetreiber': "company", 'Anzeigename': "plantname", 'Postleitzahl': "plz", 'Ort': "place", 'Strasse': "street", 'Hausnummer': "streetnum", 'Bundesland': "federalstate", 'Land': 'nation', 'Jahr_Inbetriebnahme': 'initialopYear', 'Jahr_Stilllegung**': 'endop', 'Kraftwerksstatus': "state", 'Energietraeger': "energysource", 'Hauptbrennstoff': "e2", 'Waermeauskopplung_KWK': "chp", 'Erneuerbarer_Energietraeger': "eeg", 'Bruttoleistung_MW': "grosspower", 'Nettonennleistung_MW': "power", 'Technologie_Stromerzeugung': "tech", 'Volleinspeisung_Teileinspeisung': "fullsupply", 'Spannungsebene': "voltagelevel", 'Anschlussnetzbetreiber': "TSO", 'Bestandteil_Grenzkraftwerk': 'border', 'Grenzkraftwerk_Nettonennleistung_MW': "gerpower"}


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

def get_renamed_blocks4(pl0):
    plt = pl0.rename(columns=names_dict4)
    return plt

def match_inspire(name):
    if re.match(r"DE.EEA\/[0-9]+\.FACILITY", name):
        return "DE.EEA" + re.search("[0-9]+", name)[0]
        #None
    elif re.match(r"https:\/\/registry.gdi-de.org\/id\/de.bb.inspire.pf.eureg\/[0-9]+", name):
        return "BB" + re.search("[0-9]+", name)[0]
        #return None
    elif re.match(r"https:\/\/registry.gdi-de.org\/id\/de.sh\/[0-9]+", name):
        return "SH" + re.search("[0-9]+", name)[0]
        #return None
    elif re.match(r"https:\/\/registry.gdi-de.org\/id\/de.bw.lubw.inspire.pf\/[A-Za-z]*-[0-9]+", name):
        return "BW" + re.search("[A-Za-z]*([0-9]*-)*[0-9]+$", name)[0]
        #return None
    elif re.match(r"https:\/\/registry.gdi-de.org\/id\/de.by.inspire.pf.ied\/S[0-9]+", name):
        return "BY" + re.search("S[0-9]+", name)[0]
        #return None
    elif re.match(r"https:\/\/registry.gdi-de.org\/id\/de\.hb\/[0-9]+", name):
        return "HB" + re.search("[0-9]+$", name)[0]
        # return None
    elif re.match(r"https:\/\/registry.gdi-de.org\/id\/de.hb\/de.hb.pf.bube-eureg.([0-9]*\-*\/*)*[0-9]*", name):
        return "HB" + re.search("([0-9]*-*/*)*[0-9]+", name)[0]
        #return None
    elif re.match(r"https:\/\/registry.gdi-de.org\/id\/de.he.0945.de7.pf.eu_industrie\/[0-9]*", name):
        return "HE" + re.search("[0-9]*$", name)[0]
        #return None
    elif re.match(r"https:\/\/registry.gdi-de.org\/id\/de.hh\/pf.bube-eureg_\/[0-9]+", name):
        return "HH" + re.search("[0-9]*$", name)[0]
        #return None
    elif re.match(r"https:\/\/registry.gdi-de.org\/id\/de.mv.land.inspire.pf.bube\/[0-9]+", name):
        return "MV" + re.search("[0-9]*$", name)[0]
        #return None
    elif re.match(r"https:\/\/registry.gdi-de.org\/id\/de.ni.mu\/[0-9]+", name):
        return "NI" + re.search("[0-9]*$", name)[0]
        #return None
    elif re.match(r"https://registry.gdi-de.org/id/de.nw.inspire.pf.bube-eureg/arb-([0-9]*-)[0-9]+", name):
        return "NW" + re.search("([0-9]*-)[0-9]+$", name)[0]
        #return None
    elif re.match(r"https://registry.gdi-de.org/id/de.rp.inspire.pf.bube-eureg\/[0-9]+", name):
        return "RP" + re.search("[0-9]*$", name)[0]
        #return None
    elif re.match(r"https://registry.gdi-de.org/id/de.sl.inspire.pf\/[0-9]+-G", name):
        return "SL" + re.search("[0-9]*-G$", name)[0]
        #return None
    elif re.match(r"https://registry.gdi-de.org/id/de.sn.sax4inspire.pf\/[0-9]+", name):
        return "SN" + re.search("[0-9]*$", name)[0]
        #return None
    elif re.match(r"https://registry.gdi-de.org/id/de.st.lau.pf.anlagen-ied-euregistry\/[0-9]+", name):
        return "ST" + re.search("[0-9]*$", name)[0]
        #return None
    elif re.match(r"https://registry.gdi-de.org/id/de.th/([a-z]*[0-9]*-*)*([a-z]*[0-9]*)/[0-9]+", name):
        return "TH" + re.search("[0-9]+$", name)[0]
        # return None
    elif re.match(r"https://registry.gdi-de.org/id/de.be.pf.lisa\/[0-9]+", name):
        return "BE" + re.search("[0-9]*$", name)[0]
        # return "MLT" + re.search("[0-9]+", name)[0]
        #return None
    else:
        return name
