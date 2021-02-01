#Author: Vikas Dhyani
#This is the code to extract the stock price from IEX API (need to take the subscription for it)
#
import requests
import json
import org.pydev.dhyaniv.mediaPlayer.alertSounds as alertSounds
import org.pydev.dhyaniv.constants.constants as constants
import org.pydev.dhyaniv.dbfetch.loadCryptos as loadCryptos
import pync
from datetime import datetime
from termcolor import colored
import urllib.request

from os import path


        
def getShortTermBuyData():
    cryptosToTrack = loadCryptos.getCryptosymbols()
    print("****************")
    for x in cryptosToTrack:
        endPoint = "https://data.messari.io/api/v1/assets/"+str(x[1])+"/metrics"
        #stock_symbol = x[0]
        stock_name = x[1]
        #print(IEXendpoint) # Printing the symbol
        #stockName = str(x[2])
        
        #getStockData(IEXendpoint, stockName)
        shortBuyNotification(endPoint, stock_name)
        
    print("****************\n")
    
    
              
def shortBuyNotification(url, nameOfStock):
     
    filepath = path.relpath(constants.APISECRETPATH)  
    
    with open(filepath) as f:
        data = f.read()
        
    hdrs = json.loads(data)   
    req = urllib.request.Request(url, headers=hdrs)
    response = urllib.request.urlopen(req)
    data = response.read()
    currencyData = json.loads(data.decode('utf-8'))
    print(currencyData["data"]["market_data"]["price_usd"])
    print(currencyData["data"]["market_data"]["percent_change_usd_last_24_hours"])
    print(currencyData["data"]["market_data"]["percent_change_usd_last_1_hour"])
    
    
    