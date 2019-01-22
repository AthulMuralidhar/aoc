"""
sources:https://www.geeksforgeeks.org/md5-hash-python/
"""
import hashlib

def hashgetter(string,int_part):
    result = string+"".join(str(i) for i in int_part)
    result = hashlib.md5(result.encode())
    result = result.hexdigest()
    if result[:5] == '00000':
        return True

    return False

def intchanger(string,int_part):
    for i in  range(-1,-9,-1):
        while int_part[-i-1] <= 9:
            if hashgetter(string,int_part) == True:
                print(hashgetter(string,int_part))
                return int_part
            elif hashgetter(string,int_part) == False:
                int_part[-i-1] +=1

if __name__ == '__main__':

    string = 'bgvyzdsv'
    int_part = [0,0,0,0,0,0,0,0]

    print(intchanger(string,int_part))
