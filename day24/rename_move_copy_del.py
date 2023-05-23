folder_path = "C:\\Users\\ACER\\Desktop\\Practice"

# for i in range(1, 6):
#     fp = open(f"{folder_path}\\file{i}.py", "w")
#     fp.close()

import os
import shutil

os.chdir(folder_path)
# print(os.listdir())

# for count, file in enumerate(os.listdir(), start=1):
#     name, ext = os.path.splitext(file)
#     new_name = f"test{count}{ext}"
#     os.rename(file, new_name)


# if not os.path.exists("data"):
#     os.mkdir("data")
#
#
# for file in os.listdir():
#     if file in "data":
#         continue
#     # shutil.move(file, "data")
#     shutil.copy(file, "data")


os.remove("data/file1.py")
# os.rmdir("data")  # deletes the empty folder
shutil.rmtree("data")   # deletes folder and all the files recursively
