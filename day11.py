

# file handling

# modes

# r - road
# w - write
# a - append
# x -create

# file = open("studentslist.txt","x")

# file = open("studentslist.txt","w")

# file.write("Roopan")

# file.close()

# autoclose

# with open("studentslist.txt","w") as file:
#     file.write("joel")

# students = ["Roopan\n", "joal\n", "hari\n"]

# with open("studentslist.txt","w") as file:
#     file.writelines(students)

# with open("studentslist.txt","a") as file:
#     file.write("priya")

# with open("studentslist.txt","r") as file:
#     print(file.read())
#     print(file.readline())
#     print(file.readline(4))
#     print(file.readlines())

# with open("studentslist.txt","r") as file:
#     line = file.readlines()

# print("Before line", line)

# line.insert(3, "vasanthi\n")

# print("After line", line)

# with open("studentslist.txt","w") as file:
#     file.writelines(lines)


# file pointer

# with open("studentslist.txt", "r") as file:
#     print(file.read(2))
#     file.seek(2)
#     print(file.read())
#     print(file.tell())


# with open("file.txt", "r") as file:
#     file.read(2) 
#     current_pos = file.tell()
#     remaining_content = file.read() 
#     print(f"I am at position: {current_pos}")
#     print(f"Remaining text is: '{remaining_content}'")


# with open("studentslist.txt", "w", encoding="utf-8") as file:
#     file.write("யோகேஷ்")



# with open("studentslist.txt", "w", encoding="utf-8") as file:
#     file.write("😂")

