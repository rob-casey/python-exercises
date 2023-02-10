# Define a function named is_two. 

# It should accept one input and return True if the passed input
# is either the number or the string 2, False otherwise.


def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False


# print(is_two(1))

# alternative options
# can use assert function
# assert is_two(2) == True
# if type(num) == str
# if type(num) == int
# return num == 2 or num == '2'; can render inside return statement


# Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.


def is_vowel(x):
    
    if x.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


# print(is_vowel('a'))
# print(is_vowel('A'))
# print(is_vowel('b'))

# alternative options
# return my_let.lower() in 'aeiou'
# if type(my_let) == str:
#    if len(my_let) == 1:
#.      my_let.lower() in list('aeiou')
# else: return false



# Define a function named is_consonant. 
# It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.


def is_consonant(x):
    
    if is_vowel(x):
        return False
    else:
        return True

# print(is_consonant('a'))
# print(is_consonant('b'))
# print(is_consonant('e'))

# alternative options
# isalpha() - in alphabet


def get_letter_grade(my_num_grade):
    if my_num_grade >= 90:
        return 'A'
    elif my_num_grade >= 80:
        return 'B'
    elif my_num_grade >= 70:
        return 'C'
    else:
        return 'F'