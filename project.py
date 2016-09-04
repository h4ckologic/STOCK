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
    timestamp,close,high,low,_open,volume = np.loadtxt(filename, dtype='O,'+'f8,'*5, delimiter=',', unpack=True, converters={0: lambda d: datetime.datetime.fromtimestamp(float(d))})

    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,4), (0,0), rowspan=40, colspan=40)

    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)


    plt.title(stock)
    plt.xlabel("Time")
    plt.ylabel("Rate")
    ax1.plot(timestamp, low, color='orange', label ='low')
    ax1.plot(timestamp, high, color='green', label ='high')
    ax1.plot(timestamp, _open, color='black', label ='open')
    ax1.plot(timestamp, close,color='blue', label ='close')
    fill = 'red'
    fille = 'green'
    ax1.fill_between(timestamp, high, high[0], where=(high < high[0]), facecolor=fill, edgecolor=fill,alpha = 0.5)
    ax1.fill_between(timestamp, high, high[0], where=(high > high[0]), facecolor=fille, edgecolor=fille, alpha = 0.5)
    print "The Graph for "+stock+ "is being plotted"
    
    plt.subplots_adjust(left=0.09 , bottom=0.14 , right=0.97 , top=0.94 , wspace=0.2 , hspace=0)
    plt.legend()
    plt.grid(True)
    plt.show()
    
for each in stox:
    fetchdata(each)
    graph(each)


