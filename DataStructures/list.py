# List
print("------------------List---------------------")
my_list = []
my_list.append(1)
my_list.append("string")
print("my list -> ", my_list)
print("type of my list -> ", type(my_list))
print("length of my list -> ", len(my_list))

## List comprehension
print("\n------------------List Comprehension---------------------")

###filters
print("\n------------------List Comprehension - Filters ---------------------")

number_list = list(range(10))
filtered_list = [item for item in number_list if item % 2 == 0]
print('Filtered list : ', filtered_list)


###functions
print("\n------------------List Comprehension - functions ---------------------")

my_string = 'this is my list which is created for examples'

def format_word(word):
    return word.upper()

formatted_list = [format_word(item) for item in my_string.split()]
print('formatted_list-->',formatted_list)
