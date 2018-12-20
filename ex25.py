def break_words(stuff):
    #This string will display when using help(ex25.break_words)
    """This method is used for breaking sentence to words
        Usage : break_words(sentence)""" 
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_world(words):
    word = words.pop(0)
    print(word)

def print_last_world(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    word = break_words(sentence)
    print_first_world(words)
    print_last_world(words)

def print_first_and_last_sorted(sentence):
    words=sort_sentence(sentence)
    print_first_world(words)
    print_last_world(words)