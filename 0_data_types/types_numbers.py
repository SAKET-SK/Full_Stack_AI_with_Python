# Integers

boy1_weight = 50
boy2_weight = 60

total_weight = boy1_weight + boy2_weight
print(f"Total weight of boy1 and boy2 is {total_weight} kgs")

boy1_weight = 50
boy2_weight = 60

total_weight = boy1_weight - boy2_weight
print(f"Difference between weight of boy1 and boy2 is {total_weight} kgs")

# Super easy isn't it? You haven't seen anything yet...

no_of_toffes = 7
no_of_students = 3
toffes_per_student = no_of_toffes / no_of_students
print(f"Each student will get {toffes_per_student} toffes")  # 2.333; Division always results in float, BUT

no_of_toffes = 7
no_of_students = 3
toffes_per_student = no_of_toffes // no_of_students
print(f"Each student will get {toffes_per_student} toffes")  # 2; // is floor division, it gives integer result

total_cake_pieces = 10
no_of_dudes = 3   # Assuming we are divding cake among dudes equally
cake_piece_per_dude = total_cake_pieces // no_of_dudes
print(f"Each dude will get {cake_piece_per_dude} pieces of cake")  # 3; // is floor division, it gives integer result
leftover_cake = total_cake_pieces % no_of_dudes
print(f"Leftover cake pieces after equally distributing are {leftover_cake}")  # 1; % is modulus operator, it gives the remainder

base_number = 7
exponent = 4
result = base_number ** exponent
print(f"{base_number} raised to the power {exponent} is {result}")  # 2401; ** is exponentiation operator

Money_earned_by_rich_man = 10_000_000_000_000  # You can use _ in between numbers to make it more readable
print(f"Money earned by rich dude per day is $ {Money_earned_by_rich_man}")

# Boolean

is_rich = True
money_in_account = 1000000
boolAction = money_in_account + is_rich  # True is treated as 1 in arithmetic operations, False is treated as 0. This is known as upcasting
print(f"Money in account after adding boolean value is {boolAction}")

has_credit_card = 0
print(f"Do you have credit card? The person in bank answered {bool(has_credit_card)}")  # bool() function converts 0 to False and any non-zero number to True
has_atm_service = 1
print(f"Do you have ATM service? The person in bank answered {bool(has_atm_service)}")  

has_uniform = True
has_id_card = True
is_allowed_to_exam = has_uniform and has_id_card  # and, or, not are logical operators
print(f"Is the student 1 allowed to sit in exam? The answer is {is_allowed_to_exam}") # AND : both conditions should be True to get True

has_uniform = False
has_id_card = True
is_allowed_to_exam = has_uniform or has_id_card  
print(f"Is the student 2 allowed to sit in exam? The answer is {is_allowed_to_exam}") # OR : any one condition should be True to get True

has_uniform = False
has_id_card = True
is_allowed_to_exam = has_uniform and has_id_card  
print(f"Is the student 3 allowed to sit in exam? The answer is {is_allowed_to_exam}")

# Real Numbers (Floating Point Numbers)

import sys
from fractions import Fraction  # To work with fractions; big numbers ; works well for complex numbers
from decimal import Decimal as D  # To work with decimal numbers; high precision; also typecasting

price_of_apple = 30.5
price_of_orange = 25.7
print(f"Difference between price of apple and orange is {price_of_apple - price_of_orange}")
print(sys.float_info)  # Check the precision of floating point numbers in your system