# File: initials.py
# Description: Printing my intials "MSM" in block letters using python
# Assignment Number: 2

#Name: Menye Senam
#Student ID: 2425402306
#Email: 2425402306@live.gctu.edu.gh
#Grader:Augustus Buckman

#On my honor,Menye Senam, this programming assignment is my own work
#and I have not provided this code to any other student.


def main():
    #A written code in python to print my intials "MSM"
    print()
    print("...MSM")
    print()

    # Large period made of 4 asterisks
    period_row = "****"
    three_dots = "..."

    # Printing the letter "M" by using 12 characters wide and 10 high
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

    #Printing the letter "S" by using 12 characters wide and 10 high
    s0 = ".SSSSSSSS.."
    s1 = "SS......SS."
    s2 = "SS........"
    s3 = ".SSSSSSSS.."
    s4 = "........SS."
    s5 = "........SS."
    s6 = "SS......SS."
    s7 = "SS......SS."
    s8 = ".SSSSSSSS.."
    s9 = ".........."


    # Printing the 10 rows - each row combines the letters using the concatenator "+": ... + M + **** + ... + S + **** + ... + M
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

    # To print a blank line after printing the intials
    print()


if __name__ == "__main__":
    main()