my_llist = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0

while count < len(my_llist):
    num = my_llist[count]
    count = count + 1
    if num == 0:
        continue
    elif num < 0:
        break
    elif count == len(my_llist):
        print(num)
    else:
        print(num)
