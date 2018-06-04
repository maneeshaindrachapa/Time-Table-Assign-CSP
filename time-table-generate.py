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

def backtracking(assignment, slots, depth):
    if (depth == len(assignment)):              #depth is the index of each row of 3d arrays, pointer to current subject
        return True                             #every row of assignement is assigned with room,slot
    global subs
    global rooms  
    sub = subs[depth][0]                        #subject name                       
    available = subs[depth][2:]                 #array - available time slots for subject
    category = subs[depth][1]                   #compulsory or optional
    if (category == "c"):                       #always select empty time slot and assign                      
        for slot in available:
            if (slots[slot] == -1):             #if slot is empty
                assignment[depth] = [sub, slot, rooms[0]]       #assign sub,slot and first room to assignement (to current subject in assignment)
                slots[slot] = rooms[0]                          #update slots (dictionary) with room_no (str)
                if (backtracking(assignment, slots, depth+1)):
                    return True                 #remaining slots and rooms are enough for lower level
                else:
                    slots[slot] = -1                    #if not - remove assigned values
                    assignment[depth] = [sub, -1, -1]   #remove assigned values
        else:
            return False                        #cannot continue with any of available slots, combinations used so far are not wrong
        
    elif (category == "o"):                     #select empty slot or slot with optional subjects
        for slot in available:
            if (slots[slot] == -1):
                assignment[depth] = [sub, slot, rooms[0]]
                slots[slot] = [rooms[0]]
                if (backtracking(assignment, slots, depth+1)):
                    return True
                else:
                    slots[slot] = -1
                    assignment[depth] = [sub, -1, -1]
            elif (type(slots[slot]) == list):
                asRooms = slots[slot]
                temp = asRooms[:]
                if (len(asRooms) == len(rooms)):
                    continue
                asRooms.append(rooms[len(asRooms)])
                assignment[depth] = [sub, slot, asRooms[-1]]
                slots[slot] = asRooms
                if (backtracking(assignment, slots, depth+1)):
                    return True
                else:
                    slots[slot] = temp
                    assignment[depth] = [sub, -1, -1]
        else:
            return False
