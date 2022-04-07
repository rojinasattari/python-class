'''
for  i in range(10):
    for j in range(10-(i+1)):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print("") 
'''
'''
          *
         ***
        *****
       *******
      *********
     ***********
'''

'''
for i in range(10):
    for j in range(10-(i+1)):
        print(" ", end="")
    for j in range(i*2+1):
        print("*", end="")
    print("")
'''

'''
for i in range(10):
    for j in range(i):
        print(" ", end="")
    for j in range(((9-i)*2)+1):
        print("*", end="")
    print("")
'''
'''
for i in range(19):
    if i >= 10:
        m = 20 - (i + 2);
        n = (i - 9) * 2 + 1;
    else:
        m = i;
        n = (10 - (i + 1)) * 2 + 1;

    for j in range(m):
        print(" ", end="")
    for j in range(n):
        print("*", end="")
    print("")
'''
'''
import math

for i in range(30):
    for j in range(int(math.sqrt(30-i)*10)):
        print(" ", end="")
    print("*")
    |
'''
'''
import math

for i in range(30):

    y=int(math.sin(i/30*2*math.pi)*30)+30
       
    if y >= 30:
        space_count_1 = 30 
        for j in range(space_count_1-1):
            print(" ", end="")
        if(y != 30):
            print("|", end="")
        for j in range(y-space_count_1):
            print(" ", end="")
        print("*")
    else:
        for j in range(y):
            print(" ", end="")
        print("*", end="")
        for j in range(30-(y+2)):
            print(" ", end="")
        print("|")
'''

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 
