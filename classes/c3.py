import random

class mylist(list):

   def shuffle(self):
    random.shuffle(self)

   def get_random(self):
    return random.choice(self)

#object

a = mylist([12, 121, 3, 1, 2, 4, 5, 6, 4])
a.sort()
print(a)
a.shuffle()
print(a)
print("random item from list = ", a.get_random())