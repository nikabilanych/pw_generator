
       
from string import digits,punctuation,ascii_lowercase,ascii_uppercase
import random


def password_generator(LENGTH=10,Upper_Case=True,Punct=True,Digits=True):
    # list of options
    if LENGTH==4:
        print("Please select a safer option")
        return

    # default - > password will be generated containing at least one upper char, one punct, one dig
    password=""
    #uprav
    n=1
    options={n:ascii_lowercase}
    
    if Upper_Case:
        options.setdefault(n+1,ascii_uppercase)
        n=n+1
    if Punct:
        options.setdefault(n+1,punctuation)
        n=n+1
    if Digits:
        options.setdefault(n+1,digits)
        n+=1
    #TODO:create regex for checking whether password includes all the requirements
        
    for _ in range(LENGTH):
        
        password+=random.choice(options.get(random.randint(1,n)))
    return password


    
   
