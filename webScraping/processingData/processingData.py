file_path = '../webPage.txt'
with open(file_path, 'r') as file:
    next(file)
    next(file)
    next(file)
    count = 0
    search_group = "Computer Science"
    for line in file:
        parts = line.strip().split(',')
        group = parts[0]
        nameAndCode = parts[1]
        link = parts[2]
        if (group == search_group):
            count += 1
            print(line)
    print(f'Found {count} classes')

