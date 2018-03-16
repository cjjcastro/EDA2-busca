""" Python version 3.6.3 """
from random import randint
import os
max_len = 100

def insertion_sort(list_db = []):
    for current_item in range(0,len(list_db)):

        next_item = current_item

        while next_item != 0 and list_db[next_item] < list_db[next_item -1]:
            aux = list_db[next_item]
            list_db[next_item] = list_db[next_item - 1]
            list_db[next_item - 1] = aux
            next_item-=1

def index_list(list_db = []):
    list_index=[]
    index = [index for index in range(0,max_len,10)]
    list_values = [list_db[code] for code in index]
    return list_values , index

def search_binary(list_db,number):
    begin = 0
    end = max_len - 1
    while begin <= end :
        find = int((begin + end) / 2)
        #print("Number: {} Find: {}".format(number,list_db[find]))
        if list_db[find] == number:
            print("encontrei")
            return find;
        if list_db[find] < number:
            begin = find + 1
        else:
            end = find - 1
    return -1

def init_list(db):
    list_db = []
    for line in db:
        list_db.append(int(line))
    db.close()
    return list_db


def choise(answer,list_db):
    if answer == 0:
        print("Good bye!!")

	if answer == 1:
        print("Unsorted list :\n {}".format(list_db))
        print("\n\n\n")
    if answer == 2:
        insertion_sort(list_db)
        print("Sorted list :\n {}".format(list_db))
        print("\n\n\n")
    if answer == 3:
        print("Write a number of your choise!\n")
        ans_1 = int(input())
        ans_2 = search_binary(list_db,ans_1)
        if ans_2 != -1:
            print("Found: {}\n".format(list_db[ans_2]))
        else:
            print("Don't find anything\n")

    if answer == 4:
        list_values,list_index= index_list(list_db)
        print("Index list: \n{}".format(list_values))
        print("Indexes: \n{}".format(list_index))
        print("\n")



if __init__ == "__main__":

path = os.path.dirname(os.path.abspath(__file__))
new_path = os.path.join(path,"db.txt")

if os.stat(new_path).st_size == 0 :
    db = open("db.txt","w+")
    for count in range(0,max_len):
        number = randint(0,99999)
        db.write("%d \n" %(number))
    db.close()

db = open("db.txt","r")
list_db = init_list(db)

while ans > 0:
    print("Choose one of choises bellow:\n1-Print unorder list.\n2- Print order list.\n3-Find a number.\n4- Print list index\n0- getout here.")
    answer = input()
    choise(answer,list_db)
    input()
    os.system("clear")
