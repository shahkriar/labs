import os
def ex1(): 
    path = str(input("Input the path: "))# путь к директории 
    print("Directories:")  # Выводим заголовок "Directories:"
    for dir in os.listdir(path): # бeгаем по всем элементам в указонной директории 
        if os.path.isdir(os.path.join(path, dir)): # Проверяем является ли текущий элемент директорией
            print(dir)  # Выводим имя директории
            
    print("Files:")  # Выводим заголовок "Files:"
    for file in os.listdir(path): # перебираем все элементы 
        if os.path.isfile(os.path.join(path, file)):  #проверяем является ли текущий элемент файлом
            print(file) # выводим имя файла 
    print("All:")  # Выводим заголовок "All:"
    for all in os.listdir(path):  # Перебираем все элементы в указанной директории
        print(all) # Выводим все элементы, включая и директории, и файлы

def ex2():
    path = str(input('Input the path: '))
    if os.path.exists(path):# check is the path exists
        print('The path exists')
        read = os.access(path, os.R_OK)# check is the readble
        if read:
            print('The file is readable')
        else:
            print('The file is not readable')
        write = os.access(path, os.W_OK)# check is the writable 
        if write:
            print('The file is writable')
        else:
            print('The file is not writable')
        exe = os.access(path, os.X_OK)#is the executable
        if exe:
            print('The file is executable')
        else:
            print('The file is not executable')
    else:
        print('The path does not exist')

def ex3():
    path = str(input('Input the path: '))
    if os.path.exists(path):# check is the exists
        print('The path exists')
        path_name = os.path.basename(path)#get the basename of the file 
        path_dir = os.path.dirname(path)#get directory name of the file 
        print('File name is: ', path_name)
        print('File path is: ', path_dir)
    else:
        print('The path does not exists')
      
def ex4():#number of lines in the text format  
    path = input("Input the path: ")
    with open(path, 'r') as f:
        lines = f.readlines()
        print('Number of lines in ', len(lines))
        

def ex5():
    path = str(input("Input the path: "))
    with open(path, 'w') as file:
        list = [1, 2, 3, 4, 5, 6, 7, 8]
        file.write('\n'.join(list)) # converts each integer in the list to a string
        
def ex6(): # generate 26 text files named A.txt, B.txt, and so on
    for letter in "abcdefghijklmnopqrstuvwxyz":
        filename = letter + '.txt'
        with open(filename, 'w') as file:
            file.write(letter)

def ex7():# copy the contents of a file to another file
    path = str(input("Input the path: "))
    new_path = str(input("Input the new path: "))
    with open(path, 'rb') as file:
        write = file.read()
    with open(new_path, 'ab') as new_file:
        new_file.write(write)
        

def ex8():#delete file by specified path. Before deleting check for access and  existing
    path = str(input("Input the path: "))
    if os.path.exists(path):
        if os.access(path, os.X_OK):# check for executability
            os.remove(path)
            print('The file have been deleted')
        else:
            print('This file is not accessiable')
    else:
        print('The file does not exist')

ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
ex8()



    
    