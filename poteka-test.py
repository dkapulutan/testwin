from ftplib import FTP
filename = 'event_00064920_201801152203.csv'
files = list()
with FTP("www.poteka.jp") as ftp:
    ftp.login("vlf", "skr7e5zP")
    #ftp.dir()
    ftp.dir(files.append)
    print(len(files), 'files in the directory.')
    #ftp.retrlines('LIST')
    #ftp.retrbinary('RETR event_00064920_201801152203.csv', open('event_00064920_201801152203.csv', 'wb').write)
    #ftp.retrbinary('data_00064920_20180109.csv', open('data_00064920_20180109.csv', 'wb').write)
    ftp.retrbinary('RETR' + filename, open(filename, 'wb').write)
