print('\n\n')
print(f"\t\t {'='*20} MKB ATM ⭐ {'='*20}")
print()

print("\t- Create your Account in MKB ATM")

account_holder = {
    'name': input('Name - ').strip().title(),
    'phone_number': int(input('Phone Number - +91 ').strip()),
    'mail': input('Mail ID - ').strip(),
    'pincode': int(input('\n\t⭐Create Pin = ').strip())
}
valid = True

if not account_holder['name'].replace(' ', '').isalpha():
    print('❌ Invalid Name')
    valid = False

phone_n = str(account_holder['phone_number'])
if len(phone_n) != 10 or phone_n[0] not in '6789':
    print('❌ Invalid Phone Number')
    valid = False

if account_holder['mail'].count('@') != 1 or account_holder['mail'].endswith('.com') == False:
    print('❌ Invalid Mail Id')
    valid = False

pincode_1 = str(account_holder['pincode'])
if len(pincode_1) > 4:
    print('❌ Invalid Pin [It should be numeric and 4 Digit]')
    valid = False

if valid:
    print(f'\n\t{'-'*20} Congratulation {'-'*20}\n\t ✅ Customer Acc. is created Successfully.')
    print(f'\nAccount Holder Information: \n {'-'*20}')
    for keys,values in account_holder.items():
        print(f'*{keys.upper()} = {values}')
        print()
    balance = float(0)

continue_account = input('Do you want to continue with your account? (Yes/No) ').strip().upper()

if continue_account == 'YES' or continue_account == 'Y':

    pin = int(input("\n\t ~~~ MKB ATM Pin = "))

    if pin == account_holder['pincode']:
        print(f"\n{'~'*20} 🏧 ATM Menu {'~'*20}")
        print(f"{' '*20}~~~~~~~~~~~~~~{' '*20}")

        print(f"\n\t----> 1. Deposit💵 \n\t----> 2. Withdraw📉 \n\t----> 3. Balance Enquiry⚖️ \n\t----> 4. Exit💨 \n")

        choice = input('Enter your choice - ').strip().lower()

        if choice == 'deposit' or choice == '1':

            d_amount = float(input('~ Amount :- ').strip())
            balance = balance + d_amount
            print(f'\n\t✅Your Account has been credited by an amount {d_amount} 💵\n')
            print(f'\n\t Total Acc. Balance after credited is {balance}')

        elif choice == 'withdraw' or choice == '2':

            w_amount = float(input('~ Amount :- ').strip())
            balance = balance - w_amount
            print(f'\n\t✅Your Account has been debited by an amount {w_amount} 💵\n')
            print(f'\n\t Total Acc. Balance after withdrawal is {balance}')

        elif choice == 'balance' or choice == '3':
            print(f'\n\t✅ Account Balance = {balance} 💵\n')
        
        else:
            print(f"\n\t{'~'*20} Thank You for using MKB ATM {'~'*20}\n\t{'~'*20} Visit Again {'~'*20}\n\t{'~'*20} MKB ATM ⭐ {'~'*20}")

    else:
        print('\n\t❌ Invalid Pin')
        print(f"\n\t{'~'*20} Thank You for using MKB ATM {'~'*20}\n\t{'~'*20} Visit Again {'~'*20}\n\t{'~'*20} MKB ATM ⭐ {'~'*20}\n\n")
else:
    print(f"\n\t{'~'*20} Thank You for using MKB ATM {'~'*20}\n\t{'~'*20} Visit Again {'~'*20}\n\t{'~'*20} MKB ATM ⭐ {'~'*20}\n\n")