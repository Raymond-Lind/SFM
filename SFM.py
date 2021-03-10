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

# Colors for customization
yellow = '\033[93m'
red = '\033[91m'
blue =  '\u001b[34m'
green = '\033[92m'
reset = '\033[0m'

# Name input to give user specialized experience
entry = input('Please give me your name before entering the File System: ')
print(blue + '\nHey {}, welcome to the File System!'.format(entry) + reset + '\nType' + green + ' help' + reset + ' for more information.\n')
path = blue + entry + '@FileSystem:' + reset

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
        return print(red + 'Directory does not exist' + reset)

# Function to list files and directories
def ls():
    global current
    for i in current.file:
        for key, value in i.items():
            print(key, value)
    for i in current.directory:
        print(green + i.name + reset)

# Main loop simulating a file system with commands
if __name__ == '__main__':
    while True:
        print(path, end=red + ' --> ' + reset)
        command = input().split(' ')

        # Creates touch command capability in loop
        if command[0] == 'touch':
            try:
                for files in current.file:
                    for key in files:
                        if command[1] == key:
                            print(green + "Timestamp for " + reset + red + command[1] + reset + green + " has been updated." + reset)
                            current.file.remove(files)
                touch(command[1])
            except: # Error handling in touch requests
                print(red + '--------------\nError in usage\n-------------- ' + reset + '\nTry: ' + red + 'touch' + reset + ' FileName\n')

        # Creates mkdir command capability in loop
        elif command[0] == 'mkdir':
            try:
                for dirs in current.directory:
                    if command[1] == dirs.name:
                        print(red + "This directory name already exists. Try a different name." + reset)
                        current.directory.remove(dirs)
                mkdir(command[1])
            except: # Error handling in mkdir requests
                print(red + '--------------\nError in usage\n-------------- ' + reset + '\nTry: ' + red + 'mkdir' + reset + ' DirectoryName\n')

        # Creates cd command capability in loop
        elif command[0] == 'cd':
            try:
                cd(command[1])
            except: # Error handling in cd requests
                print(red + '--------------\nError in usage\n-------------- ' + reset + '\nTry: ' + red + 'cd' + reset + ' DirectoryName\n')

        # Creates ls command capability in loop
        elif command[0] == 'ls':
            ls()

        # Creates help command capability in loop
        elif command[0] == 'help':
            print('---------------\n' + red + 'COMMAND OPTIONS' + reset + '\n---------------')
            print(red + 'mkdir' + reset + ' ~ Create Directory\n' + red + 'touch' + reset + ' ~ Create Empty File\n'
                  + red + 'ls' + reset + ' ~ List Directories & Files in Current Directory\n' + red +
                  'cd' + reset + ' ~ Open Directory\n' + red + 'exit' + reset + ' ~ Exit File System\n'
                  + red + 'usage' + reset + ' ~ Shows how to use commands\n')

        # Creates usage command capability in loop
        elif command[0] == 'usage':
            print('-------------\n' + red + 'COMMAND USAGE' + reset + '\n-------------')
            print(red + 'usage' + reset + ' = ' + red + 'usage\nls' + reset + ' = ' + red + 'ls\n' + red +
                  'mkdir' + reset + ' = ' + red + 'mkdir' + reset + ' NEW_DIRECTORY_NAME\n' + red +
                  'touch' + reset + ' = ' + red + 'touch' + reset + ' NEW_FILE_NAME\n' + red +
                  'cd' + reset + ' = ' + red + 'cd' + reset + ' DIRECTORY_NAME\n' + red + 'exit' +
                  reset + ' = ' + red + 'exit\n' + reset)

        # Creates exit command capability in loop
        elif command[0] == 'exit':
            positive = input(yellow + 'Are you sure you want to exit?\nyes|no: ' + reset)
            if positive == 'yes': # Exits file system
                exit()
            elif positive == 'no': # Returns you to loop
                print(yellow + 'Okay, going back to File System... \n' + reset)
            else: # Returns to loop if no answer defined
                print(red + '\nyes or no not specified, returning you to File System... \n' + reset)

        else: # Displays this if command does not exist
            print(red + '----------------------')
            print('{} is not a command'.format(command[0]))
            print('----------------------' + reset)

# END
