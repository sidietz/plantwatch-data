def get_price(x):
    if x == "Erdgas":
        return 40
    elif x == "Steinkohle":
        return 120
    elif x == "Braunkohle":
        return 18 # https://green-planet-energy.de/blog/energiewende/kohleausstieg/subventionen-fuer-kohlekonzerne/
    else:
        return 75

def get_factor(x):
    if x == "Erdgas":
        return 1.5
    elif x == "Steinkohle":
        return 2.68
    elif x == "Braunkohle":
        return 3.25
    else:
        return 2.3