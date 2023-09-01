# File-Manager-Using-Python
Aim of this project is to develope a file manager, which can perform operations like opening a file, copying it, renaming, moving, and deleting. Also, we will include options for making and deleting a folder. Along with listing all the files present in the folder and organising based on the extensions.

![Screenshot 2023-09-01 114412](https://github.com/sricharan959/File-Manager-Using-Python/assets/115167414/9c513635-0f84-4df1-8a5d-f7f1465a2ea7)
## Operations
### 1. Rename Multiple Files
Python comes with a built-in function, rename(), as part of the os library. As the name implies, the function is used to rename a file. Before diving into how practical examples, let’s take a look at what makes up the function, including its various parameters. I have combined the function with a loop to rename multiple files at once.
### 2. Move Multiple Files
Python shutil module offers several functions to perform high-level operations on files and collections of files. We can move files using the shutil.move() method.
The shutil.move() function is a dedicated function for moving files. Because of this, it tends to be my preferred method of moving files. This is because it makes it clear that the intention of your code is to move a file, rather than rename it. In order to move multiple files with Python, we can actually simply use a for loop to iterate over a list of files. In this way, we actually move one file at a time, but use the for loop to repeat this for all files in a folder.
### 3. Copy Multiple Files
The shutil.copy() function is a dedicated function for copying files. Because of this, it tends to be my preferred method of copying files. This is because it makes it clear that the intention of your code is to copy a file, rather than rename it. In order to copy multiple files with Python, I used a for loop to iterate over a list of files. In this way, we actually copy one file at a time, but use the for loop to repeat this for all files in a folder.
### 4. Remove Directory and File
Python uses the os.rmdir() function to delete empty directories. In this scenario, the required directory must be empty; else, an OSError would be raised. If the directory doesn't exist, the FileNOtFoundError is thrown.
I deleted the required directory and its contents from system using the shutil.rmtree() function. Therefore, to remove a directory tree, use the shutil module.

## Organising various types of files
There are often times when we feel that the computer we are working on is cluttered with files. You barely have time to organize those files and even find it difficult to find a particular file right when you need it. Even the file explorer comes with a file search functionality but who remembers the names of the file for a longer time. LOL!!!
In this project, I am going to share a code walkthrough of how you can create your own automated file organizer service in just few minutes. Let's dig into it.
