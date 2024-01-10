with open('filename.txt', 'r') as file:
    for line in file:
        if 'search_string' in line:
            print(line);