# Relational Operators 
# equal to operator: ==
# not equal to operator: !=

# 2 * 2 == 2 + 2
first_expression = True # this statement is true, as 2*2=4 and 2+2=4 also. Therefore 4 == 4.

# 3 + 3 != 3 * 3
second_expression = True # this statement is true, as 3+3=6 and 3*3=9. Therefore 6 != 9

# 3 * 3 == '9'
third_expression = False # this statement is false as '9' is a string. 3*3=9, nine is a integer and integers are not equal to a string  
# More Practice
x = 20
y = 20

# Create an if statement that checks if 'x' and 'y' are equal, print the string below if so: 'These numbers are the same'
# Write the first if statement here:
if x == y:
  print('These numbers are the same')

credits = 120

# The nearby college, Calvin Coolidge's Cool College (or 4C, as the locals call it) requires students to earn 120 credits to graduate.
# Write an if statement that checks if the student has enough credits to graduate.  If they do, print the following string: 'You have enough credits to graduate!'
# Write the second if statement here:
if credits >= 120:
  print('You have enough credits to graduate!')
