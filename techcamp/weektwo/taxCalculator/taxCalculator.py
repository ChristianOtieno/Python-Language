class Payroll:
    basicSalary = 0
    overtime = 0
    houseAllowance = 0
    otherBenefits = 0
    grossSalary = 0

    def __init__(self, basic, over, house, other):
        Payroll.basicSalary = basic
        Payroll.overtime = over
        Payroll.houseAllowance = house
        Payroll.otherBenefits = other

    def calculateGrossSalary(self):
        Payroll.grossSalary = Payroll.basicSalary + Payroll.overtime + Payroll.otherBenefits + Payroll.houseAllowance
