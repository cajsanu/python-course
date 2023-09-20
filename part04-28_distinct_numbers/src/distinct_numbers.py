# Write your solution here

def distinct_numbers (lst: list):
    index = 0
    d_list = []
    while index < len(lst)-1:
        new_lst = sorted(lst)
        if new_lst[index] == new_lst[index + 1]:
            index += 1
            continue
        else: 
            d_list.append(new_lst[index])
            index += 1
    d_list.append(new_lst[-1])
    return d_list

if __name__ == "__main__":
    mylist = [2,2,5,6,4,6,7,3,3,2]
    result = distinct_numbers(mylist)
    print(result)
 
# model solution
# def distinct_numbers(my_list: list):
#     results = []
#     for item in my_list:
#         if item not in results:
#             results.append(item)
 
#     results.sort()
#     return results