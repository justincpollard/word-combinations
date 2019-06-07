import json

dictionary = {"mobile",
              "samsung",
              "sam",
              "sung", 
              "man",
              "mango",
              "icecream",
              "and", 
              "go",
              "i",
              "love",
              "ice",
              "cream"}

def find_words(mash):
    # Find the possible first words from mash.
    # E.g. in "mango" we'd get ["man", "mango"].
    first_words = []
    for i in range(len(mash)):
        word = mash[0:i+1]
        if word in dictionary:
            first_words.append(word)
    
    # If there are no first word possibilities,
    # just return an empty list.
    if len(first_words) == 0:
        return []
    
    # If there are possible first words, then 
    # add each of them to the return list. Also
    # add the possible combinations of words
    # in the substring of mash after each first
    # word.
    ret_list = []
    for first_word in first_words:
        # If the first_word is the whole mash,
        # just add it to the return list.
        if first_word == mash:
            ret_list.append([first_word])
        else:
            # If we have next_words (i.e. words that come
            # after first_word) then add each of them to
            # the list alongside first_word
            next_words = find_words(mash=mash[len(first_word):])
            if len(next_words) > 0:
                for next_word in next_words:
                    word_list = [first_word]
                    word_list.extend(next_word)
                    ret_list.append(word_list)
    return ret_list

word_combos_1 = find_words("iloveicecreamandmango")
word_combos_2 = find_words("ilovesamsungmobile")

print word_combos_1
print word_combos_2
