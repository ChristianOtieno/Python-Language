x = 1
while x == 1:
    try:
        basicSalary = int(input("Enter basic salary: "))
        otherBenefits = int(input("Enter total of other benefits: "))
        houseAllowance = int(input("Enter house allowance: "))
        overtime = int(input("Enter overtime: "))
        personalRelief = int(input("Enter personal relief: "))
        break
    except:
        print("That's not a valid input try again.")
