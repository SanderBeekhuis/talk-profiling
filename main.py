
from random import random
from math import sqrt
from time import sleep

def main():
    for _ in range(10):
        harder_better_faster_stronger()

def harder_better_faster_stronger():
    work_it_harder()
    for _ in range(100):
        make_it_better()
        do_it_faster()

    makes_us_stronger()

def work_it_harder():
    r = random() 
    q = sqrt(r)
    print(q)

def make_it_better():
    pass

def do_it_faster():
    pass

def makes_us_stronger():
    sleep(.1)


if __name__ == "__main__":
    main()