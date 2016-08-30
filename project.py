import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import urllib2
import datetime

stox = 'AAPL', 'GOOGL', 'MSFT' , 'AMZN' , 'EBAY'



def fetchdata(stock):
    filename = stock+'.txt'
    x = urllib2.urlopen("http://chartapi.finance.yahoo.com/instrument/1.0/"+stock+"/chartdata;type=quote;range=1d/csv")
    val = x.read()
    splitsrc = val.split('\n')

    for each in splitsrc:
        splitline = each.split(',')
        if len(splitline) == 6:
            if 'values' not in each:
                 f = open(filename,'a')
                 line = each+'\n' 
                 f.write(line)
                 f.close()
    print"Fetched from ", stock 

    
def graph(stock) :
    filename = stock+'.txt'
    timestamp,close,high,low,_open,volume = np.loadtxt(filename,unpack = True , delimiter=',' , converters={0:lambda ts : datetime.datetime.fromtimestamp(ts)})
    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,4), (0,0), rowspan=40, colspan=40)
    plt.title(stock)
    plt.xlabel("Date")
    plt.ylabel("Rate")
    ax1.plot(date,close)
    ax1.plot(date,_open)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y%m%d%H%M%S'))	
    
    print "The Graph for "+stock+"is being plotted"

    plt.grid(True)
    plt.show()

for each in stox:
    fetchdata(each)
    graph(each)


