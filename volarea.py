
#!/usr/bin/python3

import math
def main():
    #vol = eval(input("Enter the Volume: "))
    radius = eval(input("Enter the Radius: "))
    #area = eval(input("Enter the Area: "))

    volume = 4/3 * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2
    print(" This is the Volume: ", volume)
    print(" This is the Area: ", area)

main()
