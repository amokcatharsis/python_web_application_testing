files = {
    'cool_movie.avi': ['X'],
    'math_summary.docx': ['R', 'W'],
    'war_and_peace.txt': ['R', 'W', 'X']
}

actions = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}


def working_with_files(query):
    item = query.split()

    if actions[item[0]] in files[item[1]]:
        print('ОК')
    else:
        print('Access denied')
