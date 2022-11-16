integer_list = list(input("Enter a list of integers of your choice without any seperator(space,comma) : "))

lst1 = []
lst2 = []
temp = []
condi = True


def sumset(integer_list, condi):
    for i in range(0, len(integer_list) - 1):
        for j in range(i + 1, len(integer_list)):
            temp = integer_list.copy()
            temp.pop(i)
            temp.pop(j - 1)
            if int(integer_list[i]) + int(integer_list[j]) == sumset2(temp):
                condi = False
                sumset.lst1 = [integer_list[i], integer_list[j]]
                sumset.lst2 = temp
                print("The set 1 is :", sumset.lst1)
                print("The set 2 is :", sumset.lst2)
    return condi


def sumset2(temp):
    set2Val = 0
    for i in temp:
        set2Val = set2Val + int(i)
    return set2Val


valueee = sumset(integer_list, condi)
if valueee:
    print("Cannot be split with the given condition")
