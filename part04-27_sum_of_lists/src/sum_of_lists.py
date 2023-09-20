# Write your solution here

def list_sum (a:list, b:list):
    index = 0
    list = []
    while index < len(a):
       sum = a[index] + b[index]
       list.append(sum)
       index += 1
    return list


if __name__ == "__main__":
    list1 = [6,5,8,2]
    list2 = [6,7,4,10]
    result = list_sum(list1, list2)
    print(result)





       
       
