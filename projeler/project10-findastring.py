def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count +=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

'''
def count_substring(string, sub_string):
    length = len(string)
    length1 = len(sub_string)
    count = 0
    counter = 0

    for a in range(length):
        if string[a] == sub_string[0]:
            for i in range(length1):
                if a+i < length:
                    if string[a+i] == sub_string[i]:
                        counter +=1
        if counter == length1:
            counter = 0
            count +=1
        
    return count

'''

