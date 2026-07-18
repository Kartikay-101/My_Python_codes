print(f"\n{'~'*20} 🏧 ATM Menu {'~'*20}")
        print(f"{' '*20}~~~~~~~~~~~~~~{' '*20}")

        print(f"\n\t----> 1. Deposit💵 \n\t----> 2. Withdraw📉 \n\t----> 3. Balance Enquiry⚖️ \n\t----> 4. Exit💨 \n")

        choice = input('Enter your choice - ').strip().lower()

        if choice == 'deposit' or choice == 1:

            d_amount = float(input('~ Amount :- ').strip())
            balance = balance + d_amount
            print(f'\n\t✅Your Account has been credited by an amount {d_amount} 💵\n')
            print(f'\n\t Total Acc. Balance after credited is {balance}')

        elif choice == 'withdraw' or choice == 2:

            w_amount = float(input('~ Amount :- ').strip())
            balance = balance - w_amount
            print(f'\n\t✅Your Account has been debited by an amount {w_amount} 💵\n')
            print(f'\n\t Total Acc. Balance after withdrawal is {balance}')

        elif choice == 'balance' or choice == 3:
            print(f'\n\t✅ Account Balance = {balance} 💵\n')
        