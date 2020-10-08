with open(r'C:\Users\User\PycharmProjects\pythonProject\steam_description_data.csv',encoding='utf-8') as f:
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    s = ''
    p = ''
    for i in f:
        for j in i:
            a += 1
            if j == ' ':
                b += 1
            if j.isalnum() == 1:
                c += 1
            if s.isalnum() == 1 and (j == ' ' or j == '.' or j == ',' or j == '!' or j == '?'):
                d += 1
            s = j
            if j != '.' and j != '!' and j != '?':
                p += j
            elif p != '':
                e += 1
                p = ''
print(a)
print(a - b)
print(c + b)
print(d)
print(e)