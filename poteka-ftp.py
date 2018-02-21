import os
import ftplib
ftpServer = ftplib.FTP(host ="ftp.poteka.jp", user="vlf", passwd="skr7e5zP", timeout=None, source_address=("ftp.poteka.jp",201))
ftpServer.retrlines("LIST")
dirList = []
ftpServer.retrlines("LIST", dirList.append)
str = dirList[0].split(None, 8)
filename = str[-1].lstrip()
print("Dowloading File :: ",filename)
localPath = os.path.join(r"D:\SATREPS\Data", filename)
file = open(localPath, "wb")
ftpServer.retrbinary("RETR " + filename, file.write, 8*1024)
file.close()
print("Done !!")
print("Please check your downloded file : D:\SATREPS\Data")
