import os


def count_lines_on_project():
    walker = os.walk('./')
    all_files = [[i[0], i[2]] for i in walker if not i[0].startswith('./.git') and not i[0].startswith('./build')
                 and not i[0].startswith('./dist') and not i[0].startswith('./venv') and i[2]]
    count = 0
    py_files = []
    for i, cell in enumerate(all_files):
        temp = []
        for j in cell[1]:
            if j[-3:] == '.py':
                temp.append(j)
        if temp:
            path = all_files[i][0].replace('\\', '/')
            py_files.append([path, temp])
    for i in py_files[1:]:
        path = i[0]
        for file in i[1]:
            if file != 'Lines_Count.py':
                with open(f'{path}/{file}', 'r', encoding='utf-8') as f:
                    lines = [i for i in f.readlines() if i and i != '\n']
                    lines = [i for i in lines if not i.lstrip().startswith('#')]
                    count += len(lines)
    print(f'Counted lines of code (.py only, without comments): {count}')
