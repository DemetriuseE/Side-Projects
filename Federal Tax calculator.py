Salary_required= "Please input your salary"
print(f"{Salary_required} and press [enter] once done.")
State_Taxes_AL = 0.05
State_Taxes_AK = 0
State_Taxes_AZ = 0.025
State_Taxes_AR = 0.049
State_Taxes_CA = 0.133
State_Taxes_CZ = 0 #Canal Zone#
State_Taxes_CO = 0.0440
State_Taxes_CT = 0.0699
State_Taxes_DE = 0.0660
State_Taxes_DC = 0.1075
State_Taxes_FL = 0
State_Taxes_GA = 0.0575
State_Taxes_GU = 0 #Guam#
State_Taxes_HI = 0.1100
State_Taxes_ID = 0.0580
State_Taxes_IL = 0.0495
State_Taxes_IN = 0.0315
State_Taxes_IA = 0.0600
State_Taxes_KS = 0.0570
State_Taxes_KY = 0.0450
State_Taxes_LA = 0.0425
State_Taxes_ME = 0.0715
State_Taxes_MD = 0.0575
State_Taxes_MA = 0.0900
State_Taxes_MI = 0.0425
State_Taxes_MN = 0.0985
State_Taxes_MS = 0.05
State_Taxes_MO = 0.0495
State_Taxes_MT = 0.0675
State_Taxes_NE = 0.0664
State_Taxes_NV = 0
State_Taxes_NH = 0.0400
State_Taxes_NM = 0.0590
State_Taxes_NY = 0.1090
State_Taxes_NC = 0.0475
State_Taxes_ND = 0.0290
State_Taxes_OH = 0.0399
State_Taxes_OK = 0.0475
State_Taxes_OR = 0.099
State_Taxes_PA = 0.0307
State_Taxes_PR = 0 #Puerto Rico#
State_Taxes_RI = 0.0599
State_Taxes_SC = 0.0650
State_Taxes_SD = 0.0
State_Taxes_TN = 0
State_Taxes_TX = 0
State_Taxes_UT = 0.0485
State_Taxes_VT = 0.0875
State_Taxes_VI = 0 #Virgin Islands#
State_Taxes_VA = 0.0575
State_Taxes_WA = 0.0700
State_Taxes_WV = 0.0650
State_Taxes_WI = 0.0765
State_Taxes_WY = 0

number = int(input())
if number < 11000:
    number = number * 0.10
    print(f"This is how much you owe in federal taxes: ${number}.")
if number > 11000 and number < 44725:
    number = number * 0.12
    print(f"This is how much you owe in federal taxes: ${number}.")
if number > 44725 and number < 95375:
    number = number * 0.22
    print(f"This is how much you owe in federal taxes: ${number}.")
if number > 95375 and number < 182100:
    number = number * 0.24
    print(f"This is how much you owe in federal taxes: ${number}.")
if number > 182100 and number < 231250:
    number = number * 0.32
    print(f"This is how much you owe in federal taxes: ${number}.")
if number > 231250 and number < 578125:
    number = number *0.35
    print(f"This is how much you owe in federal taxes: ${number}.")
if number > 578125:
    number = number * 0.37
    print(f"This is how much you owe in federal taxes: ${number}.")
else:
    print("Have a great day.")
