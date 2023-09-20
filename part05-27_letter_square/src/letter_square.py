# Write your solution here
import math

# dictionary = {}
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
# index = 0
# for number in numbers:
#     dictionary[number] = letters[index]
#     index += 1


layers = int(input("Layers: "))






# counter = 0
# print(f"{dictionary[layers]*(layers+layers-1)}")


# highest_letter = letters[layers - 1] # D
# highest_letter_idx = layers - 1

# inverse_pyramid_range = (list(range(layers-1, -1, -1)) + list(range(1, layers)))

# for lowest_letter_idx in inverse_pyramid_range: # changes from 3 to 0 and then form 1 to 3
#     lowest_letter_in_row = letters[lowest_letter_idx]
#     # first half of the row
#     letter_counter = 0
#     while letter_counter < layers:
#         curr_letter_idx = max(highest_letter_idx - letter_counter, lowest_letter_idx)
#         print(letters[curr_letter_idx], end="")
#         letter_counter += 1
#     # second half of the row
#     letter_counter = layers - 2
#     while letter_counter >= 0:
#         curr_letter_idx = max(highest_letter_idx - letter_counter, lowest_letter_idx)
#         print(letters[curr_letter_idx], end="")
#         letter_counter -= 1
#     print()




highest_letter_idx = layers - 1 # index of D

lowest_letter_idx_for_each_row = (list(range(highest_letter_idx, -1, -1)) + list(range(1, highest_letter_idx + 1))) # length is layers * 2 - 1
letter_idx_for_middle_row = list(range(0, highest_letter_idx + 1)) + list(range(highest_letter_idx - 1, -1, -1)) # length is layers * 2 - 1

for lowest_letter_idx_on_this_row in lowest_letter_idx_for_each_row: # changes from 3 to 0 and then form 1 to 3
    for letter_idx_if_on_middle_row in letter_idx_for_middle_row:
        real_letter_idx = max(highest_letter_idx - letter_idx_if_on_middle_row, lowest_letter_idx_on_this_row)
        print(letters[real_letter_idx], end="")
    print()










    # if counter == layers//2:
    #     print(f"{dictionary[layers] + letters[1]*(layers//2) + letters[0]*1 + letters[1]*(layers//2)+ dictionary[layers]}")
    # else: 
    #     print(f"{dictionary[layers] + dictionary[layers-1]*((layers*2)-3) + dictionary[layers]}")
    # counter += 1
#print(f"{dictionary[layers]*(layers+layers-1)}")

    

    