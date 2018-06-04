import copy

def inputData(fileName):
    with open(fileName, 'r') as fileOb:
        text = fileOb.read()
        lines = text.split('\n')
        data = [];          #subject details and rooms 3d array
        for line in lines:
            data.append(line.split(','))
        print data
        return data

def outputData(fileName, data):
    dataStr = ""
    for row in data:
        rowStr = ""
        for col in row:
            rowStr += col + ','
        else:
            rowStr = rowStr[:-1]
        dataStr += rowStr + '\n'
    else:
        dataStr = dataStr[:-1]
    with open(fileName, 'w') as fileOb:
        fileOb.write(dataStr)
