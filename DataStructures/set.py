# Set
print("\n------------------Set---------------------")
my_set = {1,2,3,4}
print("my set -> ", my_set)
print("type of my set -> ", type(my_set))
print("length of my set -> ", len(my_set))

my_set.add(1);
print("my set after adding duplicate-> ", my_set)

copy_set = my_set.copy();
print("copy of my set-> ", copy_set)

my_set.pop();
print("my set after removing element-> ", my_set)
print("copy of my set after removing element from my list-> ", my_set)

