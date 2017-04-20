import winsound


#for i in range(400,20000):
    #winsound.Beep(i,500)


for x in range(1,20):
    print str(x*1000) + " hertz"
    winsound.Beep(1000*x,1000)
