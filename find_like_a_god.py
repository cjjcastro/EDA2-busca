""" Python version 3.6.3 """
from random import randint
import os
import time
max_len = 100


def sequencial_search(num_search,list_num):
    count = 0
    for item in list_num:
        if item[0] == num_search or item[0] > num_search:
            return item[1],list_num[count-1][1]
        count+=1
    return -1

def mix_search(list_db,num_search):
    insertion_sort(list_db)
    list_index = index_list(list_db)
    end,begin = sequencial_search(num_search,list_index)
    print("end: {} begin: {}".format(end,begin))
    if not(end or begin):
        return -1
    number = search_binary(list_db,num_search,begin,end)
    return number

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
    index = [index-1 for index in range(0,max_len,10)]
    index[0]+=1
    list_values = [list_db[code] for code in index]
    list_values = zip(list_values,index)
    return list_values

def search_binary(list_db,number,begin = 0,end = max_len -1):
    while begin <= end :
        find = int((begin + end) / 2)
        if list_db[find] == number:
            return find;
        if list_db[find] < number:
            begin = find + 1
        else:
            end = find - 1
    return -1,-1

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

    if answer == 2:
        insertion_sort(list_db)
        print("Sorted list :\n {}".format(list_db))

    if answer == 3:
        print("Write a number of your choise!\n")
        ans_1 = int(input())
        ans_2 = search_binary(list_db,ans_1)

        if ans_2 != -1:
            print("Found: {}\n".format(list_db[ans_2]))

        else:
            print("Don't find anything\n")

    if answer == 4:
        print("Write a number of your choise!\n")
        ans_1 = int(input())
        ans_2 = mix_search(list_db,ans_1)

        if ans_2 != -1:
            print("Found: {}\n".format(list_db[ans_2]))

        else:
            print("Don't find anything\n")




if __name__ == "__main__":

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
    answer = 10
    while answer > 0:
        print("Choose one of choises bellow:\n1-Print unorder list.\n2-Print order list.\n3-Find a number.\n4-Mix search\n0-Getout here.")
        answer = int(input())
        choise(answer,list_db)
        time.sleep(3)
        os.system("clear")
