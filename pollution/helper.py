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
