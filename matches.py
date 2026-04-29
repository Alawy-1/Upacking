clubs = {
    '00000': "Al-Nassr",
    '00001': "Al-Hilal",
    '00010': "Al-Ahli",
    '00011': "Al-Qadsiah",
    '00100': "Al-Taawoun",
    '00101': "Al-Ittihad",
    '00110': "Al-Ettifaq",
    '00111': "NEOM_SC",
    '01000': "Al-Hazm",
    '01001': "Al-Khaleej",
    '01010': "Al-Feiha",
    '01011': "Al-Fateh",
    '01100': "Al-Shabab",
    '01101': "Al-Kholood",
    '01110': "Damac_FC",
    '01111': "Riyadh",
    '10000': "Al-Akhdoud",
    '10001': "Al-Najma",
}

value = input("Please enter a hex number: ")
value = int(value, 16)
print(hex(value))

value = bin(value)

value = value[2:].zfill(16)
print(value)

if value[0] == '0':
    r = 'Local Refree'
    #print("local Refree") for my info (anything commented was for me to follow the code)
else: 
    r = 'Global Refree'
    #print("Global Refree") 

match value[1:3]:
    case '00':
        g = 'league cup'
        #print('league cup')
    case '01':
        g = 'king cup'
        #print('king cup')
    case '10':
        g = 'prince cup'
        #print('prince cup')
    case '11':
        g = 'super cup'
        #print('super cup')
    case _:
        print('unkown cup')

if value[3] == '0':
    field = f'{clubs[value[11:16]]} field'
    #print('team1 field')
else:
    field = f'{clubs[value[6:11]]} field'
    #print('team2 field')

match value[4:6]:
    case '00':
        s = 'draw'
        #print('Draw')
    case '01':
        s = f'Team {clubs[value[11:16]]} won'
        #print('Team 1 winning')
    case '10':
        s = f'Team {clubs[value[6:11]]} won'
        #print('Team 2 winning')
    case '11':
        s = 'Cancelled match'
        #print('Cancelled match')
    case _:
        print('unkown command')

if value[6:11] not in clubs:
    print("club not available")
else:
    T2 = clubs[value[6:11]]
    T1 = clubs[value[11:16]]
    #print(T1 + '\n' + T2)

#print(value)

print('Details about the match:')
print('The', g ,'match is between', T1, 'and', T2 + '.', r + '.', 'It was in', field + '.', s + '.')
