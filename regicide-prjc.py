import sys
import random
from random import *
input('press enter')
print('input et to exit')
bl = 0
list = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
while True:
    ok = choice(list)
    print(f'score - {bl}')
    print()
    print(ok)
    ol = input()
    if ol == ok:
        print('+1')
        bl += 1
    if ol != ok and ol != "et":
        print('-1')
        bl -= 1
    if ol == "et":


        sys.exit()
