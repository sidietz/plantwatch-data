pl0nd1 = {0: "blockid", 1: "company", 2: "plantname", 3: "plz", 4: "place", 5: "street", 6: "federalstate", 7: "blockname", 8: "initialop", 9: "state", 10: "e1", 11: "e2", 12: "e3", 13: "energysource", 14: "eeg", 15: "chp", 16: "power"}

def get_renamed_blocks(pl0):
    pl0nd2 = {}
    for idx, new, old in list(zip(pl0nd1.keys(), pl0nd1.values(), list(pl0))):
        pl0nd2[old] = new
    plt = pl0.rename(columns=pl0nd2)
    return plt