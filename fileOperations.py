def fileOperations(file_path, key, value):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path,"w") as file:
        for line in lines:
            if key in line:
                file.write(key + "for " + value + "\n")
            else:
                file.write(line)

fileOperations("server.txt", "e ", "elephant")
