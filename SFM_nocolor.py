# Simulated File System Stored in Memory
# Created by Raymond Lind

# Main Class
class Files:
    def __init__(self, father, name):
        self.father = father
        self.name = name
        self.directory = []  # Directory list
        self.file = []  # File list

# Configure Home Directory & Path Management
home = Files(father=None, name='home')
current = home

# Name input to give user specialized experience
entry = input('Please give me your name before entering the File System: ')
print('\nHey {}, welcome to the File System!'.format(entry) + '\nType help for more information.\n')
path = entry + '@Avanan:'

# Function to create a file
def touch(name):
    global current
    current.file.append({name: ''})

#Function to create a directory
def mkdir(name):
    global current
    directory = Files(father=current, name=name)
    current.directory.append(directory)

# Function to change into new directory
def cd(name):
    global current, path
    if name == '..':
        if current.father is not None:
            path = path[:(len(path) - len(current.name)) - 1]
            current = current.father
    else:
        for i in current.directory:
            if i.name == name:
                current = i
                path = path + '/' + name
                return
        return print('Directory does not exist')

# Function to list files and directories
def ls():
    global current
    for i in current.file:
        for key, value in i.items():
            print(key, value)
    for i in current.directory:
        print(i.name)

# Main loop simulating a file system with commands
if __name__ == '__main__':
    while True:
        print(path, end=' --> ')
        command = input().split(' ')

        # Creates touch command capability in loop
        if command[0] == 'touch':
            try:
                for files in current.file:
                    for key in files:
                        if command[1] == key:
                            print("Timestamp for " + command[
                                1] + " has been updated.")
                            current.file.remove(files)
                touch(command[1])
            except:  # Error handling in touch requests
                print('--------------\nError in usage\n--------------\nTry: touch FileName\n')

        # Creates mkdir command capability in loop
        elif command[0] == 'mkdir':
            try:
                for dirs in current.directory:
                    if command[1] == dirs.name:
                        print("This directory name already exists. Try a different name.")
                        current.directory.remove(dirs)
                mkdir(command[1])
            except: # Error handling in mkdir requests
                print('--------------\nError in usage\n--------------\nTry: mkdir DirectoryName\n')

        # Creates cd command capability in loop
        elif command[0] == 'cd':
            try:
                cd(command[1])
            except: # Error handling in cd requests
                print('--------------\nError in usage\n--------------\nTry: cd DirectoryName\n')

        # Creates ls command capability in loop
        elif command[0] == 'ls':
            ls()

        # Creates help command capability in loop
        elif command[0] == 'help':
            print('---------------\nCOMMAND OPTIONS\n---------------')
            print('mkdir ~ Create Directory\ntouch ~ Create Empty File\nls ~ List Directories & Files in Current Directory\n'
                  'cd ~ Open Directory\nexit ~ Exit File System\nusage ~ Shows how to use commands\n')

        # Creates usage command capability in loop
        elif command[0] == 'usage':
            print('-------------\nCOMMAND USAGE\n-------------')
            print('usage = usage\nls = ls\nmkdir = mkdir NEW_DIRECTORY_NAME\ntouch = touch NEW_FILE_NAME\ncd = cd DIRECTORY_NAME\nexit = exit\n')

        # Creates exit command capability in loop
        elif command[0] == 'exit':
            positive = input('Are you sure you want to exit?\nyes|no: ')
            if positive == 'yes': # Exits file system
                exit()
            elif positive == 'no': # Returns you to loop
                print('Okay, going back to File System... \n')
            else: # Returns to loop if no answer defined
                print('\nyes or no not specified, returning you to File System... \n')

        else: # Displays this if command does not exist
            print('----------------------')
            print('{} is not a command'.format(command[0]))
            print('----------------------')

# END
