print("Hello, WORLD!")

user_input = input('Name: ')

name = user_input

import time

while True:
    Gate = input("PASSWORD: ")
    if  Gate == 'COMPUTER':
            time.sleep(2)
            print ("ACCESS GRANTED!")
            print ("Welcome to PYTHON, code away!")
    else:
        time.sleep(2)
        print ("ACCESS DENIED")
    break
import time

while True:
    ponder = input('Do this or that? ')
    def do_this():
        print('Doing this...')
        
    def doing_that():
        print('Doing that...')
        
        if ponder == 'This':
            time.sleep(1)
            print(doing_this)
        if ponder == 'That':
            time.sleep(1)
            print(doing_that)
        else:
            print('INVALID REQUEST')
        
        