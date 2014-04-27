import random

def sort_selection(my_list):
    for i1 in xrange(0,len(my_list)-1,1):
        min_loc = i1
        for j1 in xrange(i1+1,len(my_list),1):
            if my_list[j1] < my_list[min_loc]:
                min_loc = j1
        my_list[i1],my_list[min_loc] = my_list[min_loc],my_list[i1]
    return my_list


if __name__ == "__main__":

    tk_list = random.sample(xrange(1000),10)
    print "my_list" + str(tk_list)
    print sort_selection(tk_list)
    print sorted(tk_list)