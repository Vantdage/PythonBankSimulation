# all functions kept in this file to keep main file cleaner. 
# run this to update it, then run bank.py to start
version = '1.0.00'
creator = 'Andrew Dovan'

import os

def display_menu():
    print('################')
    print('# OFFLINE BANK #')
    print('################')
    print('project by ' + creator)
    print('Version: ' + version + '\n')

def login_menu_options():
    print('1. Create Account')
    print('2. Login')
    login_menu_choice = input('Enter Numerical Choice: ')
    print('\n')

    if login_menu_choice == '1':
        #call create user function
        create_user()
    elif login_menu_choice == '2':
        #call login user function
        login_user()
    else:
        #if failed recall function
        print("INCORRECT INPUT")
        login_menu_options()
    
def create_user():
    print('Create User Function')
    username = input('Please enter a username: ')
    password = input('Please enter a password: ')

    #write to file username and password
    #CHECK IF USERNAME IS TAKEN, IMPLEMENT
    #aaf = open('accounts.txt', 'r') #all accounts file
    #for line in aaf:
        #if username == line.strip:
            #print('taken')
        #else:
            #continue
    #aaf = open('accounts.txt', 'a')
    #aaf.write(username)
    #aaf.write('\n')
    #aaf = open('accounts.txt', 'a')
    
    ucf = open(username + '_credentials.txt', 'w') #user credential files
    ucf.write(username + ':' + password + '\n0')
    ucf.close()

    #call menu
    login_menu_options()


def login_user():
    username = input('Please enter a username: ')
    password = input('Please enter a password: ')
    
    #reading from file
    
    ucf = open(username + '_credentials.txt', 'r') 
    lines_to_read = [0]
    for position, line in enumerate(ucf):
        if position in lines_to_read:
            login = line
    
    login = login[:-1]
    print(login)
    if login == username + ':' + password:
        user_menu(username, password)
        ucf.close()
    else:
        print('DENIED')
        ucf.close()
        login_menu_options()

def user_menu(username, password):    
    print('Choose Option:')
    print('1. Check Balance')
    print('2. Send Money')
    print('3. Deposit Money')
    print('4. Change Password')
    print('5. Log out')
    print('6. Delete Account')
    
    login_menu_choice = input('Enter Numerical Choice: ')
    print('\n')

    if login_menu_choice == '1':
        check_balance(username)
    elif login_menu_choice == '2':
        send_money_data(username)
    elif login_menu_choice == '3':
        deposit_money(username)   
    elif login_menu_choice == '4':
        change_password(username, password)
    elif login_menu_choice == '5':
        print('Logging out...')
        print('DONE')
    elif login_menu_choice == '6':
        print('deleted')
        os.remove(username + '_credentials.txt')

    else:
        print("INCORRECT INPUT")
        user_menu(username, password)

def check_balance(username):
    ucf = open(username + '_credentials.txt', 'r')
    lines_to_read = [1]
    for position, line in enumerate(ucf):
        if position in lines_to_read:
            balance = line
    ucf.close()
    print('$' + balance)

def send_money_data(username):
    print('\n')
    print('SEND MONEY')
    ucf = open(username + '_credentials.txt', 'r')
    lines_to_read = [1]
    for position, line in enumerate(ucf):
        if position in lines_to_read:
            balance = line
    ucf.close()
    print('CURRENT BALANCE IS: $' + balance)
    amount = input('Enter amount to send: ')
    recipitent = input('Enter account to send to: ')
    try:
        float(amount)
        print(amount)
        send_money(amount, username, recipitent)
    except ValueError:
        print('ENTER VALID AMOUNT OR FORMAT')
        send_money_data(username)


def send_money(amount, username, recipitent):
    print('send ' + amount)
    ucf = open(username + '_credentials.txt', 'r') 
    lines_to_read = [1]
    for position, line in enumerate(ucf):
        if position in lines_to_read:
            client_balance = line
    rf = open(recipitent + '_credentials.txt', 'r')
    lines_to_read = [1]
    for position, line in enumerate(rf):
        if position in lines_to_read:
            recipitent_balance = line

    ucf.close()
    rf.close()
    client_balance = float(client_balance)
    recipitent_balance = float(recipitent_balance)
    amount = float(amount)
    
    
    if client_balance > amount or client_balance == amount:
        recipitent_balance = recipitent_balance + amount
        
        client_balance = client_balance - amount
        

        #write balance to client
        file = open(username + '_credentials.txt')
        lines = file.readlines()
        file.close()
        client_balance = str(client_balance)
        lines[1] = client_balance + '\n'
        f = open(username + '_credentials.txt', 'w')
        f.writelines(lines)
        f.close()
        
        #write balance to recipitent
        file = open(recipitent + '_credentials.txt', 'r')
        lines = file.readlines()
        file.close()
        recipitent_balance = str(recipitent_balance)
        lines[1] = recipitent_balance + '\n'
        f = open(recipitent + '_credentials.txt', 'w')
        f.writelines(lines)
        f.close()
        print('SENT')
    elif client_balance < amount:
        print('NOT ENOUGH MONEY')
        send_money_data(username)
    else:
        print('something went wrong')
    
def deposit_money(username):
    ucf = open(username + '_credentials.txt', 'r') 
    lines_to_read = [1]
    for position, line in enumerate(ucf):
        if position in lines_to_read:
            client_balance = line
    ucf.close()
    print('CURRENT BALANCE IS: $' + client_balance)
    client_balance = float(client_balance)
    amount = input('Enter amount to deposit: ')
    try:
        amount = float(amount)
        client_balance = client_balance + amount
    except ValueError:
        print('ENTER VALID AMOUNT OR FORMAT')
        deposit_money(username)

    
    
    file = open(username + '_credentials.txt')
    lines = file.readlines()
    file.close()
    client_balance = str(client_balance)
    lines[1] = client_balance + '\n'
    f = open(username + '_credentials.txt', 'w')
    f.writelines(lines)
    f.close()
    print('Deposited!... logged out')

def change_password(username, password):
    print('CHANGE PASSWORD')
    password_check = input('Enter current password: ')
    if password_check == password:
        new_password = input('Enter new password: ')
        print(new_password)
    else: 
        print('DENIED')
        change_password(username, password)
    file = open(username + '_credentials.txt')
    lines = file.readlines()
    file.close()
    lines[0] = username + ':' + new_password + '\n'
    f = open(username + '_credentials.txt', 'w')
    f.writelines(lines)
    f.close()
