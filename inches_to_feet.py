# FILE NAME - inches_to_feet.py

# NAME: Bailey Orlick
# DATE: 2/15/2025
# BRIEF DESCRIPTION:  This will output the conversion, Inches to Feet and leftover Inches.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience





# BEWARE! You'll need to cast not only the input from the user
# but also maybe the number of feet

########## ENTER YER CODE BELOW THIS LINE ##########
    
    
inch = int(input('Enter the number of inches: '))
    
feet = inch // 12    
leftover_inch = inch % 12
    
print(f'{inch} inches is {feet} feet, and {leftover_inch} inches')
    
    
########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the number of inches: 14

14 inches is 1 feet, and 2 inches


'''



'''

Enter the number of inches: 100

100 inches is 8 feet, and 4 inches

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does it mean to "cast" input from the user?


Casting is to convert a value from one data type to another.


'''
