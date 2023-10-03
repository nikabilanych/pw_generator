
from string import digits,punctuation,ascii_lowercase,ascii_uppercase
import random
import re
gt

def password_generator(LENGTH=10,Upper_Case=True,Punct=True,Digits=True):
    """  
    Generate a random password based on specified criteria.

    Parameters:
    - LENGTH (int): Length of the password (default is 10).
    - Upper_Case (bool): Whether to include uppercase letters (default is True).
    - Punct (bool): Whether to include punctuation characters (default is True).
    - Digits (bool): Whether to include digits (default is True).

    Returns:
    - str: The generated password.

    If LENGTH is set to 4, the function will print a message and return, indicating that it's not secure.
    The generated password by default contains at least:1 upper_case char, 1 dig and 1 punct symbol
    """

    # instead of creating "heavy" list/string of options 
    if LENGTH==4:
        print("Please select a safer option")
        return

    # dictionary where the keys access the already existing variables of string module

    password=""
    #the key to access the variable
    option_index=1
    options={option_index:ascii_lowercase}
    
    if Upper_Case:
        option_index+=1
        options.setdefault(option_index,ascii_uppercase)

    if Punct:
        option_index+=1
        options.setdefault(option_index,punctuation)
    if Digits:
        option_index+=1
        options.setdefault(option_index,digits)

    
    for _ in range(LENGTH):
        password+=random.choice(options.get(random.randint(1,option_index)))

    if requirements_check(password,Upper_Case,Punct,Digits):
        return password
    #if requirements not met call functions calls itself again 
    password=''
    password_generator(LENGTH,Upper_Case,Punct,Digits)


#if true return password else start again

def requirements_check(password,Upper_Case,Punct,Digits):
    """
    Check whether the password meets the specified requirements.

    Parameters:
    - password: generated password from the password_generator funct
    - Upper_Case (bool): Whether to include uppercase letters (default is True).
    - Punct (bool): Whether to include punctuation characters (default is True).
    - Digits (bool): Whether to include digits (default is True).
    
    Returns:
    - bool: Whether the password meets the specified requirements.

    """
    #list of regex patterns to check if criteria is met
    requirements=[]
    if Upper_Case:
        upper_regex=r'.*[A-Z]{1,}.*'
        requirements.append(upper_regex)

    if Digits:
        digit_regex=r'.*[0-9]{1,}.*'
        requirements.append(digit_regex)
    if Punct:
        punct_regex=r".*[\(!\"\#\$\%\&'\(\)\*\+\,\-\./:;<=>\?@\[\]\\^_`\{\|\}~]{1,}.*"
        requirements.append(punct_regex)
        
    for pattern in requirements:
        match=re.search(pattern,password)
        if not match:
            return False
    return True
#print("this is a test")