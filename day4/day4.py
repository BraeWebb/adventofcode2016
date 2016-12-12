ALPHABET = list('abcdefghijklmnopqrstuvwxyz')

def is_real_room(encrypted_name, checksum):
    encrypted_name = list(filter(lambda x: not x.isdigit() and x != '-', encrypted_name))
    occurrences = {letter: encrypted_name.count(letter) for letter in set(encrypted_name)}
    occurrences = [x[0] for x in sorted(occurrences.items(), key=lambda x: (-x[1], x[0]))]
    return ''.join(occurrences[:5]) == checksum

def split_sector(sector):
    return sector.split('[', 1)[0], sector.split('[', 1)[1].split(']')[0]

def get_reals(rooms):
    return list(filter(lambda x: is_real_room(*x), rooms)), list(filter(lambda x: not is_real_room(*x), rooms))

def split_room(room):
    return '-'.join(room[0].split('-')[:-1]), int(room[0].split('-')[-1])

def sum_sectors(rooms):
    room_list = []
    for room in rooms:
        room_list.append(split_sector(room))
    real_rooms = get_reals(room_list)[0]
    return sum(split_room(room)[1] for room in real_rooms)

def decode_sector(sector):
    room_id, code = split_room(split_sector(sector))
    decode = ''
    for letter in room_id:
        if letter == '-':
            decode = decode + '-'
        else:
            decode = decode + ALPHABET[(ALPHABET.index(letter) + code) % 26]
    return decode, code

#print(is_real_room('aaaaa-bbb-z-y-x-123', 'abxyz'))
#print(is_real_room('a-b-c-d-e-f-g-h-987', 'abcde'))
#print(is_real_room('not-a-real-room-404', 'oarel'))
#print(is_real_room('totally-real-room-200', 'decoy'))

#print(decode_sector('qzmt-zixmtkozy-ivhz-343[sadw]'))

with open('inputs.txt') as f:
    print(sum_sectors(f.read().splitlines()))
    f.seek(0)
    for room in f:
        print(*decode_sector(room))