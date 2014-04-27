__author__ = 'tk'

import random

def merge(test1,test2):
    i , j , k = 0 , 0 , 0
    arr = []
    lens1 = len(test1)
    lens2 = len(test2)
    while i<lens1 and j<lens2:
        if test1[i] < test2[j]:
            arr.append(test1[i])
            i = i+1
        else:
            arr.append(test2[j])
            j = j +1
    if i==lens1:
        arr.extend(test2[j::])
    else:
        arr.extend(test1[i::])
    return arr

def mergesort(my_list):
    if len(my_list) > 1:
        blist = my_list[0:len(my_list)/2:1]
        clist = my_list[len(my_list)/2::1]
        bsorted = mergesort(blist)
        csorted = mergesort(clist)
        return merge(bsorted,csorted)
    else:
        return my_list

if __name__ == "__main__":
    tk_list = random.sample(xrange(1000),10)
    print "my_list" + str(tk_list)
    print mergesort(tk_list)
    print sorted(tk_list)

