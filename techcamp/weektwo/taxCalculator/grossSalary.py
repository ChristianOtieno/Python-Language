from main import basicSalary, otherBenefits, houseAllowance, overtime


def getGrossSalary(basicSalary, otherBenefits, houseAllowance, overtime):
    grossSalary = basicSalary + otherBenefits + houseAllowance + overtime
    return grossSalary

print("Your gross salary is:", getGrossSalary(basicSalary, otherBenefits, houseAllowance, overtime))
