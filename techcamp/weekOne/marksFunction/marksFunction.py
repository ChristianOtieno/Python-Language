# Define a variable x equal to 1
x = 1
# Start while loop until x != 1
while x == 1:
    maths = input("Enter maths: ")
    english = input("Enter English: ")
    kiswahili = input("Enter Kiswahili: ")
    science = input("Enter Science: ")
    social = input("Enter Social: ")

    try:
        marks = int(maths, english, kiswahili, science, social)

    except:
        print("Please enter a valid marks")


def calculateTotalMarks(maths, english, kiswahili, science, social):
    total = maths + english + kiswahili + science + social
    print("total marks is: ", total)
    return total


def calculateAverageMarks(total):
    average = total/5
    print("Average marks is: ", average)
    return average


def calculateGrade(average):
    if average > 0 and average <= 40:
        print("Grade E")
    elif average > 40 and average <= 51:
        print("Grade C")
    elif average > 50 and average <= 61:
        print("Grade B")
    else:
        print("Grade is A")


x = calculateTotalMarks(maths, english, kiswahili, science, social)
y = calculateAverageMarks(x)
z = calculateGrade(y)
