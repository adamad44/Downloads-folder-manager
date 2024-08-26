import os
import time


downloadsDirectory = "/Users/adamjanzir/Downloads"




image_extensions = [
    "jpeg", "jpg", "png", "gif", "bmp", "tiff", "ico", "webp", "svg", "raw", "heif", "avif", "heic"
]

document_extensions = [
    "pdf", "docx", "doc", "xlsx", "xls", "pptx", "ppt", "txt", "rtf", "odt", "ods", "odp",
    "epub", "mobi", "pages", "key"
]

video_extensions = [
    "mp4", "avi", "mov", "mkv", "wmv", "flv", "webm", "mpeg", "mpg", "3gp", "rm", "rmvb",
    "ts", "m4v", "svi", "ogv"
]

audio_extensions = [
    "mp3", "wav", "aac", "flac", "ogg", "m4a", "wma", "alac", "aiff", "opus", "mka"
]

archive_extensions = [
    "zip", "rar", "tar", "gz", "7z", "bz2", "xz", "iso", "cab", "lzma", "arj", "z", "ace"
]

script_extensions = [
    "py", "js", "html", "css", "php", "rb", "pl", "sh", "bat", "ts", "coffee", "lua", "go"
]

executable_extensions = [
    "exe", "dll", "bin", "bat", "sh", "app", "out", "jar", "cgi", "run"
]

spreadsheet_extensions = [
    "xlsx", "xls", "csv", "tsv", "ods", "numbers"
]

presentation_extensions = [
    "pptx", "ppt", "key", "odp"
]

app_downloads = ["dmg", "pkg", ".app"]

torrent_extensions = [".torrent"]






fileTypeFolderList = ["images", "docs", "videos", "audios", "archives", "scripts", "executables", "spreadsheets", "presentations", "DMG-installers", "torrents", "OTHERS", "FOLDERS"]




try:
    fileList = os.listdir(downloadsDirectory)
    
except FileNotFoundError as e:
    print("no such file or directory, check spelling of directory")
    exit()


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

def get_directories(fileList, base_path):
    
    for item in fileList:
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path):
            directoriesWithFileTypes.append(item)

        if os.path.isdir(item_path) and (item_path.split("/")[-1]) not in fileTypeFolderList:

            directories.append(item)
    
    return directories, directoriesWithFileTypes
    





def sortFiles():

    for file in fileList:
        if file not in directoriesWithFileTypes:
                
            for extension in image_extensions:
                if (file.lower()).endswith(extension):
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/images/{file}")

            for extension in document_extensions:
                if (file.lower()).endswith(extension):
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/docs/{file}")

            for extension in video_extensions:
                if (file.lower()).endswith(extension):
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/videos/{file}")

            for extension in audio_extensions:
                if (file.lower()).endswith(extension):
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/audios/{file}")       

            for extension in archive_extensions:
                if (file.lower()).endswith(extension):
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/archives/{file}")

            for extension in script_extensions:
                if (file.lower()).endswith(extension):
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/scripts/{file}") 
        
            for extension in executable_extensions:
                if (file.lower()).endswith(extension):
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/executables/{file}")

            for extension in spreadsheet_extensions:
                if (file.lower()).endswith(extension):
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/spreadsheets/{file}")

            for extension in presentation_extensions:
                if (file.lower()).endswith(extension):
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/presentations/{file}")
            
            for extension in app_downloads:
                if (file.lower()).endswith(extension):
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/DMG-installers/{file}")

            for extension in torrent_extensions:
                if (file.lower()).endswith(extension):
                    os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/torrents/{file}")
    for file in os.listdir(downloadsDirectory):
        if file not in directoriesWithFileTypes:
            os.rename(f"{downloadsDirectory}/{file}", f"{downloadsDirectory}/OTHERS/{file}")


    
    for folder in directories:
        os.rename(f"{downloadsDirectory}/{folder}", f"{downloadsDirectory}/FOLDERS/{folder}")

checkDownloadDirForFolders()
get_directories(fileList, downloadsDirectory)

for i in range(200):
    sortFiles()


print("done sorting files")