import time, os
from Crypto.Cipher import AES

def clear():
    os.system("cls")

clear()
usersdir = str(input(f"Enter DIR u wish to recover >> "))
key = KEY_HERE


def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)
    os.remove(file_name)



def main():
    listOfFiles = list()
    file_input = usersdir
    if os.path.exists(file_input):
        if file_input !="":
            if os.path.isfile(file_input)==False:
                    for (dirpath, dirnames, filenames) in os.walk(file_input):
                        EXCLUDE_DIRECTORY = (
                            #Mac/Linux system directory
                            '/usr',  
                            '/Library/',
                            '/System',
                            '/Applications',
                            '.Trash',
                            #Windows system directory
                            'Program Files',
                            'Program Files (x86)',
                            'Windows',
                            '$Recycle.Bin',
                            'AppData',
                            'logs',
                        )
                        if any(s in dirpath for s in EXCLUDE_DIRECTORY):
                            pass
                        else:
                            listOfFiles += [os.path.join(dirpath, file) for file in filenames]
                            for l in listOfFiles:
                                EXTENSIONSS = (
                                    '.enc',
                                )
                                if l.endswith(EXTENSIONSS):
                                    decrypt_file(l, key)
                                else:
                                    pass
            else:
                decrypt_file(file_input, key)    
            print(f"\n\nDecrypted DIR {usersdir}\n\nYour Files are back to normal!")
            input("Press enter to continue. . .")
            main()
        else:                             
            print(f"Please enter a DIR!")
            input("Press enter to continue. . .")
            main()
    else: 
        print(f"DIR does not exist!")
        input("Press enter to continue. . .")
        main()



clear()
main()
