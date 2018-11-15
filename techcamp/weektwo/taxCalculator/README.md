# TAX CALCULATOR

1. Create a program that calculates and prints the net salary of an individual.
2. The program should take the "basicSalary", "overtime", "houseAllowance", "otherBenefits" and.
3. Use it to calculate the net salary.
4. Use the Payee Table to find Payee, NHIF Table to find nhifContribution and nssfContribution

*HINT:*
>netSalary = grossSalary - deductions + personalRelief
>grossSalary = basicSalary + overtime + huseAllowance + otherBenefits
>deductions = payee + nhifContribution + nssfContribution

## Functions

i. getNetSalary(gross, deductions)
ii. getGrossSalary(basic, benefits)
iii. getDeductions(payee, nhif, nssf)
iv. getBenefits(overtime, house, other)
v. getPayee(gross)
vi. getNHIF(gross)
vii. getNSSF(gross)
