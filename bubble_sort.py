__author__ = 'tk'
import random

def sort_selection(my_list):
    for j in xrange(0,len(my_list)-1,1):
        for i in xrange(0,len(my_list)-1-j,1):
            if my_list[i] > my_list[i+1]:
                my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
    return my_list



if __name__ == "__main__":
    tk_list = random.sample(xrange(1000),10)
    print "my_list" + str(tk_list)
    print sort_selection(tk_list)
    print sorted(tk_list)