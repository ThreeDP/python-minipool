# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dapaulin <dapaulin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/07 14:44:04 by dapaulin          #+#    #+#              #
#    Updated: 2023/02/08 11:17:15 by dapaulin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class HotBeverage():

    name = "hot beverage"
    price = 0.30
    
    def __init__(self):
        pass
        
    def __str__(self):
        return "name : {0}\nprice : {1:.2f}\ndescription : {2}\n".format(self.name, self.price, self.description())
        
    def description(self):
        return ("Just some hot water in a cup.")

class Coffee(HotBeverage):
    
    def __init__(self):
        self.name = "coffee"
        self.price = 0.5
        
    def description(self):
        return "A coffee, to stay awake"
    
class Tea(HotBeverage):
    
    def __init__(self):
        self.name = "tea"
    
class Chocolate(HotBeverage):
    def __init__(self):
        self.name = "chocolate"
        self.price = 0.50
    
    def description(self):
        return "Chocolate, sweet chocolate..."
    
class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = "cappuccino"
        self.price = 0.45
    
    def description(self):
        return "Un po' di Italia nella sua tazza!"

if __name__ == "__main__":   
    print(HotBeverage())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())