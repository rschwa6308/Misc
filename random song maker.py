import winsound
from math import floor
from random import randint

freq = [261.6,293.7,329.6,349.2,392.0,440,493.9,523,587,659,698,784,880,998]
notes = ['C','D','E','F','G','A','B','c','d','e','f','g','a','b']



tones = int(raw_input("Enter number of tones to play: "))
tempo = int(raw_input("Enter BPM: "))


for x in range(tones):
    z = randint(0,len(notes)-1)
    print notes[z]
    derp = 50
    winsound.Beep(int(freq[z])+10,int(derp)+int(floor(((float(60)/float(tempo))*float(1000)))))
