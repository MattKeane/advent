class Directory():
    def __init__(self, parent):
        self.parent = parent
        self.sub_directories = {}
        self.files = {}

    def __repr__(self):
        return str(self.sub_directories | self.files)
        
    def mkdir(self, name):
        sub_directory = Directory(self)
        self.sub_directories[name] = sub_directory

    def touch(self, size, name):
        self.files[name] = int(size)

    def get_size(self):
        total = 0
        for _, directory in self.sub_directories.items():
            total += directory.get_size()
        for _, size in self.files.items():
            total += size
        return total

    def size_of_all_below(self, max):
        total = 0
        size = self.get_size()
        if size <= max:
            total += size
        for _, directory in self.sub_directories.items():
            total += directory.size_of_all_below(max)
        return total

with open('input.txt', 'r') as data:
    lines = data.read().split('\n')
    root = Directory(None)
    pwd = root
    i = 0
    while i < len(lines):
        line = lines[i]
        # if the line is a command
        if line[0] == '$':
            command = line.split(' ')[1:]
            # if the command is cd
            if command[0] == 'cd':
                if command[1] == '/':
                    pwd = root
                elif command[1] == '..':
                    pwd = pwd.parent
                else:
                    pwd = pwd.sub_directories[command[1]]
                i += 1
            elif command[0] == 'ls':
                i += 1
                while i < len(lines):
                    output = lines[i].split(' ')
                    if output[0] == '$':
                        break
                    if output[0] == 'dir':
                        pwd.mkdir(output[1])
                    else:
                        pwd.touch(output[0], output[1])
                    i += 1
    print(root.size_of_all_below(100000))