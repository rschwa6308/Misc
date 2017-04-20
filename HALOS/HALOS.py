#HalOS is a siri/cortana style personal assistant.  She takes the string arg 'query' and returns a string response.

#http://collabedit.com/xfrbb

#lib imports
import urllib2
from urllib2 import *
from time import *
from random import *
from math import *
import webbrowser
from webbrowser import *
from text_assets import jokes




#define assets path
assets = os.path.split(os.path.abspath(__file__))[0]
assets = os.path.join(assets,"assets")



#define minimize decimals function (takes float):
def min_dec(num):
    if num - int(num) == 0:
        return int(num)
    return num
    


#creating a list of all acceptable chars for input
ascii = []
asciinum = [str(chr(i)) for i in range(48, 58)]
for i in asciinum:
    ascii.append(i)
asciicap = [str(chr(i)) for i in range(65, 91)]
for i in asciicap:
    ascii.append(i)
asciilow = [str(chr(i)) for i in range(97, 123)]
for i in asciilow:
    ascii.append(i)
asciimath = ["+", "-", "*", "/"]
for i in asciimath:
    ascii.append(i)
ascii.append(" ")
#print ascii



def HALOS(query):
    
    #lowercase all letters in query
    query = query.lower()
    
    #remove punctuation
    chars = [char for char in query if char in ascii]
    query = "".join(chars)
    

    #parse query into word list
    words = query.split(" ")

    #append empty words to words list
    for i in range(10):
        words.append("")
 
    
    #split up math expression into seperate words
    if words[0][1] in asciimath:
        a = words[0][0]
        b = words[0][2]
        exp = words[0][1]
        words.pop(0)
        words.insert(0,b)
        words.insert(0,exp)
        words.insert(0,a)
    
    
    
    #quit command
    if query in ["quit", "exit", "bye", "goodbye"]:
        quit()

    #conversational
    if words[0] in ["hello", "hi", "hey", "sup", "yo"]:
        return ["Hello", "Hi", "Greetings"][randint(0,2)] + ", human" + ["!","",""][randint(0,2)]
    if query in ["how are you", "how are you doing"]:
        return "I'm doing quite well. Thank you for asking"
    if query in ["tell me a joke", "joke"]:
        #jokes = ["What do you feed an invisible cat? Evaporated Milk!", "The time traveler was still hungry after his last bite, so he went back four seconds.", "What do you call an unpredictable, out of control photographer? A loose Canon.", "What do auditioning for an acting role and playing sports have in common? If you break a leg, you get cast.", "Why is six afraid of seven? Because seven \'ate\' nine.", "What did Lil Jon do when the hardware store employee tried to sell him a lightbulb? Turned down 4 Watt.", "Mr. and Mrs. Brown had two sons. One was named Mind Your Own Business & the other was named Trouble. One day the two boys decided to play hide and seek. Trouble hid while Mind Your Own Business counted to one hundred. Mind Your Own Business began looking for his brother behind garbage cans and bushes. Then he started looking in and under cars until a police man approached him and asked, \"What are you doing?\" \"Playing a game,\" the boy replied. \"What is your name?\" the officer questioned. \"Mind Your Own business.\" Furious, the policeman inquired, \"Are you looking for trouble?!\" The boy replied, \"Why, yes, I am!\"", "What do you call crystal clear urine? 1080pee.", "Did you hear about the kidnapping at school? It\'s ok, he woke up.", "How do you make a tissue dance? Put a little boogie in it.", "If it weren’t for C, we’d all be programming in BASI and OBOL.", "There are 10 types of people in this worls: those who understand binary and those who don't.", "An SQL statement walks into a bar and sees two tables. It approaches, and asks \"may I join you?\"","A logician tells a colleague that his wife just had a baby. The colleague asks, \"Is it a boy or a girl?\" The logican responds, \"Yes.\""]
        return jokes[randint(0,len(jokes)-1)]
    
        

    #math related queries
    if words[0].isdigit() and words[2].isdigit():
        #print "math query"
        a = float(words[0])
        b = float(words[2])
        if words[1] in ["plus", "+"]:
            return str(str(min_dec(a)) + " + " + str(min_dec(b)) + " = " + str(min_dec(a+b)))
        elif words[1] in ["minus", "-"]:
            return str(str(min_dec(a)) + " - " + str(min_dec(b)) + " = " + str(min_dec(a-b)))
        elif words[1] in ["times", "multiplied-by", "of", "x", "*"]:
            return str(str(min_dec(a)) + " * " + str(min_dec(b)) + " = " + str(min_dec(a*b)))
        elif words[1] in ["divided-by", "into", "/"]:
            return str(str(min_dec(a)) + " / " + str(min_dec(b)) + " = " + str(min_dec(a/b)))





    #time and date related queries
    #time
    if query in ["what time is it", "time", "what is the time"]:
        local = localtime(time())
        if local.tm_min < 10:
            mins = "0" + str(local.tm_min)
        else:
            mins = str(local.tm_min)
        hours = str(local.tm_hour%12)
        out = hours + ":" + mins
        if local.tm_hour > 12:
            return str("\nIt is currently " + out + " pm.")
        else:
            return str("\nIt is currently " + out + " am.")
            

    #date
    if query in ["what is the date", "what is the day", "what date is it", "what day is it", "date", "day", "what is todays date"]:
        local = localtime(time())
        out = str(["January","February","March","April","May","June","July","August","September","October","November","December"][local.tm_mon - 1] + " " + str(local.tm_mday) + ", " + str(local.tm_year))
        return str("\nIt is " + out + ".")

    
    #ask google
    if words[0] == "google" or (words[0] == "ask" and words[1] == "google"):
        words.pop(0)
        words.pop(0)
        qdata = ""
        for word in words:
            qdata += word + "%20"
        url = 'https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=' + qdata
       #print "opening " + url
        webbrowser.open_new(url)
        return "\nYou have been sent to Google."
    

    #play a game
    if words[0] == "play":
        if words[1] == "tic" or words[1]+words[2]+words[3] == "tictactoe":
            os.startfile(os.path.join(assets,"tic\\tic tac toe.py"))
            return
        if words[1] in ["checkers", "check"]:
            os.startfile(os.path.join(assets,"check\\checkers graphical.py"))
            return ""
    
    
    #default return
    return "I'm sorry, I don't understand."






#test code
print("\n\nI am HalOS, your virtual assistant.\n")
while True:
    print HALOS(str(raw_input("How can I help you?\n")))
    print ""
    print ""
    sleep(0.5)
