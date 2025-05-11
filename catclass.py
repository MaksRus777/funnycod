

class Cat:

  def __init__(self, pet_name):  # initializator
    self.cat_name = pet_name
    self.paws = 4
    self.ears = 2
    self.eyes = 2
    self.tail = True
    self.wool = True
    self.energy = 100
    self.sleep = False


  def say_mew(self):
    print(f"Your pet {self.cat_name} say 'Mew!'")


  def play(self, action):
    if self.energy >= 20:
            match action:
                case "play with hand":
                    self.energy -= 10
                    return print(f"The cat has been playing with your hand and is a little tired. {self.energy = }")
                case "play with a laser pointer":
                    self.energy -= 20
                    return print(f"The cat has been playing with a laser pointer and is a little tired. {self.energy = }")
                case "night madness":
                    return print(f"The cat's gone into 'night madness' mode. No energy wasted.")
    else:
        return print("The cat is tired, he's going to bed.")
    

cat=Cat('Musia')
cat.say_mew()
cat.play('play with hand')
print(cat.paws)
