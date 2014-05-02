__author__ = 'tk'
import random
def alpartition(my_str):

    signal = 0
    i = 0
    j = len(my_str)

    while i < j:
            if signal == 0 :
                while 1:
                    j = j - 1
                    if my_str[j] <= my_str[i]:
                        break
                signal = 1
            else:
                while 1:
                    i = i + 1
                    if my_str[j] <= my_str[i]:
                        break
                signal = 0
            # print my_str,i,j
            my_str[j],my_str[i] = my_str[i],my_str[j]
    my_str[j],my_str[i] = my_str[i],my_str[j]
    return i


def test(my_str):
    if len(my_str)>1:
        tick = alpartition(my_str)
        # print my_str,my_str[0:tick:],my_str[tick+1::],tick
        my_str[0:tick:]=test(my_str[0:tick:])
        my_str[tick+1::]=test(my_str[tick+1::])
    return my_str



a = random.sample(xrange(0,100),10)

print a

print test(a)
print sorted(a)

