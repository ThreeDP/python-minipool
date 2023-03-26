# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    intern.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dapaulin <dapaulin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/07 13:58:18 by dapaulin          #+#    #+#              #
#    Updated: 2023/02/08 14:05:45 by dapaulin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Intern():
    
    class Coffee():         
        def __str__(self):
            return "This is the worst coffee you ever tasted."
        
    def __init__(self, name = "My name? I'm nobody, an intern, I have no name."):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        return self.Coffee()
    
if __name__ == "__main__":
    intern = Intern()
    mark = Intern("Mark")
    print(intern)
    print(mark)
    print(mark.make_coffee())
    try:
        intern.work()
    except Exception as error:
        print(error)
        
    
        