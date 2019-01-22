"""
sources:https://www.geeksforgeeks.org/md5-hash-python/
sources:https://github.com/jjhelmus/adventofcode/blob/master/day04.py
"""
import hashlib

def hashgetter(string,int_part):
    result = string+"".join(str(int_part))
    result = hashlib.md5(result.encode())
    result = result.hexdigest()
    if result[:6] == '000000':
        return True

    return False

def intchanger(string):
    for i in  range(10000000):
        if hashgetter(string,i) == True:
            return i
    return

if __name__ == '__main__':

    string = 'bgvyzdsv'

    print(intchanger(string))
