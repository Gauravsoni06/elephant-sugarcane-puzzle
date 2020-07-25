import math
def eat_no(items):
    rd = items / 1000
    eat = 2 * rd - 1
    return eat
    
def elephant(km,items):
    if items>1000:
        extra=items%1000
        if extra>0:
            eat = eat_no(items)
            while(extra>0):
                items = items - eat
                km = km - 1
                extra=extra-eat
        eat=eat_no(items)
        while(items>=1000):
            k=math.ceil(eat)
            for i in range(1000,0,-k):
                items=items-eat
                km=km-1
            eat=eat_no(items)
    eat = eat_no(items)
    for i in range(km,0,-1):
        km=km-1
        items=items-eat
    print(items)
items=int(input("enter no of sugarcanes"))
km=int(input("enter total distance"))
elephant(km,items)
