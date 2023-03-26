import random
from beverages import *

class CoffeeMachine():
    
    count = 0
    
    def __init__(self):
        pass
    
    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90
        
        def description(self):
            return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    
    def repair(self):
        self.count = 0
    
    def serve(self, order):
        if self.count < 10:
            drink = random.choice([order(), self.EmptyCup()])
            self.count += 1
        else:
            raise self.BrokenMachineException()
        return drink

if __name__ == "__main__":
    other = CoffeeMachine()
    i = 0
    for i in range(22):
        try:
            print(other.serve(random.choice([Coffee, Cappuccino, HotBeverage, Tea, Chocolate])))
        except Exception as e:
            print(e)
            other.repair()