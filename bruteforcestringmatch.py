__author__ = 'tk'

import random
import string
def bruteforcestringmatch(my_str,wan_str):
    wlen = len(wan_str)
    for i in xrange(0,len(my_str)-wlen,1):
        j = 0
        while j < wlen and wan_str[j] == my_str[i+j]:
            j = j+1
        if j == wlen:
            return i
    else:
        return -1


if __name__ == "__main__":
    test_str = "41kga34s3"
    want_str = "34s"
    print bruteforcestringmatch(test_str,want_str)
