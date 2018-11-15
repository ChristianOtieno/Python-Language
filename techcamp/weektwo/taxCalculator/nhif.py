from grossSalary import grossSalary


nhifContribution = 0


def getNHIF(grossSalary):
    if grossSalary > 0 and grossSalary < 5999:
        nhifContribution == 150
    elif grossSalary > 5999 and grossSalary < 8000:
        nhifContribution == 300
    elif grossSalary > 7999 and grossSalary < 12000:
        nhifContribution == 400
    elif grossSalary > 11999 and grossSalary < 15000:
        nhifContribution == 500
    elif grossSalary > 14999 and grossSalary < 20000:
        nhifContribution == 600
    elif grossSalary > 19999 and grossSalary < 25000:
        nhifContribution == 750
    elif grossSalary > 24999 and grossSalary < 30000:
        nhifContribution ==850
    elif grossSalary > 29999 and grossSalary < 35000:
        nhifContribution == 900
    elif grossSalary > 34999 and grossSalary < 40000:
        nhifContribution == 950
    elif grossSalary > 39999 and grossSalary < 45000:
        nhifContribution == 1000
    elif grossSalary > 44999 and grossSalary < 50000:
        nhifContribution == 1100
    elif grossSalary > 49999 and grossSalary < 60000:
        nhifContribution == 1100
    elif grossSalary > 59999 and grossSalary < 70000:
        nhifContribution == 1200
    elif grossSalary > 69999 and grossSalary < 80000:
        nhifContribution == 1400
    elif grossSalary > 79999 and grossSalary < 90000:
        nhifContribution == 1500
    elif grossSalary > 89999 and grossSalary < 100000:
        nhifContribution == 1600
    else:
        nhifContribution == 1700
    
    return nhifContribution
