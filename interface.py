from Bank import BankAccount

customer_dict = {}              # use account no. as key and class object(customer account) as value
mobile_acc_link = {}            # use mobile no. as key and store account no. as value, for linking purpose

def new_cust():
    name = input('Enter the name of customer: ')
    mobile_no = int(input('Enter the mobile number of customer: '))
    initial_depo = int(input('Enter the initial deposit amount: '))
    if initial_depo <= 0:
        print('Invalid Amount')
        return
    pin = int(input('Create PIN: '))
    customer = BankAccount(name=name, mobile_no=mobile_no, initial_depo=initial_depo, pin=pin)
    customer_dict[customer.cust_acc_num] = customer                 # acct. no. stored as key and oject as value
    mobile_acc_link[customer.mobile_no] = customer.cust_acc_num     # mobile no. linked
    print('New User Created!')
    print(f'Welcome {customer.name} to Corporate Bank. {customer.cust_acc_num} is your account number')

def login():
    account_no = int(input('Enter your Account Number: '))
    account_pin = int(input('Enter your Account PIN: '))
    if account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin :
        print(f'\n{customer_dict[account_no].name} Logged in')
        customer_dict[account_no].basic_details()
    else:
        print('Account either not exist or the pin is wrong')
        return
    while True:
        print('''1. Deposit
2. Withdrawl
3. Money transfer
4. Log out\n''')
        user_input1 = input('Please enter your choice:')
        if user_input1 == '1':
            customer_dict[account_no].deposit()
        elif user_input1 == '2':
            customer_dict[account_no].withdrawl()
        elif user_input1 == '3':
            mobile = int(input('Enter the mobile number of recepient: '))
            if mobile in mobile_acc_link.keys():
                secondary = mobile_acc_link[mobile]             # use mobile no. to get acct. no.
                customer_dict[account_no].payment(customer_dict[secondary])
            else:
                print('The mobile number you have enter does not have an account associated with it')
        elif user_input1 == '4':
            user_input1 = input('Do you really want to log out? Yes or No?') 
            print('Logged Out')
            return
        else:
            print('Invalid input try again')
        print('\n#############################################################\n')
        customer_dict[account_no].basic_details()
      
