import os
import plotly
from plotly.graph_objs import Bar, Layout




count = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
    "'": 0
}




#load words list
containing = os.path.split(os.path.abspath(__file__))[0]

words_text = open(os.path.join(containing, "wordsEn.txt"))
words_list = words_text.readlines()


for word in words_list:
    for char in word.strip():
        count[char] += 1
        #print char


print count








#plotly stuff

plotly.offline.plot({
    "data": [
        Bar(x=[key for key in count], y=[count[key] for key in count])
    ],
    "layout": Layout(title = "charactar counts")
    
})



