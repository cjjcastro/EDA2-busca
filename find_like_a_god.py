""" Python version 3.6.3 """
from random import randint
import os
import time
import timeit
max_len = 100

def mix_search(list_db,num_search):
    tic = timeit.default_timer()
    insertion_sort(list_db)
    toc = timeit.default_timer()
    print("-------------------------------------------------")
    print("| Time insertion_sort: {}    |".format(toc-tic))
    print("-------------------------------------------------")
    tic = timeit.default_timer()
    list_index = index_list(list_db)
    toc = timeit.default_timer()
    print("| Time index_list: {}        |".format(toc-tic))
    print("----------------------------------------------------------")
    tic = timeit.default_timer()
    end , begin = sequencial_search(num_search,list_index)
    toc = timeit.default_timer()
    print("| Time sequencial_search in index_list: {} |".format(toc-tic))
    print("---------------------------------------------------------------")
    print("| Sub set list_db end: {} begin: {}              |".format(end,begin))
    print("-------------------------------------------------")
    if not(end or begin):
        return -1
    tic = timeit.default_timer()
    number = search_binary(list_db , num_search, begin, end)
    toc = timeit.default_timer()
    print("| Time search_binary: {}     |".format(toc-tic))
    print("-------------------------------------------------")
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
    index.append(max_len-1)
    index[0]+=1
    list_values = [list_db[code] for code in index]
    list_values = list(zip(list_values,index))
    return list_values

def sequencial_search(num_search,list_num):
    count = 0
    for item in list_num:
        if item[0] >= num_search:
            if item[1] == 0:
                return 9,0
            return item[1] , list_num[count-1][1]
        count+=1
    return -1,-1

def search_binary(list_db,number,begin = 0,end = max_len -1):
    while begin <= end :
        find = int((begin + end) / 2)
        if list_db[find] == number:
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

    if answer == 2:
        insertion_sort(list_db)
        print("Sorted list :\n {}".format(list_db))

    if answer == 3:
        print("Write a number of your choise!\n")
        ans_1 = int(input())
        tic = timeit.default_timer()
        ans_2 = search_binary(list_db,ans_1)
        toc = timeit.default_timer()
        if ans_2 != -1:
            print("Found: {} in time: {}".format(list_db[ans_2],toc-tic))

        else:
            print("Don't find anything\n")

    if answer == 4:
        print("Write a number of your choise!\n")
        ans_1 = int(input())
        tic = timeit.default_timer()
        ans_2 = mix_search(list_db,ans_1)
        toc = timeit.default_timer()
        if ans_2 != -1:
            print("Found: {} in time: {}".format(list_db[ans_2],toc-tic))

        else:
            print("Don't find anything\n")




if __name__ == "__main__":

    path = os.path.dirname(os.path.abspath(__file__))
    new_path = os.path.join(path,"db.txt")
    try:
        db = open(new_path,"r")
    except:
        db = open("db.txt","w+")
        for count in range(0,max_len):
            number = randint(0,99999)
            db.write("%d \n" %(number))
        db.close()
    db = open(new_path,"r")
    list_db = init_list(db)
    answer = 10
    while answer > 0:
        print("Choose one of choises bellow:\n1-Print unorder list.\n2-Print order list.\n3-Binary search.\n4-Mix search\n0-Getout here.")
        answer = int(input())
        choise(answer,list_db)
        print("Press enter to continue!!!")        
        try:
            input()
        except:
            print("You are in python2 please press enter again !!!")
            raw_input()
        #time.sleep(3)
        os.system("clear")
