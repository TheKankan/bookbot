def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    char_count = {}
    for c in text:
        char = c.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(d):
    return d["num"]

def get_sorted_list(text_list):
    result = []
    for char in text_list:
        result.append({"char" : char, "num": text_list[char]})

    result.sort(reverse=True, key=sort_on)
    return result
