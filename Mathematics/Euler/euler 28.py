



def sum_layer(n):
    start = (n*2-1)**2+1
    gap = 2*n-1

    #print "start: " + str(start)
    #print "gap: " + str(gap)
    
    s = 0
    s += start + gap
    s += start + gap*2 + 1
    s += start + gap*3 + 2
    s += start + gap*4 + 3

    #print s

    return s

def get_diags(most):
    s = 1
    for layer in range(int((most**0.5-1)/2)):
        #print "layer: " + str(layer+1)
        s += sum_layer(layer+1)

    return s



print get_diags(1001*1001)
