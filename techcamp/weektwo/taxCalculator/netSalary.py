from grossSalary import grossSalary
from deductions import deductions
from main import personalRelief


def getNetSalary(grossSalary, deductions, personalRelief):
    netSalary = grossSalary + personalRelief - deductions

    return netSalary
