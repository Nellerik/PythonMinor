tableData = [['apples', 'oranges', 'cherries', 'bannana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData[0])
for i in tableData:
    for j in range(len(i)):
        if len(i[j]) > colWidths[j]:
            colWidths[j] = len(i[j])

for i in tableData:
    for j in range(len(i)):
        print(i[j].rjust(colWidths[j] + 2), end='')
    print();