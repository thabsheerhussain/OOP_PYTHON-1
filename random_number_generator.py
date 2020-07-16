import random 

class number:
    def num(self):
        n=random.randint(0, 100)
        return n


a = input("press y to get a number ")
if(a == 'y'):   
    b = number()
    print("random number is "+str(b.num())+" this")