avg_lung_cancer_pack = 10.15
avg_lung_cancer_price = avg_lung_cancer_pack / 20

def eu_2_dollar(money):
    dollar = 1.125 * money
    return dollar

def dollar_2_eu(money):
    eu = 0.8642 * money
    return eu

currency_choice = 0

while currency_choice == 0:
    print("What currency are you using?\n\n1. U.S. dollars\n2. Euros\n")
    currency_choice = input()
    if int(currency_choice) == 1:
        num_lung_cancer = int(input("How many packs of c*garettes did you buy? "))
        price = float(input("How much did you pay for them? ")) if num_lung_cancer > 1 else float(input("How much did you pay for it? ")) 
        price_per = (price / num_lung_cancer)
        percent_saved = abs((price_per - avg_lung_cancer_pack) / avg_lung_cancer_pack) * 100
        if price_per >= avg_lung_cancer_pack:
            print(f"\nYou got scammed. (By {percent_saved:.1f}%).")
            break
        else:
            print(f"\nWow! What a deal! You payed {percent_saved:.1f}% less than average!")
            break
    if int(currency_choice) == 2:
        num_lung_cancer = int(input("How many packs of c*garettes did you buy? "))
        price = float(input("How much did you pay for them? ")) if num_lung_cancer > 1 else float(input("How much did you pay for it? "))
        normal_price = eu_2_dollar(price)
        price_per = (price / num_lung_cancer)
        percent_saved = abs((price_per - avg_lung_cancer_pack) / avg_lung_cancer_pack) * 100
        if price_per >= avg_lung_cancer_pack:
            print(f"\nYou got scammed. (By {percent_saved:.1f}%).")
            break
        else:
            print(f"\nWow! What a deal! You payed {percent_saved:.1f}% less than average!")
            break
    else:
        print("Pick 1 or 2 bruh")