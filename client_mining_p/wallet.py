import requests
import sys
import json


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
    chain = requests.get(url=node + '/').json()

    while True:
        action = input('What would you like to do? (h for help)')
        if action == "h":
            print(f'(id) Change Id, Current: {id}')
            print('(b) Display Balance')
            print('(t) Display transactions')
