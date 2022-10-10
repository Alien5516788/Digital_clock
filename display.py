import digits
from time import strftime, sleep
import os

# number characters

numdict = {"0" : digits.x0, 
           "1" : digits.x1,
           "2" : digits.x2, 
           "3" : digits.x3, 
           "4" : digits.x4, 
           "5" : digits.x5, 
           "6" : digits.x6, 
           "7" : digits.x7, 
           "8" : digits.x8,
           "9" : digits.x9,
           "div" : digits.div}

dx = 25 # distance from left side, 1 = space
dy = 4 # distance form top, 1 = newline
h24  = False # 24 hour format toggle

# starting

os.system("@echo off") 
print("starting...")
sleep(1)

while True:

    os.system("cls")  # clear screen

    datedict = {"hour"   : strftime("%H"),  # hour now
                "minute" : strftime("%M"),  # minute now
                "second" : strftime("%S")}  # second now

    # digits

    # hour
    h1 = numdict[ datedict["hour"][0] ] 
    h2 = numdict[ datedict["hour"][1] ]
    
    if h24 == False:
        if int(datedict["hour"]) >= 12: # convert 24 hours to 12
            h1 = numdict[ "0" ] 
            h2 = numdict[ str(int(datedict["hour"]) -2 )[1] ]

    # minute
    m1 = numdict[ datedict["minute"][0] ]
    m2 = numdict[ datedict["minute"][1] ]

    # second
    s1 = numdict[ datedict["second"][0] ]
    s2 = numdict[ datedict["second"][1] ]
    
    # colon mark
    div = numdict["div"]

    # print time now
    print(datedict["hour"], datedict["minute"], datedict["second"] + "\n"*dy)
    
    # print digits
    for i in range(0, 10):
        ln = " "*dx + f"""{h1.splitlines()[i]} {h2.splitlines()[i]} {div.splitlines()[i]} {m1.splitlines()[i]} {m2.splitlines()[i]} {div.splitlines()[i]} {s1.splitlines()[i]} {s2.splitlines()[i]}"""
        print(ln)

    sleep(0.9)