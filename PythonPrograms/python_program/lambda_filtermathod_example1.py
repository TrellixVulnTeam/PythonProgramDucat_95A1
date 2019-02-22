# filter mathod in lambda python   ==  even number in list ..??
# syntax ==>>   filter(function_object , iterable_object)

a = [5,4,8,45,52,12,13,100,51]
add = lambda x:x%2 ==0
b = filter(add,a)
print(list(b))


# new mathod of expression python expression in python ==   odd number in list ..??

x = [5,4,8,45,52,12,13,100,51]
add = lambda x : x%2 == 1
b = filter(add,a)
print(list(b))



# new mathod of expression python expression in python   ==    list print ..??

x = [5,4,8,45,52,12,13,100,51]
add = lambda x : x-1
b = filter(add,a)
print(list(b))



'''
output ==

[4, 8, 52, 12, 100]
[5, 45, 13, 51]
[5, 4, 8, 45, 52, 12, 13, 100, 51]

'''