import os
import time

#please enter your downloads directory
downloadsDirectory = "/Users/adamjanzir/Downloads"


#dictionary of extensions and their respective folders
extension_dict = {
    "images": [
        "jpeg", "jpg", "png", "gif", "bmp", "tiff", "ico", "webp", "svg", "raw", "heif", "avif", "heic"
    ],
    "docs": [
        "pdf", "docx", "doc", "xlsx", "xls", "pptx", "ppt", "txt", "rtf", "odt", "ods", "odp",
        "epub", "mobi", "pages", "key"
    ],
    "videos": [
        "mp4", "avi", "mov", "mkv", "wmv", "flv", "webm", "mpeg", "mpg", "3gp", "rm", "rmvb",
        "ts", "m4v", "svi", "ogv"
    ],
    "audios": [
        "mp3", "wav", "aac", "flac", "ogg", "m4a", "wma", "alac", "aiff", "opus", "mka"
    ],
    "archives": [
        "zip", "rar", "tar", "gz", "7z", "bz2", "xz", "iso", "cab", "lzma", "arj", "z", "ace"
    ],
    "scripts": [
        "py", "js", "html", "css", "php", "rb", "pl", "sh", "bat", "ts", "coffee", "lua", "go"
    ],
    "executables": [
        "exe", "dll", "bin", "bat", "sh", "app", "out", "jar", "cgi", "run"
    ],
    "spreadsheets": [
        "xlsx", "xls", "csv", "tsv", "ods", "numbers"
    ],
    "presentations": [
        "pptx", "ppt", "key", "odp"
    ],
    "DMG-installers": [
        "dmg", "pkg", ".app"
    ],
    "torrents": [
        ".torrent"
    ]
}

#list of folders to be created
fileTypeFolderList = ["images", "docs", "videos", "audios", "archives", "scripts", "executables", "spreadsheets", "presentations", "DMG-installers", "torrents", "OTHERS", "FOLDERS"]


try:
    fileList = os.listdir(downloadsDirectory)
    
except FileNotFoundError as e:
    print("no such file or directory, check spelling of directory")
    exit()


#check if folders exist, if not create them
def checkDownloadDirForFolders():
    workingDir = os.getcwd()
    os.chdir(downloadsDirectory)
    
    for name in fileTypeFolderList:
        if os.path.exists(f"{str(downloadsDirectory)}/{name}") == False:
            os.mkdir(f"{str(downloadsDirectory)}/{name}")
            print(f"written: {name}")
    
    os.chdir(workingDir)



global directories 
global directoriesWithFileTypes
directories = []
directoriesWithFileTypes = []

#check if file is a directory
def get_directories(fileList, base_path):
    
    for item in fileList:
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path):
            directoriesWithFileTypes.append(item)

        if os.path.isdir(item_path) and (item_path.split("/")[-1]) not in fileTypeFolderList:

            directories.append(item)
    
    return directories, directoriesWithFileTypes

#sort files into their respective folders
def sortFiles():
    for file in fileList:
        if file not in directoriesWithFileTypes:
            file_extension = file.split(".")[-1].lower()
            for folder, extensions in extension_dict.items():
                if file_extension in extensions:
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/{folder}/{file}")
                    break

    for file in os.listdir(downloadsDirectory):
        if file not in directoriesWithFileTypes:
            os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/OTHERS/{file}")
    
    for folder in directories:
        os.rename(f"{downloadsDirectory}/{folder}", f"{downloadsDirectory}/FOLDERS/{folder}")


checkDownloadDirForFolders()
get_directories(fileList, downloadsDirectory)

#sort files 200 times to ensure all files are sorted as some files are not sorted on the first run
for i in range(200):
    sortFiles()


print("done sorting files")