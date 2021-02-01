'''
Created on Jan 3, 2021

@author: dhyaniv
'''

import mysql.connector
import org.pydev.dhyaniv.dbfetch.getDBConnection as dbConn



def getCryptosymbols(): #no error method
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    cur.execute("select id, curr_symbol from crypto_list")
    cryptoList = cur.fetchall()
    return cryptoList



def getOpenPriceSubjectsList():
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    cur.execute("select id, stock_symbol, stock_name from stocks_watch_list where track_open_price = 'Y'")
    openPriceStalkerSubjects = cur.fetchall()
    return openPriceStalkerSubjects    

#getStockSubjectsList()

def insertIntoOpenPriceTracker(stock_symbol, trading_date, open_price):
    
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    #query = 'INSERT INTO stocks_opening_prices1(stock_symbol, trading_date, open_price) values(%s,%s,%d) '
    query = 'INSERT INTO stocks_opening_prices(stock_symbol, trading_date, open_price) values(%s,%s,%s) '
    args = (stock_symbol, trading_date, round(open_price,2))
    print(stock_symbol+"***"+trading_date+"***"+str(open_price))
    cur.execute(query, args)
    dbConnection.commit()
    
    
def getSellTargets():
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    #cur.execute("select stock_symbol, stock_name, qty, min_target_price, buy_price from stocks_buys_and_targets where already_sold = 'N' ")
    cur.execute("select stock_symbol, stock_name, qty, min_target_price, buy_price, buy_date from stocks_buys_and_targets where already_sold = 'N' and through_recommendation='N' ")
    openPriceStalkerSubjects = cur.fetchall()
    return openPriceStalkerSubjects


def getShortTermTargets():
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    #cur.execute("select stock_symbol, stock_name, qty, min_target_price, buy_price from stocks_buys_and_targets where already_sold = 'N' ")
    cur.execute("select stock_symbol, stock_name from short_term_watch_list where track_intra_day = 'Y'")
    openPriceStalkerSubjects = cur.fetchall()
    return openPriceStalkerSubjects 
 
def updateLatestPrice(stock_symbol, latest_price):     
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    #query = 'INSERT INTO stocks_opening_prices1(stock_symbol, trading_date, open_price) values(%s,%s,%d) '
    query = 'update stocks_buys_and_targets set latest_price =%s where stock_symbol = %s'
    args = (latest_price, stock_symbol)
    cur.execute(query, args)
    dbConnection.commit()
    
def getLosses():
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    #cur.execute("select stock_symbol, stock_name, qty, min_target_price, buy_price from stocks_buys_and_targets where already_sold = 'N' ")
    cur.execute("select stock_symbol, stock_name, qty, buy_price, latest_price, buy_date from stocks_buys_and_targets where already_sold = 'N' and through_recommendation='N'  and latest_price < buy_price")
    lossStocks = cur.fetchall()
    return lossStocks    
        
def getProfits():
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    #cur.execute("select stock_symbol, stock_name, qty, min_target_price, buy_price from stocks_buys_and_targets where already_sold = 'N' ")
    cur.execute("select stock_symbol, stock_name, qty, buy_price, latest_price, buy_date from stocks_buys_and_targets where already_sold = 'N' and through_recommendation='N'  and latest_price >= buy_price")
    profitStocks = cur.fetchall()
    return profitStocks    