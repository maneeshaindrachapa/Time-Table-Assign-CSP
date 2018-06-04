import copy
#csv comma seperate values ,without using csv module

def inputData(fileName):
    with open(fileName, 'r') as fileOb:
        text = fileOb.read()
        lines = text.split('\n')
        data = []; #subject details and rooms as array
        for line in lines:
            data.append(line.split(','))
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
    category = subs[depth][1]                   #compulsory or optional, c|o
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
            if (slots[slot] == -1):             #if slot is empty
                assignment[depth] = [sub, slot, rooms[0]] #assign sub,slot and first room to assignment
                slots[slot] = [rooms[0]]        #update slots(dictionary) with room_no(str)
                if (backtracking(assignment, slots, depth+1)):
                    return True                 #remaining slots and rooms are enough for lower level
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

inputDetails = inputData('input.csv')

subs = inputDetails[:-1]    #3d array - sub_name,type,available_slots
rooms = inputDetails[-1]    #array - room names
slots = {}                  #dictionary - key is slot_name, when c sub assigned value is room_name, when o sub assigned value is array of room_names
assignment = []             #3d array - sub_name,assigned_slot,room_name per each row

for sub in subs:
    for slot in sub[2:]:
        if (slot not in slots):
            slots[slot] = -1
    assignment.append([sub[0],-1,-1])

result = backtracking(assignment, slots, 0)

if (result):
    outputData('output.csv', assignment)
    print "\n"
    for sub in assignment:
       print sub
