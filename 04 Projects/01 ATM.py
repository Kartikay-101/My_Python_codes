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

if not account_holder['name'].isalpha():
    print('Invalid Name')
    valid = False

if len(account_holder['phone_number']) != 10 or account_holder['phone_number[0]' not in '6789']:
    print('Invalid Phone Number')

print('\nAccount Holder Information =')
for keys,values in account_holder.items():
    print(f'{keys} = {values}')