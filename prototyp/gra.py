# table = [[1, 2, 3, 4, 5, 6]
#          [7, 8, 9, 10, 11, 12]
#          [13, 14, 15, 16, 17, 18]
#          [19, 20, 21, 22, 23, 24]
#          [25, 26, 27, 28, 29, 30]
#          [31, 32, 33, 34, 35, 36]]
game_on = True:
while game_on == True:
    tables = [['[]', '[]', '[]', '[]', '[]', '[]'],
            ['[]', '[]', '[]', '[]', '[]', '[]'],
            ['[]', '[]', '[]', '[]', '[]', '[]'],
            ['[]', '[]', '[]', '[]', '[]', '[]'],
            ['[]', '[]', '[]', '[]', '[]', '[]'],
            ['[]', '[]', '[]', '[]', '[]', '[]']]

    for table in tables:
        print(table)
    print('Orders Turn')
    move = tuple(input('Insert your move: (x/o), y, x '))
    new_table = []
    for i, element in enumerate(tables):
        if i != int(move[1]):
            new_table.append(tables[i])
        else:
            new_element = []
            for n, tile in enumerate(element):
                if n == int(move[2]):
                    new_element.append(f'[{move[0]}]')
                else:
                    new_element.append(element[n])
            new_table.append(new_element)

    for table in new_table:
        print(table)
                    


