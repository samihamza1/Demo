import random
class Dice :
    def roll(self) :
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

diec1=Dice()
print(diec1.roll())
members=['sami', 'mosh','ali' ,'adam' ,'sam']
print(random.choice(members))


#for i in range(10):
#   print(random.random()*100)
