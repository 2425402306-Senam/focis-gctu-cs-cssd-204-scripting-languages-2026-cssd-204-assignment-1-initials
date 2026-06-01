# File: initials.py
# Description: Print out my initials M S M as large stylized block letters.
# Assignment Number: 1
#
# Name: Augustus Buckman
# STUDENT ID:  mds98123
# Email: abuckman@gctu.edu.gh
# Grader: Augustus
#
# On my honor, Augustus Buckman, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():
    # Print the small initials line with three periods and "MSM"
    print()
    print("...MSM")
    print()
    
    # Large period made of 4 asterisks
    period_row = "****"
    three_dots = "..."
    
    # Letter 'M' - 12 chars wide, 10 chars high (stylish block M)
    m0 = "MM......MM."
    m1 = "MMM....MMM."
    m2 = "MMMM..MMMM."
    m3 = "MM.MM.MM.MM"
    m4 = "MM..MM..MM."
    m5 = "MM......MM."
    m6 = "MM......MM."
    m7 = "MM......MM."
    m8 = "MM......MM."
    m9 = "MM......MM."
    
    # Letter 'S' - 12 chars wide, 10 chars high (stylish block S)
    s0 = ".SSSSSSSS.."
    s1 = "SS.....SS."
    s2 = "SS........"
    s3 = ".SSSSSSSS.."
    s4 = "........SS."
    s5 = "........SS."
    s6 = "SS......SS."
    s7 = "SS......SS."
    s8 = "SS......SS."
    s9 = ".SSSSSSSS.."
    
    # Print all 10 rows - each row combines: ... + M + **** + ... + S + **** + ... + M
    # Row 0
    line0 = three_dots + m0 + period_row + three_dots + s0 + period_row + three_dots + m0
    print(line0)
    # Row 1
    line1 = three_dots + m1 + period_row + three_dots + s1 + period_row + three_dots + m1
    print(line1)
    # Row 2
    line2 = three_dots + m2 + period_row + three_dots + s2 + period_row + three_dots + m2
    print(line2)
    # Row 3
    line3 = three_dots + m3 + period_row + three_dots + s3 + period_row + three_dots + m3
    print(line3)
    # Row 4
    line4 = three_dots + m4 + period_row + three_dots + s4 + period_row + three_dots + m4
    print(line4)
    # Row 5
    line5 = three_dots + m5 + period_row + three_dots + s5 + period_row + three_dots + m5
    print(line5)
    # Row 6
    line6 = three_dots + m6 + period_row + three_dots + s6 + period_row + three_dots + m6
    print(line6)
    # Row 7
    line7 = three_dots + m7 + period_row + three_dots + s7 + period_row + three_dots + m7
    print(line7)
    # Row 8
    line8 = three_dots + m8 + period_row + three_dots + s8 + period_row + three_dots + m8
    print(line8)
    # Row 9
    line9 = three_dots + m9 + period_row + three_dots + s9 + period_row + three_dots + m9
    print(line9)
    
    # Print a blank line after the large initials
    print()


if __name__ == "__main__":
    main()