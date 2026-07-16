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
    print('Invalid Name')
    valid = False

phone_n = str(account_holder['phone_number'])
if len(phone_n) != 10 or phone_n[0] not in '6789':
    print('Invalid Phone Number')
    valid = False

if account_holder['mail'].count('@') != 1 or account_holder['mail'].endswith('.com') == False:
    print('Invalid Mail Id')
    valid = False

if valid:
    print('\nAccount Holder Information =')
    for keys,values in account_holder.items():
        print(f'{keys} = {values}')