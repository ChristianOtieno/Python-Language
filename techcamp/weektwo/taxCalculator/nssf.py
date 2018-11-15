from grossSalary import grossSalary


def getNSSF(grossSalary):
    if grossSalary <= 6000:
        nssfContribution = 0.06 * 6000
    elif grossSalary > 6000 and grossSalary <= 18000:
        nssfContribution = 0.06 * grossSalary
    else:
        nssfContribution = 0.06 * 18000

    return nssfContribution
