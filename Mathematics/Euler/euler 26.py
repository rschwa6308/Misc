##
##
##
##def get_cycle_length(d):
##    if len(str(1.0/d)) == 14:
##        num = str(long(100000000000000000000.0/d)).replace(".","")
##        return guess_seq_len(num)
##    else:
##        return 0
##
##
##
##
##def guess_seq_len(seq):
##    guess = 1
##    max_len = len(seq) / 2
##    for x in range(1, max_len):
##        if seq[0:x] == seq[x:2*x]:
##            return x
##
##    return guess
##
##
##
##best_d = 0
##best_length = 0
##
##for d in range(1,1000):
##    l = get_cycle_length(d)
##    if not l == 0:
##        print l
##    if l > best_length:
##        best_d = d
##        best_length = l
##
##print best_d






##########   answer: 983 (cycle length 982)
##########   https://mathematica.wolframcloud.com/app/objects/8cceea8b-6758-484b-ad55-16abf45b4f35
