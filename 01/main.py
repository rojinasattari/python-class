n = 5 # interpreter allocates 32bits of memory to save the value 3 in it.
print(hex(id(n))) # id is a function which returns the address of passed parameter variable.
print(n)
m = 4
print(hex(id(m)))
print(m)


print(list(range(10)))

for i in range(10):
    if m > i :
        print("M is greater than i")
    elif n > i :
        print("N is greater than i")
    else :
        print("I is greater than both")

s = m + n

print(hex(id(s)))
print(s)

print(int(10)) # 10
print(str(10)) # '10'
print(float(10)) # 10.0

age = 10
print("Arash is 0x%x" %(age))

'''
You can use A-Z,a-z,_,0-9 for variable names
You can not use 0-9 for fisrt character of variable names.
'-' character is not allowed for variable names.
'''
_salam = "salam"
salam_chetori = "salam chetori"
salam = "salam"
salam3 = "salam 3"
Salam_chetori4 = "salam"


x = y = z = 4
print(x + y + z)

x, y, z = 2, 3, 4
print(x + y + z)

my_array = ["apple", "banana", "orange"]
x, y , z =  my_array
print(x + " " + y + " " + z)

arash = "bye"
def sample_func():
    global arash
    arash = "salam"
    return arash
sample_func()
print (arash)
