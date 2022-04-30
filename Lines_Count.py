import os


def count_lines_on_project(extension='.py', ret_val='str'):
    walker = os.walk('./')
    banned = ['./.git', './build', './migrations', './dist', './venv']
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
    # print(files)
    for i in files:
        path = i[0]
        for file in i[1]:
            if file != 'line_counter.py':
                with open(f'{path}/{file}', 'r', encoding='utf-8') as f:
                    lines = [i for i in f.read().split('\n') if i and i != '\n']
                    lines = [i for i in lines if not i.lstrip().startswith('#')]
                    count += len(lines)
    if ret_val == "str":
        return f'Counted lines of code (without python comments): {count}'
    elif ret_val == 'int':
        return count
    return count


if __name__ == '__main__':
    print('total (html, css, js, py):', count_lines_on_project('.py', ret_val='int') +
          count_lines_on_project('.js', ret_val='int') +
          count_lines_on_project('.css', ret_val='int') +
          count_lines_on_project('.html', ret_val='int'), 'lines')