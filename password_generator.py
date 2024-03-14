from random import *
from string import *
def generate(size):
    letter=ascii_letters+digits+punctuation
    password=''.join(choice(letter) for _ in range(size))
    return password
length=int(input("Enter The Length Of The Password Need to be : "))
password=generate(length)
print(password)
