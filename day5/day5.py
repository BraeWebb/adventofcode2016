import sys
import hashlib

def decode(code):
    index = 0
    password = ''
    while True:
        if hashlib.md5('{}{}'.format(code, index).encode()).hexdigest()[:5] == '00000':
            password = password + hashlib.md5('{}{}'.format(code, index).encode()).hexdigest()[5]
            if len(password) == 8:
                break
        index += 1
    return password

def advanced_decode(code):
    index = 0
    password = [None]*8
    while True:
        hexcode = hashlib.md5('{}{}'.format(code, index).encode()).hexdigest()
        if hexcode[:5] == '00000':
            if hexcode[5].isdigit():
                code_index = int(hexcode[5])
                if code_index < 8 and password[code_index] == None:
                    password[code_index] = hexcode[6]
                    if None not in password:
                        break
        index += 1
    return ''.join(password)

#print(decode('abc'))
#print(advanced_decode('abc'))

def run(stdin):
    code = stdin.readline()
    print(decode(code))
    print(advanced_decode(code))

if __name__ == "__main__":
    run(sys.stdin)
