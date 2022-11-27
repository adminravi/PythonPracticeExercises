#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

list = []
for i in range(2000, 3201):
    #check if i is divisible by 7 and not divisible by 5
    if i%7 == 0 and i%5 != 0:
        #print(i, end=",")
        list.append(str(i))

#The join() method takes all items in an iterable and joins them into one string.
#A string must be specified as the separator.
print(','.join(list))


