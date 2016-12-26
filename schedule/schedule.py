# File: schedule.py
# Author: Edward Ly
# Last Modified: 25 December 2016
# Outputs any schedule conflicts found by filling instructors' schedules
# (found in the 'instructor_availability.csv' file) with students' requested
# appointments (found in the 'input.csv' file).
#
# Assumptions:
# 1. input files must be named exactly as above
#    (can be changed later with command line arguments)
# 2. all times are specified in the same local time zone (in this case, EST)
# 3. all dates and times are valid and in a format that allows them
#    to be compared as strings
#
# Algorithm:
# 1. open the 'instructor_availability.csv' file
#    copy list of instructors into instructors array
# 2. open and read the 'input.csv' file
# 3. for each row/schedule request:
#    a. search for instructor and lesson type in instructors array
#       if no matching instructor found
#          add conflict reason: instructor not found
#    b. compare requested date/time range with instructor's date/time range
#       if requested date/time falls outside instructor's range,
#          add conflict reason: instructor not available
#       if private lesson and duration is not a whole number of blocks long
#          add conflict reason: invalid lesson duration
#       if group lesson and duration is not one block long
#          add conflict reason: invalid lesson duration
#    c. search list of previously scheduled lessons
#       if group lesson
#          if instructor and date/time slot match a previous group lesson request
#             increment capacity counter
#             if capacity reached
#                add conflict reason: instructor not available
#       if instructors match and date/time slot overlaps a previous request
#          add conflict reason: instructor not available
#       if students match and requested date/time overlaps a previous request
#          add conflict reason: student not available
#    d. if there are any conflict reasons, print conflict to terminal
#    e. if there are no conflicts, add lesson to lessons array
#
# Data Structures:
# array: list of instructors
# array: list of valid lessons
# set: list of reasons
#

import csv

if __name__ == "__main__":
    with open('instructor_availability.csv', 'rb') as inst_csv:
        inst_reader = csv.reader(inst_csv)
        for row in inst_reader:
            print ', '.join(row)

    with open('input.csv', 'rb') as input_csv:
        input_reader = csv.reader(input_csv)
        for row in input_reader:
            print ', '.join(row)
