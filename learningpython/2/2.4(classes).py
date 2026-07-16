#Class: A blueprint of what an object should look like and do
class Microwave:
    def __init__(self, brand: str, power_rating: str):
        pass
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on : bool =False
    def turn_on(self):
        pass
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned on')
    def turn_off(self):
        pass
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave ({self.brand}) is now turned off')
        else:
            print(f'Microwave ({self.brand}) is already turned off')
    def run(self, seconds: int):
        pass
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds')
        else:
            print('Turn on your microwave first')
    def __add__(self, other):#dunder method
        pass
        return(f'{self.brand} + {other.brand}')
    def __mul__(self, other):#smeg*bosch
        pass#put anything here
    def __str__(self):#returns smth readible
        pass
        return f'{self.brand} (Rating: {self.power_rating})'
    def __repr__(self):
        pass#representation if string cannot be found


smeg: Microwave = Microwave('smeg','B')# makes smeg a type microwave, "self" turns to smeg
#smeg = Microwave('Smeg','B')#parantheses creates a unique microwave

#Methods
smeg.turn_on()
smeg.run(30)
smeg.turn_off()


bosch: Microwave = Microwave('bosch','A')
bosch.turn_on()
bosch.run(30)
bosch.turn_off()

#Dunder methods
#print(smeg+bosch) brings error
print(smeg+bosch)