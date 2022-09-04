def commanddivide(com):
    l = com.split(" ")
    if len(l) == 3:
        command = l[0]
        a = int(l[1])
        b = int(l[2])
    elif len(l) ==2:
        command = l[0]
        a = int(l[1])
        b=0
    else:
        command = l[0]
        a=0
        b=0
    
    return command, a, b

N = int(input())


list = []


for i in range(N):
    com = input()
    command, a, b = commanddivide(com)
    
    
    if command == "insert":
        list.insert(a, b)

    elif command == "print" :
        print(list)

    elif command == "remove":
        list.remove(a)

    elif command == "append":     
        list.append(a)

    elif command == "sort":
        list.sort()

    elif command == "pop":
        list.pop()

    elif command == "reverse":
        list.reverse()
    
    else:
        print("There is no this command")