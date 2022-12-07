import fileinput

def dirsize(dirs, metadata_list):
    total_size = 0
    for m in metadata_list:
        if m[0] == 0: # dir
            total_size += dirsize(dirs, dirs[m[1]])
        else:
            total_size += m[2]
    return total_size

def parse_lines(lines):
    # dict dirpath -> [(type, name, size)]
    #   where dirpath: full path as a string
    #         type: 0 for dir, 1 for file
    #         name: name of dir or file
    #         size: file size (if dir, then 0)
    dirs = {}
    curpath = []
    for l in lines:
        tokens = l.split(' ')
        is_command = (tokens[0] == '$')
        if is_command:
            if tokens[1] == 'cd':
                if tokens[2] == '/':
                    curpath = ['/']
                elif tokens[2] == '..':
                    curpath.pop()
                else:
                    curpath.append(tokens[2])
            else:
                assert(tokens[1] == 'ls')
                # nothing special to do here
        else: # output of ls
            curpathstr = '/'.join(curpath)
            if curpathstr not in dirs:
                dirs[curpathstr] = []
            if tokens[0] == 'dir':
                dirname = tokens[1]
                metadata = (0, curpathstr + '/' + dirname, 0)
                dirs[curpathstr].append(metadata)
            else: # file
                size = int(tokens[0])
                filename = tokens[1]
                metadata = (1, filename, size)
                dirs[curpathstr].append(metadata)

    # part 1
    part1_ans = 0
    dirsizes = {}
    for k,v in dirs.items():
        # print(k, dirsize(dirs, v))
        size = dirsize(dirs, v)
        dirsizes[k] = size
        if size < 100000:
            part1_ans += size
    print(part1_ans)

    # part 2
    total = 70000000
    used = dirsizes['/']
    remaining = total - used
    to_free = 30000000 - remaining
    best_dir_size = total
    for size in dirsizes.values():
        if size > to_free:
            best_dir_size = min(best_dir_size, size)
    print(best_dir_size)


lines = [l.rstrip() for l in fileinput.input()]
parse_lines(lines)
