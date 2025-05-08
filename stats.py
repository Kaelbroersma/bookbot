def get_word_count(text):
    wordcount = text.split()
    return len(wordcount)

def get_char_count(text):
    chars = {}
    for word in text:
        lowercase = word.lower()
        if lowercase in chars:
            chars[lowercase] += 1
        else:
            chars[lowercase] = 1
    return chars

def sort_on(d):
    return d["num"]

def neat_char_dict(charcountdict):
    neatlist = []
    for char in charcountdict:
        neatlist.append({"char": char, "num": charcountdict[char]})
    neatlist.sort(reverse=True, key=sort_on)
    return neatlist
