ivan = {
    'name': 'ivan',
    'age': 34,
    'children': [{
        'name': 'vasja',
        'age': 12,
    }, {
        'name': 'petja',
        'age': 15,
    }],
}

darja = {
    'name': 'darja',
    'age': 41,
    'children': [{
        'name': 'kirill',
        'age': 21,
    }, {
        'name': 'pavel',
        'age': 15,
    }],
}

emps = [ivan, darja]

def Children_Are_Adult (arr):
    adults = []
    for worker in arr:
        try:
            for child in worker['children']:
                if child['age'] >= 18:
                    adults.append(worker['name'])
                    break
        except KeyError:
            print ('Dictionary key error!')
    return adults

print (Children_Are_Adult(emps))