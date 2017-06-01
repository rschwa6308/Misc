##
##
##ways = 0
##
##
##for twoPs in range(0,1+1):
##    for onePs in range(0,2+1):
##        print "onePs: " + str(onePs)
##        for fifties in range(0,4+1):
##            for twenties in range(0,10+1):
##                print "twenties: " + str(twenties)
##                for tens in range(0,20+1):
##                    for fives in range(0,40+1):
##                        for twos in range(0,100+1):
##                            for ones in range(0,200+1):
##                                s = twoPs*200 + onePs*100 + fifties*50 + twenties*20 + tens*10 + fives*5 + twos*2 + ones*1
##                                if s == 200:
##                                    ways += 1
##
##print ways
##
##






target = 200

coin_sizes = [1,2,5,10,20,50,100,200]

ways = [0 for i in range(target+1)]
ways[0] = 1

for i in range(len(coin_sizes)):
    for j in range(coin_sizes[i],target+1):
        ways[j] += ways[j - coin_sizes[i]]























