import os


def count_lines_on_project(extension='.py'):
    walker = os.walk('./')
    banned = ['./.git', './build', './migrate', './dist', './venv']
    all_files = [[i[0], i[2]] for i in walker if not any([i[0].startswith(j) for j in banned]) and i[2]]
    count = 0
    files = []
    for i, cell in enumerate(all_files):
        temp = []
        for j in cell[1]:
            if j.endswith(extension):
                temp.append(j)
        if temp:
            path = all_files[i][0].replace('\\', '/')
            files.append([path, temp])
    for i in files[1:]:
        path = i[0]
        for file in i[1]:
            if file != 'Lines_Count.py':
                with open(f'{path}/{file}', 'r', encoding='utf-8') as f:
                    lines = [i for i in f.readlines() if i and i != '\n']
                    lines = [i for i in lines if not i.lstrip().startswith('#')]
                    count += len(lines)
    print(f'Counted lines of code (without python comments): {count}')


if __name__ == '__main__':
    count_lines_on_project()