from itertools import groupby  # https://docs.python.org/3/library/gzip.html
from optparse import OptionParser
import numpy as np
import pandas as pd
#import logging 

file = "../testing_files/NASA_access_log_Aug95.gz"


# 6) Option Parsing
parser = OptionParser()
parser.add_option('-m','--mode', action='store', type='string'  ,dest='flag')
(options, args) = parser.parse_args()

#logging.basicConfig(filename='log.txt', filemode='w', format ='%(message)s')


#https://httpd.apache.org/docs/2.4/logs.html


def create_df(file):
    log_header = ['host', 'identity', 'userid', 'date', 'timezone', 'request', 'status', 'size']

    df = pd.read_csv(
        file,
        header=None,
        index_col=None,
        names = log_header,
        sep=" ",
        quotechar='"',
        parse_dates= True,
        on_bad_lines="warn",
        encoding="unicode_escape",
    )
    # fix and merge date into a column  eg '[DD/MM/YYYY:HH:MM:SS , -04:00]' -> 'DD/MM/YYYY:HH:MM:SS -04:00'
    df['date'] = df['date'].str[1:] +   df['timezone'].str[:-1] 
    del df['timezone']
    #print( df.head())
    #print(df.dtypes)
    return df

def top_requests(df):
    return df.groupby('request').request.count().reset_index(name = '# requests').sort_values('# requests', ascending = False)

def successful_requests(df):
    return  df[(df['status'] >= 200) & (df['status'] < 400)]
   
def failed_requests(df):
    return df[(df['status'] < 200) | (df['status'] >= 400)]
   
def top_failed_request(failed_df):
    return failed_df.groupby('request').request.count().reset_index(name = '# requests').sort_values('# requests', ascending = False)

def top_hosts(df):
    return df.groupby('host').host.count().reset_index(name = '# requests').sort_values('# requests', ascending = False)


def get_percentage(df_sub, df_full):
    return (df_sub.shape[0] / df_full.shape[0])*100
 
# 1) top #10 requests 

def top_10_requests(df):
    df_top = top_requests(df)
    return str(df_top.head(10))+'\n'


# 2) successful requests
def percentage_success_requests(df):
    df_successful_requests = successful_requests(df)
    return f'Successful Requests percentage: {get_percentage(df_successful_requests,df):0.2f} %\n' 

# 3) failed requests

def percentage_failed_requests(df):
    df_failed_requests = failed_requests(df)
    return f'Failed Requests percentage: {get_percentage(df_failed_requests,df):0.2f} %\n'

# 4) top 10 failed requests

def top_10_failed_requests(df):
        
    df_failed_requests =  failed_requests(df)
    df_failed_requests = top_failed_request(df_failed_requests)
    return str(df_failed_requests.head(10))+'\n'


# 5) top 10 hosts with most request showing ip address, number of requests
def top_10_hosts(df):
    df_top_hosts = top_hosts(df)
    return str(df_top_hosts.head(10))+'\n'


# 7) top 10 hosts with most request showing ip address, number of requests
def top_10_hosts_with_top_requests(df):
    df_top_hosts = top_hosts(df)
    output = ''
    for row in df_top_hosts.head(10).itertuples():
        output += f'Host: {row.host} \n'
        top_five_requests = df[df['host'] == row.host ].groupby('request').request.count().reset_index(name = '# requests').sort_values('# requests', ascending = False)
        output += str(top_five_requests.head(5)) + '\n'
    return output


def oracle_task():
    df = create_df(file)
    output = ''
    if(options.flag == 'top10'):
        output += top_10_requests(df)
    elif(options.flag == 'successPercent'):
        output += percentage_success_requests(df)
    elif(options.flag == 'failedPercent'):
        output += percentage_failed_requests(df)
    elif(options.flag == 'top10failed'):
        output += top_10_failed_requests(df)
    elif(options.flag == 'top10hosts'):
        output += top_10_hosts(df)
    else: 
        output += top_10_requests(df) 
        output += percentage_success_requests(df)
        output += percentage_failed_requests(df)
        output += top_10_failed_requests(df)
        output += top_10_hosts(df)
    #logging.
    output += top_10_hosts_with_top_requests(df)

    return output


