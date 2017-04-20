import winsound
from random import randint
from math import floor
from time import sleep



song_of_storms = "D F d R D F d R e f e f e c A R A D D F A A D F G E R D F d R D F d R e f e f e c A R A D D F A A D F G D"

mary_had_a_little_lamb = "B A G A B B B A A A B d d B A G A B B B B A A B A G"

crazy_train = "E E R R G G R R D D R R R R R R E E R C C R R D D R R R R R R E E R G G R R D D R R R R R R E E C C D D E E B E c E B E A G F# G A G F# D E E B E c E B E A G F# G A G F# D E E B E c E B E A G F# G A G F# D"

happy_together = "B E F# G F# G R F# G R B A G F# E F# R E R E F# E F# A G F#"

intervals = "C D C E C F C G C A C B C c C d C e C f C g C a C b"



notes = raw_input("Enter notes seperated by spaces \nCAPITAL => below middle C \nlowercase => above or at middle C \nEnter 'R' for rest \n \n")
#manually enter song
notes = crazy_train
notes = notes.split(" ")

print ""
tempo = int(raw_input("Enter BPM: "))
print notes


satanFactor = 0


freq = []

for x in range(0,len(notes)):
    rest = False
    if notes[x] == "C":
        freq.append(262)
    elif notes[x] == "D":
        freq.append(294)
    elif notes[x] == "E":
        freq.append(330)
    elif notes[x] == "F":
        freq.append(349)
    elif notes[x] == "F#":
        freq.append(370)
    elif notes[x] == "G":
        freq.append(392)
    elif notes[x] == "A":
        freq.append(440)
    elif notes[x] == "B":
        freq.append(494)
    elif notes[x] == "c":
        freq.append(523)
    elif notes[x] == "d":
        freq.append(587)
    elif notes[x] == "e":
        freq.append(659)
    elif notes[x] == "f":
        freq.append(698)
    elif notes[x] == "g":
        freq.append(784)
    elif notes[x] == "a":
        freq.append(880)
    elif notes[x] == "b":
        freq.append(988)
    elif notes[x] == "R":
        sleep((floor(1000*(float(60)/float(tempo)))/1000))
        rest = True

    if not(rest):
        winsound.Beep(freq[len(freq)-1]+randint(-satanFactor,satanFactor),int(floor(((float(60)/float(tempo))*float(1000)))))
