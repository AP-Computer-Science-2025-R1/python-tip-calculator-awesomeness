
def greet_user():
    print("--------------------------------------------------------- \n Welcome to the NYC Tip calculator! ")
def calculate_ny_tax(subtotal1):
    return subtotal1 * 0.08875

def get_tip_percentage(subtotal1):
    while True:
        print("How much would like to tip:")
        user_tip= int(input("1) 15% \n 2) 18% \n3) 20% \n 4) Custom Amount \n Select Option: "))
        if user_tip == 1:
            tip_percentage = 0.15
            break
        elif user_tip== 2:
            tip_percentage = 0.18
            break
        elif user_tip== 3:
            tip_percentage = 0.2
            break
        elif user_tip== 4:
            imput_perc= float(input("Enter Custom Percentage: "))
            if imput_perc > 1:
                tip_percentage= imput_perc / 100
                break
            else:
                tip_percentage = imput_perc
                break
        else:
            print("Invalid Option")
    tipamount= tip_percentage * subtotal1
    return tipamount , tip_percentage * 100
        
def get_bill_total():
    return float(input("What was your bill subtotal:"))
    
greet_user()
subtotal= get_bill_total()
taxamt= round(calculate_ny_tax(subtotal))
tipamt , tipperc = get_tip_percentage(subtotal)
tipamt = round(tipamt)
print("calculating")
total=subtotal + taxamt + tipamt
print("----------------------------------------------- \n Bill summary: ")
print("The subtotal is: $", subtotal)
print("NYC Tax amount: 8.875% Tax Rate: $", taxamt)
print("The Tip amount was: %", tipperc, " $", tipamt)
print("The total is: $", total )
print("-----------------------------------------------")
ifsplit= input("Do You Want to Split The Bill? (y): ")
if ifsplit.lower() == 'y':
    numpeople= int(input("How many people to split the bill: "))
    splitamt= (total / numpeople)
    print("Each person owes: $", splitamt)
print(" \n -----------------------------------------------")
ifround = input("Do you want to round the total? (y): ")
if ifround.lower() == 'y':
    roundtotal= round(total)
    print("Your rounded total is: $", roundtotal)