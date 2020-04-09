import requests
import sys
import json


def fetch_chain():
    data = requests.get(url=node + '/').json()
    return data


def calc_balance(data, id):
    # Calculating balance
    balance = 0

    for block in data['chain']:
        for transaction in block['transactions']:
            if transaction['recipient'] == id:
                balance += int(transaction['amount'])
            if transaction['sender'] == id:
                balance -= int(transaction['amount'])

    return balance


def get_transactions(data, id):
    my_transactions = []

    for block in data['chain']:
        for transaction in block['transactions']:
            if transaction['recipient'] == id or transaction['sender'] == id:
                my_transactions.append(transaction)

    return my_transactions


if __name__ == '__main__':
    # What is the server address? IE `python3 miner.py https://server.com/api/`
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    # Load ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    # grabs the block chain from server
    data = fetch_chain()

    balance = calc_balance(data, id)

    transactions = get_transactions(data, id)

    print(f'Welcome to the Wallet App {id}!')

    while True:
        action = input('\nWhat would you like to do? (h for help): ')
        if action == "h":
            print(f'(id) Change Id, Current: {id}')
            print('(b) Display Balance')
            print('(t) Display transactions')
            print('(r) Refresh Blockchain')
            print('(e) Exit')
        elif action == 'e':
            break
        elif action == 'id':
            id = input('Input New Id: ')
            balance = calc_balance(data, id)
            transactions = get_transactions(data, id)
        elif action == 'b':
            print(f'Balance: {balance}')
        elif action == 't':
            print(f'Transactions: {transactions}')
        elif action == 'r':
            print('Refetching up to date blockchain')
            data = fetch_chain()
            balance = calc_balance(data, id)
            transactions = get_transactions(data, id)
        else:
            print('Input not recognized. Press (h) for help.')
