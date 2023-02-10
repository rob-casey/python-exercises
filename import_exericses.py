# Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, 
# and return the amount to tip.

def calculate_tip(bill, tip):
    return bill*tip

# print(calculate_tip(50, .15))

# alternative
# (bill, bill=.15)

def get_letter_grade(my_num_grade):
    if my_num_grade >= 90:
        return 'A'
    elif my_num_grade >= 80:
        return 'B'
    elif my_num_grade >= 70:
        return 'C'
    else:
        return 'F'