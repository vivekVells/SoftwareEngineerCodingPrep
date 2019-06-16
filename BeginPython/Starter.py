import  random
import sys

class Animal:
    __name = ""

    def __init__(self, name):
        self.__name = name


    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

cat = Animal("Jack")
cat.setName("Tommy")
print(cat.getName())

class dog(Animal):
    __owner = ""

    def __init__(self, owner, name):
        self.__owner = owner
        super(dog, self).__init__(name)

    def setOwner(self, owner):
        self.__owner = owner

    def setName(self, name):
        self.__name = name

    def getOwner(self):
        return  self.__owner

    def toString(self):
        return  "{} is the owner and {} is dog's name".format(self.getOwner(), self.getName())


nai = dog("Vivek", "Jimmy")
print(nai.toString())




'''
print( range(0,6))
print("What is your name? ")
name = sys.stdin.readline();
print("Hai", name)


str2 = [0,1,2,3]

str3 = "abcd1efgh";

'''

'''
list1 = [[5,6], [3,1000], [10]];

print(max(list1))

tuple1 = (5,6,9,5)
print(tuple(list(tuple1)))

tuple1 = (55,566)
print((tuple1.bit_length()))
print(len(tuple1))

dict1 = {'key1':'value1', 'key2':'value2'}

print(len(dict1))

list3 = list(dict1.values());
print(list3[0])

print(list(dict1.items())[0:1])

if 5 > 2:
    print('Yes, the value is greater....')

print("\n\ncheck")
for i in range(0,len(list1)):
    print(list1)

for k in (0,5):
    print(k, ' ' , end='')
'''