#random data generator
from random import *

mean = float(raw_input("mean:\n"))
max_dev = float(raw_input("max deviation:\n"))
num = int(raw_input("num of data points to generate:\n"))

for x in range(num):
    print mean + 2*(random()-0.5)*max_dev
