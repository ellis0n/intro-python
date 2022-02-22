# This program calculates and displays payment plan options and customer billing for Honest Harry's Used Car Lot.
# Written by Glen May
# Written 2021 02 13

import datetime

# Constants to be changed by service provider if required.
HST = 0.15  # Harmonized sales tax
TRANSFEE = 0.01  # Standard transaction fee per sale
LUXTAX = 0.016  # Luxury tax on sale price above $20,000
moneySet = set("1234567890.")  # Allowable characters for dollar-value inputs

# Inputs required to calculate financing rates and purchase cost
while True:
    while True:
        try:
            invDate = input("Invoice date (YYYY-MM-DD): ")
            invDate = datetime.datetime.strptime(invDate, "%Y-%m-%d")
        except:
            print("Entry must be in valid format (YYYY-MM-DD)")
        else:
            break
    while True:
        salesRep = input("Sales representative: ").title()
        if salesRep == "":
            print("Entry cannot be blank. ")
        else:
            break
    while True:
        custFirst = input("Customer first name: ").title()
        if custFirst == "":
            print("Entry cannot be blank.")
        else:
            break
    while True:
        custLast = input("Customer last name: ").title()
        if custLast == "":
            print("Entry cannot be blank.")
        else:
            break
    while True:
        custStreet = input("Customer street address: ").title()
        if custStreet == "":
            print("Entry cannot be blank.")
        else:
            break
    while True:
        custCity = input("Customer city of residence: ").title()
        if custCity == "":
            print("Entry cannot be blank.")
        else:
            break
    while True:
        custProv = input("Customer province of residence [XX]: ").upper()
        if custProv == "":
            print("Entry cannot be blank.")
        elif custProv.isalpha() == False:
            print("Entry must only contain letters.")
        elif len(custProv) != 2:
            print("Entry must be two characters [XX].")
        else:
            break
    while True:
        custPost = input("Customer postal code: ").upper()
        if custPost == "":
            print("Entry cannot be blank.")
        elif len(custPost) != 6:
            print("Entry must be six characters in length. ")
        elif custPost.isalnum() == False:
            print("Entry must contain only letters and numbers. ")
        else:
            break
    while True:
        custPhone = str(input("Customer's phone number (10 digits): "))
        if custPhone == "":
            print("Entry cannot be blank. ")
        elif custPhone.isdigit() == False:
            print("Entry must only include numbers.")
        elif len(custPhone) != 10:
            print("Phone number must be ten digits in length.")
        else:
            break
    while True:
        plateNum = input("Vehicle license plate number [AAA000]: ").upper()
        if plateNum == "":
            print("Entry cannot be blank.")
        elif len(plateNum) != 6:
            print("License plate must be six characters in length. ")
        elif plateNum[0:3].isalpha() == False:
            print("First three characters must be letters. ")
        elif plateNum[3:6].isnumeric() == False:
            print("Last three characters must be numbers. ")
        else:
            break
    while True:
        carMake = input("Car make: ").title()
        if carMake == "":
            print("Entry cannot be blank. ")
        else:
            break
    while True:
        carModel = input("Car model: ").title()
        if carModel == "":
            print("Entry cannot be blank. ")
        else:
            break
    while True:
        carYear = input("Year of manufacture: ")
        if carYear == "":
            print("Entry cannot be blank. ")
        elif carYear.isnumeric() == False:
            print("Entry must only include numbers. ")
        elif len(carYear) != 4:
            print("Entry must be four digits in length.")
        else:
            carYear = int(carYear)
            break
    while True:
        sellPrice = input("Sale price of car: ")
        if sellPrice == "":
            print("Entry cannot be blank. ")
        elif set(sellPrice).issubset(moneySet) == False:
            print("Entry must only include numbers and decimal points. ")
        elif float(sellPrice) > 50000:
            print("Sale price cannot be above $50,000.00. ")
        elif float(sellPrice) == 0:
            print("Sale price cannot be $0.00")
        else:
            sellPrice = float(sellPrice)
            sellPriceDsp = "${:,.2f}".format(sellPrice)
            break
    while True:
        tradeIn = input("Trade in value of car: ")
        if tradeIn == "":
            print("Entry cannot be blank. ")
        elif set(tradeIn).issubset(moneySet) == False:
            print("Entry must only include numbers and decimal points. ")
        elif float(tradeIn) > sellPrice:
            print("Trade-in value cannot exceed sale price. ")
        else:
            tradeIn = float(tradeIn)
            tradeInDsp = "${:,.2f}".format(tradeIn)
            break
    while True:
        custCred = input("Customer Credit Card number: ")
        if custCred == "":
            print("Entry cannot be blank. ")
        elif custCred.isdigit() == False:
            print("Entry must only include numbers. ")
        elif len(custCred) != 16:
            print("Entry must be 16 characters.")
        else:
            break
    while True:
        custCredExp = input("Customer Credit Card expiry date: ")
        if custCredExp == "":
            print("Entry cannot be blank. ")
        elif custCredExp.isdigit() == False:
            print("Entry must only contain numbers. ")
        elif len(custCredExp) != 4:
            print("Entry must be four digits. ")
        else:
            break
            
    # Calculate customer billing including fees and taxes.
    tradeDiff = sellPrice - tradeIn
    tradeDiffDsp = "${:,.2f}".format(tradeDiff)
    taxAmt = tradeDiff * HST
    taxAmtDsp = "${:,.2f}".format(taxAmt)
    if sellPrice <= 5000:
        licFee = 75
    else:
        licFee = 165
    licFeeDsp = "${:,.2f}".format(licFee)
    if sellPrice < 20000:
        transFee = TRANSFEE * sellPrice
    else:
        transFee = (TRANSFEE * sellPrice) + (LUXTAX * sellPrice)
    transFeeDsp = "${:,.2f}".format(transFee)
    totalSale = tradeDiff + taxAmt + licFee + transFee
    totalSaleDsp = "${:,.2f}".format(totalSale)

    # Display customer payment plan options and input customer selection.
    while True:
        print("")
        print("# Years   # Payments    Financing Fee   Total Price    Monthly Payment")
        print("----------------------------------------------------------------------")
        for payPlan in range(1, 5):
            financeFee = (39.99 * payPlan)
            financeFeeDsp = "${:,.2f}".format(financeFee)
            month = payPlan * 12
            totalFinc = totalSale + financeFee
            totalFincDsp = "${:,.2f}".format(totalFinc)
            monthPay = (totalFinc / month)
            monthPayDsp = "${:,.2f}".format(monthPay)
            print("{:>5} {:>11} {:>17} {:>15} {:>18}".format(payPlan, month, financeFeeDsp, totalFincDsp, monthPayDsp))

        while True:
            print("")
            payPlan = input("Enter the payment schedule you want to follow (1-4): ")
            if payPlan == "":
                print("Entry cannot be blank. ")
            elif payPlan.isnumeric() == False:
                print("Entry must 1, 2, 3 or 4.")
            elif len(payPlan) != 1:
                print("Entry must contain one character.")
            elif int(payPlan) == 0:
                print("Entry cannot be 0.")
            elif float(payPlan) > 4:
                print("Entry must be 1, 2, 3 or 4.")
            else:
                payPlan = int(payPlan)
                print("")
                break
        break

    # Calculate remaining billing information including financing.
    financeFee = (39.99 * payPlan)
    financeFeeDsp = "${:,.2f}".format(financeFee)
    month = int(payPlan * 12)
    totalFinc = totalSale + financeFee
    totalFincDsp = "${:,.2f}".format(totalFinc)
    monthPay = (totalFinc / month)
    monthPayDsp = "${:,.2f}".format(monthPay)
    paymentDate = invDate + datetime.timedelta(days=30)

    # Display customer billing and financing selection.
    print("{:^33}".format("Honest Harry Car Sales"))
    print("{:^32}".format("Used Car Sale and Receipt"))
    print("")
    print("Invoice Date: {}".format(invDate.strftime("%B %m, %Y")))
    print("Receipt No: {}".format(custFirst[0] + custLast[0] + "-" + plateNum[2:6] + "-" + custPhone[6:10]))
    print("")
    print("Sold to:")
    print("     {}. {}".format(custFirst[0], custLast))
    print("     {}".format(custStreet))
    print("     {}, {}, {}".format(custCity, custProv, custPost))
    print("")
    print("Car Details:")
    print("     {} {} {}".format(carYear, carMake, carModel))
    print("--------------------------------")
    print("Sale price: {:>20}".format(sellPriceDsp))
    print("Trade Allowance: {:>15}".format(tradeInDsp))
    print("Price after Trade: {:>13}".format(tradeDiffDsp))
    print("                      ----------")
    print("HST: {:>27}".format(taxAmtDsp))
    print("License Fee: {:>19}".format(licFeeDsp))
    print("Transfer Fee: {:>18}".format(transFeeDsp))
    print("                      ----------")
    print("Total Sales cost: {:>14}".format(totalFincDsp))
    print("--------------------------------")
    print("Terms: {}      Total Payments: {:>2}".format(payPlan, month))
    print("Monthly payment: {:>15}".format(monthPayDsp))
    print("First payment date: {:>12}".format(paymentDate.strftime("%d %b %Y").upper()))
    print("")
    print("{:^33}".format("Honest Harry Car Sales"))
    print("{:^33}".format("Best used cars at the best price!"))
    print("")

    # Restart prompt
    while True:
        restart = input("Input another sale? Press Y to continue, N to exit: ").upper()
        if restart == "":
            print("Entry cannot be blank.")
        elif len(restart) > 1:
            print("Entry too long.")
        elif restart == "N":
            print("Thank you. Good bye.")
            quit()
        elif restart == "Y":
            print("Restarting...")
            break
