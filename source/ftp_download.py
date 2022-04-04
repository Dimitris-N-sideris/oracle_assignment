from ftplib import FTP  # https://docs.python.org/3.9/library/ftplib.html


host = "ita.ee.lbl.gov"
directory = "traces"
file = "NASA_access_log_Aug95.gz"
path_location = '../testing_files/'

def retrieve_ftp_data(host, directory, file):
    # connect to host, default port
    ftp = FTP(host)
    ftp.login()  # user anonymous, passwd anonymous@
    # change  directory
    ftp.cwd(directory)
    #data = ftp.retrlines('LIST')           # list directory contents
    with open(path_location+file, "wb") as zipped_data:
        ftp.retrbinary("RETR " + file, zipped_data.write)

    ftp.quit()

retrieve_ftp_data(host, directory, file)
