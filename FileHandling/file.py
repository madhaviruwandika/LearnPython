my_file = open('files','r')

for line in my_file.readlines():
    print(line.strip())


my_file = open('files','a')
my_file.write("\nI'm editing the file now")

my_file = open('files_new','w')
my_file.write("This is a new line")

