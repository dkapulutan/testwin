from ftplib import FTP
import sys
import ftplib
import os
import fnmatch
import io
import csv

#filename = 'event_00064920_201801150041.csv'
#files = list()
dl = list()
fmatch = 'data_00064920_20180128.csv'
#fmatch = 'event_00064919_*.csv'
with FTP("www.poteka.jp") as ftp:
    ftp.login("vlf", "skr7e5zP")

    for fname in ftp.nlst(fmatch):
        if fname not in dl:
            fhandle = open(fname,'wb')
            print('Getting ' + fname)
            ftp.retrbinary('RETR ' + fname, fhandle.write)
            fhandle.close()
            dl.append(fname)
    ftp.quit()

print('Downloaded:', len(dl), ' files')

for fname in dl:
    fhandle = open (fname)
    bio = io.BytesIO()
    bio.seek(0)
    csv_data = csv.DictReader(io.TextIOWrapper(bio, newline=None), delimiter=',')
    for row in csv_data:
        print(row)
