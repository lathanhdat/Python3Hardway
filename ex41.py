import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodetherhardway.org/world.txt"
WORD = []
PHRASES = {}

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding = "utf-8"))

def convert(snippet,phrase):
    class_names = [w.capitalize()
    for w in random.sample(WORDS,snippet.count("%%%"))]