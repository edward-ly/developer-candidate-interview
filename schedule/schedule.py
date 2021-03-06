# File: schedule.py
# Author: Edward Ly
# Last Modified: 26 December 2016
# Outputs any schedule conflicts found by filling instructors' schedules
# (found in the 'instructor_availability.csv' file) with students' requested
# lessons (found in the 'input.csv' file).
#
# Assumptions:
# 1. input files must be named exactly as above
#    (can be changed later with command line arguments)
# 2. all times are specified in the same local time zone (in this case, EST)
# 3. all dates and times are valid and in a format that allows them
#    to be compared as strings
# 4. there are no restrictions on when a lesson can start or end
#    (e.g. a 1-hour lesson can start at 10:12 AM)
# 5. some names are not case sensitive (the title() method normalizes case
#    before names are compared)
#
# Algorithm:
# 1. open the 'instructor_availability.csv' file
#    copy list of instructors into instructors array
# 2. open and read the 'input.csv' file
#    copy list of requests into requests array
# 3. for each row/lesson request:
#    a. search for instructor and lesson type in instructors array
#       if no matching instructor found
#          add conflict reason: instructor not found
#       else
#          compare requested date/time range with instructor's date/time range
#          if requested date/time falls outside instructor's range,
#             add conflict reason: instructor not available
#          if private lesson and duration is not a whole number of blocks long
#             add conflict reason: invalid lesson duration
#          if group lesson and duration is not one block long
#             add conflict reason: invalid lesson duration
#    c. search list of previously scheduled lessons
#       if group lesson
#          if instructor and date/time slot match a previous group lesson request
#             increment capacity counter
#             if capacity reached
#                add conflict reason: instructor not available
#          else if requested date/time overlaps previous date/time
#             if instructors match
#                add conflict reason: instructor not available
#             if students match
#                add conflict reason: student not available
#       if private lesson and requested date/time overlaps previous date/time
#          if instructors match
#             add conflict reason: instructor not available
#          if students match
#             add conflict reason: student not available
#    d. if there are any conflict reasons, print conflict to terminal
#       else (if there are no conflicts), add lesson to lessons array
#
# Data Structures:
# csv module: read csv files
# array: list of instructors
# array: list of all schedule requests
# array: list of accepted lessons
# set: list of reasons (sets have no duplicate elements)
#

import csv

def print_conflict(id, reasons):
    print ""
    print "Request ID: " + id
    print "Reason for Conflict: " + ", ".join(reasons)
    print ""

def has_overlap(lesson, row):
    return ( ( lesson[3] >= row[3] and lesson[3] <= row[5] ) or \
             ( lesson[5] >= row[3] and lesson[5] <= row[5] ) ) and \
           ( ( lesson[4] >= row[4] and lesson[4] <  row[6] ) or \
             ( lesson[6] >  row[4] and lesson[6] <= row[6] ) )

def same_lesson(lesson, row):
    # requested group lesson duration is within previously scheduled lesson
    return lesson[3] <= row[3] and \
           lesson[4] <= row[4] and \
           lesson[5] >= row[5] and \
           lesson[6] >= row[6] and \
           lesson[7].title() == row[7].title()

def resolve_conflicts(lesson, row, reasons):
    if has_overlap(lesson, row):
        if row[7].title() == lesson[7].title():
            reasons.add("instructor not available")
        if row[1] == lesson[1]:
            reasons.add("student not available")

if __name__ == "__main__":
    instructors = []
    lessons = []
    requests = []

    with open('instructor_availability.csv', 'rb') as inst_csv:
        inst_reader = csv.reader(inst_csv)
        for row in inst_reader:
            instructors.append(row)

    with open('input.csv', 'rb') as input_csv:
        input_reader = csv.reader(input_csv)
        for row in input_reader:
            requests.append(row)

    for row in requests[1:]: # ignore first row (header)
        reasons = set()

        # find row that matches instructor's name and lesson type
        i = 1 # ignore first row (header)
        while i < len(instructors) and \
              ( row[7].title() != instructors[i][0] or \
                row[2]         != instructors[i][1] ):
            i += 1

        if i < len(instructors):
            # if dates or times are not in range
            if ( row[3] < instructors[i][3] or row[5] > instructors[i][4] or \
                 row[4] < instructors[i][5] or row[6] > instructors[i][6] ):
                reasons.add("instructor not available")

            # calculate lesson duration in minutes
            duration = ( int( row[6][0:2] ) - int( row[4][0:2] ) ) * 60 + \
                         int( row[6][3:5] ) - int( row[4][3:5] )

            # duration column can be modified to list just number of minutes,
            # hard-coded strings are a temporary solution
            expected_duration = 60 # default value
            if instructors[i][7] == "1 hour":
                expected_duration = 60
            elif instructors[i][7] == "1/2 hour":
                expected_duration = 30
            elif instructors[i][7] == "45 minutes":
                expected_duration = 45

            if ( ( row[2] == "Private Lesson" ) and ( duration % expected_duration != 0 ) ) or \
               ( ( row[2] == "Group Lesson" ) and ( duration != expected_duration ) ):
                reasons.add("invalid lesson duration")
        else:
            reasons.add("instructor not found")

        # search through previous lessons
        if row[2] == "Group Lesson":
            # determine current capacity of group lesson
            capacity = 0

            for lesson in lessons:
                if same_lesson(lesson, row):
                    if row[1] == lesson[1]:
                        # student already scheduled lesson
                        reasons.add("student not available")
                    else:
                        capacity += 1

                # not the same lesson, but still check for date/time conflicts
                else:
                    resolve_conflicts(lesson, row, reasons)

            if i < len(instructors) and capacity >= int(instructors[i][2]):
                reasons.add("instructor not available")
        elif row[2] == "Private Lesson":
            # just check previous lessons for conflicts
            for lesson in lessons:
                resolve_conflicts(lesson, row, reasons)

        if len(reasons) > 0:
            print_conflict(row[0], reasons)
        else:
            lessons.append(row)
