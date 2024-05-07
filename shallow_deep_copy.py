# https://www.youtube.com/watch?v=naG4uXpmVAU
import copy 

numbers = [1, 2, 3, 4, 5]
new_numbers = numbers

new_numbers[2] = 33

print('Numbers list', numbers)
print('Id of numbers', id(numbers))

print('new Numbers list', new_numbers)
print('Id of new numbers', id(new_numbers))

# shallow copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# shallow copy create a copy of the object 
# but references each element of the object
new_list = copy.copy(old_list)
new_list[0][2] = 'b'
print("===shallow copy ===")

print(old_list)
print(new_list)

# deep copy

# deep copy creates a copy of the object and the elements of the object
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.deepcopy(old_list)
new_list[0][2] = 'b'
print("===deep copy ===")
print(old_list)
print(new_list)