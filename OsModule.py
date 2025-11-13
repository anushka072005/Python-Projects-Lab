import os
import shutil

# check if dir already exist
# if(not os.path.exists("data")):
#     os.mkdir("data")

# create 100 dir inside data dir
# for i in range(0,100)    :
#     os.mkdir(f"data/Day{i+1}")

# rename dir name
# for i in range(0,100)    :
#     os.rename(f"data/Day{i+1}" , f"data/Totorial {i+1}")

# listdir() is used to list all files and folders present inside a directory.
# folders = os.listdir("data")

# print(folders)

# for folder in folders:    # only folders
#     print(folder)

# for folder in folders:    # with file
#     print(folder)
#     print(os.listdir(f"data/{folder}"))

# getcwd() prints path 
# print(os.getcwd(), "THIS IS PATH")

# chdir() change dir 
# os.chdir("/Users")
# print(os.getcwd())

# DELETE SINGLE FOLDER
# folder_path = r"C:\Users\hp\OneDrive\Desktop\PYTHON\data\Totorial 10"

# shutil.rmtree(folder_path)
# print("Folder deleted successfully!")


# DELETE ALL FOLDERS
# # Directory where the folders are
# parent_dir = r"C:\Users\hp\OneDrive\Desktop\PYTHON\data"

# # List everything in the directory
# for item in os.listdir(parent_dir):
#     item_path = os.path.join(parent_dir, item)
    
#     # Check if it is a folder
#     if os.path.isdir(item_path):
#         shutil.rmtree(item_path)   # delete folder and all its contents
#         print(f"Deleted folder: {item_path}")


# /DELETE DATA FOLDER
# folder_path = r"C:\Users\hp\OneDrive\Desktop\PYTHON\data"
# # Only works if folder is empty
# os.rmdir(folder_path)
# print("Folder deleted successfully!")


# print(os.getcwd())
# folder_path = r"C:\Users\hp\Desktop\TestFolder"
# os.makedirs(folder_path, exist_ok=True)
# os.chdir(folder_path)
# print(os.getcwd())
# print(os.listdir())
# os.mkdir("Anu")
# os.makedirs(r"C:\Users\hp\Desktop\TestFolder\Nested\SubNested", exist_ok=True)

# file_path = r"C:\Users\hp\OneDrive\Desktop\PYTHON\Anu\file.md"
# os.remove(file_path)
# print("file deleted successfully")

# empty_folder = r"C:\Users\hp\OneDrive\Desktop\PYTHON\Anu"
# os.rmdir(empty_folder)
# print("folder deleted successfully")

# folder_with_file = r"C:\Users\hp\OneDrive\Desktop\PYTHON\chu"
# shutil.rmtree(folder_with_file)
# print("fileNDfolder deleted successfully")

# Check if file/folder exists
# print(os.path.exists(r"C:\Users\hp\OneDrive\Desktop\PYTHON"))

# Checks type: file or folder.
# print(os.path.isfile(r"C:\Users\hp\OneDrive\Desktop\PYTHON"))
# print(os.path.isfile(r"C:\Users\hp\OneDrive\Desktop\PYTHON\my3.py"))
# print(os.path.isdir(r"C:\Users\hp\OneDrive\Desktop\PYTHON"))

# Join path folder+file
# folder = r"C:\Users\hp\OneDrive\Desktop\PYTHON"
# file = r"C:\Users\hp\OneDrive\Desktop\PYTHON\my3.py"
# print(os.path.join(folder, file))


# os.rename() – Rename file/folder
# oldname = r"C:\Users\hp\OneDrive\Desktop\PYTHON\Tuples.py"
# newname = r"C:\Users\hp\OneDrive\Desktop\PYTHON\Tuple.py"
# os.rename(oldname, newname)
# print("renamed successfully")


# os.environ → gives access to your system environment variables.
# print(os.environ["USERNAME"])
# print(os.environ["USERPROFILE"])
# print(os.environ["HOMEPATH"])
# print(os.environ["TEMP"])
# print(os.environ["PATH"])
# print(os.environ["COMPUTERNAME"])


os.system("dir")
