from payee import payee
from nhif import nhifContribution
from nssf import nssfContribution


def getDeductions(payee, nhifContribution, nssfContribution):
    deductions = payee + nhifContribution + nssfContribution

    return deductions
