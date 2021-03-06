'''
--------------------------------------------------------
                LEAP YEAR + STACK DIAGRAM
--------------------------------------------------------

Construct a function according to the following description,
then draw a stack diagram of an execution with ‘2000’ as input.

-- DESCRIPTION --
We add a Leap Day on February 29, almost every four years.
The leap day is an extra, or intercalary day and we add it to the
shortest month of the year, February. In the Gregorian calendar
three criteria must be taken into account to identify leap years:

- The year can be evenly divided by 4, is a leap year, unless:
  - The year can be evenly divided by 100, it is NOT a leap year, unless:
    - The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are
leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

-- TASK --
You are given the year, and you have to write a function to check
if the year is leap or not.

Input Format:
Read y, the year that needs to be checked.

Constraints:
1900 <= y <= 10**5

Output Format:
Your function must return a boolean value (True/False)

-- STACK DIAGRAM --
You can use the viz mode here:
http://www.pythontutor.com/visualize.html#mode=edit
for better visual understanding and support in creating the stack diagram.

'''


def leap_year_checker(year):
    if year % 4 == 0:
        first = True
    else:
        first = False

    if year % 100 == 0:
        second = False
    else:
        second = True

    if year % 400 == 0:
        third = True
    else:
        third = False

    if first == True and second == True:
        return True
    elif second == False and third == True:
        return True
    return False


leap_years = []

for i in range(1900, 10**5, 1):
    leap_years.append((i, leap_year_checker(i)))

print(leap_years)

