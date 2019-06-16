import numpy
import pprint
import  webbrowser
import requests

print('Hi Vivek! Welcome to Python World')

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
print(res.content)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']
            ]

print(str(tableData) + "\n")
print(max(tableData[0]))
colWidths = [0] * len(tableData)
for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        print(tableData[j][i].rjust(int(len(colWidths))), end=" ")
    print()
print()

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory():

    totalItems = 0
    keys = []
    print("Inventory: ")

    for k in inventory.keys():
        keys.append(k)

    keys.sort()

    for key in keys:
        print(inventory[key], " ", key)
        totalItems += inventory[key]

    '''
    for k,v in inventory.items():
        print(v, " ", k)
        totalItems += v
    '''

    print("Total number of items: ", totalItems )

displayInventory()
print(inventory)
#inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'gem', 'ruby']
inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print("Before adding inventory: ", inventory)
def addToInventory(inventory, addedItems):
    totalItems = 0
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
    print("\nAdded inventory list: ", inventory)
    print("Inventory")
    for k,v in inventory.items():
        print(v, " ", k)
        totalItems += inventory[k]
    print("Total Number of Items: ", totalItems)
addToInventory(inventory, dragonLoot)

print("\n")
'''
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn

message = 'vivekaba'

#def charCount():
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#charCount()
pprint.pprint(count)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
       ]
print(numpy.shape(grid))
for i in range(len(grid[0])):
    print("\n")
   # print(str(i) + " ", end="")
    for j in range(len(grid)):

        # print(str(j)+ str(i) + " ", end="")
        #print(str(j) + ' ' + str(i) + ": ", end="" )
        #if j != 5:
        print(grid[j][i], end="")
'''

'''
print("\n")
for index in range(len(grid)):
    print(grid[index], end="\n")
'''
spam = ['apples', 'bananas', 'tofu', 'cats']
# 'apples, bananas, tofu, and cats'

st = ''
for index in range(len(spam)):
    if index != (len(spam) - 1):
       st +=  spam[index] + ','
    else:
        st += ' and ' + spam[index]

print("Chap4 exercise 1: " + st)

'''
import random
messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']

def pickOne(messages):
    print(messages[random.randint(0,len(messages) - 1)])

choice = ""
while True:
    print("PickOne: ", end="")
    choice = input()

    if (choice == 'n') | (choice == 'N'):
        break
    else:
        pickOne(messages)


'''

print("\nCollatz Sequence")


cumulative100 = 0
for i in range(100):
    cumulative100 += i
print(cumulative100)

for i in range(10, 0, -1):
    print(i)

'''
# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
'''