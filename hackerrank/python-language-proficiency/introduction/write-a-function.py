'''
Description
We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:
  The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
      The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years

Task:
Given a year as an input, define a funtion to check is the year is a leap year or not

Input Format:
Read y, the year that needs to be checked.

Constraints:
1900 <= y <= pow(10,5)

Output Format
Output is taken care of by the template. Your function must return a boolean value (True/False)
'''
#!/usr/bin/env python3

def is_leap(year):
    leap = False

    # Write your logic here
    if year % 100 == 0:
        if year % 400 == 0:
            return True
    else:
        return False

    # Not divisible by 100
    if year % 4 == 0:
        return True
    return False

year = int(input())
print(is_leap(year))
