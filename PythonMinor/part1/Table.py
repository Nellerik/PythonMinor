tableData = [['apples', 'oranges', 'cherries', 'bannana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData[0])
for l in tableData:
    for s in range(len(l)):
        if len(l[s]) > colWidths[s]:
            colWidths[s] = len(l[s])

for l in tableData:
    for s in range(len(l)):
        print(l[s].rjust(colWidths[s] + 2), end='')
    print();