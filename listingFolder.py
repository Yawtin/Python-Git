import os

folders = input("Please input folders separated by spaces: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"{folder} is not valid")
        continue

    for file in files:
        print(file)