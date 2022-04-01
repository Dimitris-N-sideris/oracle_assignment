from ast import Try
from ftplib import FTP  # https://docs.python.org/3.9/library/ftplib.html
import gzip  # https://docs.python.org/3/library/gzip.html
import numpy as np
import pandas as pd

host = "ita.ee.lbl.gov"
directory = "traces"
file = "NASA_access_log_Aug95.gz"


def retrieve_ftp_data(host, directory, file):
    # connect to host, default port
    ftp = FTP(host)
    ftp.login()  # user anonymous, passwd anonymous@
    # change  directory
    ftp.cwd(directory)
    data = ftp.retrlines('LIST')           # list directory contents
    print(data)
    with open(file, "wb") as zipped_data:
        ftp.retrbinary("RETR " + file, zipped_data.write)

    ftp.quit()

#https://httpd.apache.org/docs/2.4/logs.html
log_header = ['host', 'identity', 'userid', 'date', 'request', 'status', 'size']
# retrieve_ftp_data(host, directory, file)
df = pd.read_csv(
    file,
    header=None,
    names = log_header,
    sep=" ",
    quotechar='"',
    on_bad_lines="warn",
    encoding="unicode_escape",
)
print(df.head())
request_group = df.groupby('request').request.count().reset_index(name = '# requests')

print(request_group.sort_values('# requests').head())
print(request_group.sort_values('# requests', ascending = False).head(10))

"""with gzip.open(file, 'rt') as unzip_data:
    log_file = unzip_data.readlines()
    
for line in log_file:        
    line.strip() 
    fields = line.split(' ')"""

# print(fields)
# df = pd.read_csv(file,header=0, sep='-', quotechar='"')
# print(df.head())
#
# - [17/Aug/1995:11:44:14 - 0400] "GET /shuttle/missions/sts-69/sts-69-patch-small.gif HTTP/1.0" 200 8083\norion.htl-bw.ch -c
header = ["site", "nothing", "nothing", "date", "request", "code", "Number"]
"""
b'in24.inetnebr.com - - [01/Aug/1995:00:00:01 -0400] "GET /shuttle/missions/sts-68/news/sts-68-mcc-05.txt HTTP/1.0" 200 1839\n'
128.158.31.201 - - [17/Aug/1995:11:42:35 -0400] "GET /shuttle/technology/sts-newsref/sts-lcc.html HTTP/1.0" 200 32252\n
- [17/Aug/1995:11:42:36 -0400] "GET /images/launch-logo.gif HTTP/1.0" 200 1713\n134.68.213.83 - 
- [17/Aug/1995:11:42:37 -0400] "GET /history/early-astronauts.txt HTTP/1.0" 200 3850\n128.159.143.202 - 
- [17/Aug/1995:11:42:38 -0400] "GET /shuttle/missions/sts-68/ksc-srl-image.html HTTP/1.0" 200 1404\n128.158.31.201 -
"""
