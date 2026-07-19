print('\n\n')
print(f"\t\t {'='*20} MKB ATM ⭐ {'='*20}")
print()

print("\t- Create your Account in MKB ATM")

account_holder = {
    'name': input('Name = ').strip().title(),
    'phone_number': int(input('Phone Number = +91 ').strip()),
    'mail': input('Mail ID = ').strip(),
    'pincode': input('\n\t⭐ Create PIN = ').strip(),
    'balance': input("\nDeposit Initial Balance = Rs. ").strip()
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

pincode = account_holder['pincode']

if not (pincode.isdigit() and len(pincode) == 4):
    print('❌ Invalid PIN. It must contain exactly 4 digits.')
    valid = False

if not account_holder['balance'].isdigit() or int(account_holder['balance']) <= 0:
    print("❌ Balance can not be maintained at 0 or below that.")
    valid = False

if valid:
    account_holder['balance'] = float(account_holder['balance'])

    print(f'\n\t{'-'*20} Congratulation {'-'*20}\n\t ✅ Customer Acc. is created Successfully.')
        
    continue_account = input('\nDo you want to continue with your account? (Yes/No) ').strip().upper()

    if continue_account == 'YES' or continue_account == 'Y':

        pin = input("\n\t~~~ MKB ATM PIN = ").strip()

        if pin == account_holder['pincode']:
            print("PIN verified.")
            print(f"\n{'~'*20} 🏧 ATM Menu {'~'*20}")
            print(f"{' '*20}~~~~~~~~~~~~~~{' '*20}")
            while True:

                print(f"\n\t----> 1. Deposit💵 \n\t----> 2. Withdraw📉 \n\t----> 3. Balance Enquiry⚖️ \n\t----> 4. Account Info.🏦 \n\t----> 5. Change Pin🫆 \n\t----> 6. Exit💨 \n")

                choice = input('Enter your choice - ').strip().lower()

                if choice in ('deposit', '1'):

                    d_amount = float(input('~ Amount to be Deposit :- ').strip())
                    if d_amount <=0:
                        print('\n❌ Enter an amount greater than zero.')
                    else:
                        account_holder['balance'] += d_amount
                        print(f'\n\t✅ Your Account has been credited by an amount {d_amount} 💵\n')
                        print(f'\n\t Total Acc. Balance after credited is {account_holder['balance']}')
                    
                        ruse = input('\n\t Do you want to Redirect to ATM Menu🏦 (yes/no) :- ').strip().lower()
                        if ruse in ('yes', 'y'):
                            print(f'\n\t Redirecting to Menu\n\t {"-"*15}')
                            continue
                        else:
                            print(f"\n\t{'~'*20} Thank You for using MKB ATM {'~'*20}\n\t{'~'*20} Visit Again {'~'*20}\n\t{'~'*20} MKB ATM ⭐ {'~'*20}\n\n")
                            break

                elif choice in ('withdraw', '2'):

                    w_amount = float(input('~ Amount :- ').strip())
                    if w_amount <= 0:
                        print("❌ Enter an amount greater than zero.")
                    elif w_amount > account_holder['balance']:
                        print("❌ Insuffiecient Balance")
                    else:
                        account_holder['balance'] -= w_amount

                        print(f'\n\t✅Your Account has been debited by an amount {w_amount} 💵\n')
                        print(f'\n\t Total Acc. Balance after withdrawal is {account_holder['balance']}')
                        ruse = input('\n\t Do you want to Redirect to ATM Menu🏦 (yes/no) :- ').strip().lower()
                        if ruse in ('yes', 'y'):
                            print(f'\n\t Redirecting to Menu\n\t {"-"*15}')
                            continue
                        else:
                            print(f"\n\t{'~'*20} Thank You for using MKB ATM {'~'*20}\n\t{'~'*20} Visit Again {'~'*20}\n\t{'~'*20} MKB ATM ⭐ {'~'*20}\n\n")
                            break
                            
                elif choice in ('balance', '3'):
                    print(f'\n\t✅ Account Balance = Rs. {account_holder['balance']} 💵\n')
                    ruse = input('\n\t Do you want to Redirect to ATM Menu🏦 (yes/no) :- ').strip().lower()
                    if ruse in ('yes', 'y'):
                        print(f'\n\t Redirecting to Menu\n\t {"-"*15}')
                        continue
                    else:
                        print(f"\n\t{'~'*20} Thank You for using MKB ATM {'~'*20}\n\t{'~'*20} Visit Again {'~'*20}\n\t{'~'*20} MKB ATM ⭐ {'~'*20}\n\n")
                        break

                elif choice in ('account info', '4'):
                    print(f'\nAccount Holder Information: \n {'-'*20}')
                    for keys,values in account_holder.items():
                        print(f'*{keys.upper()} = {values}')
                    ruse = input('\n\t Do you want to Redirect to ATM Menu🏦 (yes/no) :- ').strip().lower()
                    if ruse in ('yes', 'y'):
                        print(f'\n\t Redirecting to Menu\n\t {"-"*15}')
                        continue
                    else:
                            print(f"\n\t{'~'*20} Thank You for using MKB ATM {'~'*20}\n\t{'~'*20} Visit Again {'~'*20}\n\t{'~'*20} MKB ATM ⭐ {'~'*20}\n\n")
                            break

                elif choice in ('change pin', '5'):
                    if account_holder['pincode'] == input(f'\nEnter Existing Pin of {account_holder["name"]} Acc. = '):
                        print(f"\n\tCreate New Pincode for your bank 🏦\n\t{'-'*20}")
                        new_pincode = input("New Pin Code🫆 = ")
                        if new_pincode.isdigit() == True and len(new_pincode) == 4:
                            print(f"⭐ New Pin has created :- ({new_pincode})")
                            account_holder['pincode'] = new_pincode

                            ruse = input('\n\t Do you want to Redirect to ATM Menu🏦 (yes/no) :- ').strip().lower()
                            if ruse in ('yes', 'y'):
                                print(f'\n\t Redirecting to Menu\n\t {"-"*15}')
                                continue
                            else:
                                print(f"\n\t{'~'*20} Thank You for using MKB ATM {'~'*20}\n\t{'~'*20} Visit Again {'~'*20}\n\t{'~'*20} MKB ATM ⭐ {'~'*20}\n\n")
                                break
                            
                        else:
                            print('❌ Invalid PIN. It must contain exactly 4 digits.')
                    else:
                        print("\n\t❌ Invalid Pin")

                elif choice in ('exit', '6'):
                    print('\n\tThank you for using MKB ATM. Visit again!')
                    break

                else:
                    print(f"\n\t❌ Invalid choice. Please select 1, 2, 3, 4, 5 or 6.\n\n")

        else:
            print('\n\t❌ Invalid Pin')
            print(f"\n\t{'~'*20} Thank You for using MKB ATM {'~'*20}\n\t{'~'*20} Visit Again {'~'*20}\n\t{'~'*20} MKB ATM ⭐ {'~'*20}\n\n")
    else:
        print(f"\n\t{'~'*20} Thank You for using MKB ATM {'~'*20}\n\t{'~'*20} Visit Again {'~'*20}\n\t{'~'*20} MKB ATM ⭐ {'~'*20}\n\n")
else:
    print('\n\t❌ Account Creation Failed. Please check the errors above and try again.')