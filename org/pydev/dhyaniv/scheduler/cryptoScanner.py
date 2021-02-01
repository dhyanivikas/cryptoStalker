import org.pydev.dhyaniv.cryptoAnalyzer.analyzeCryptoPositions as analyzeCryptoPositions
import org.pydev.dhyaniv.constants.constants as constants
import time
import schedule



if __name__ == "__main__":
    print("Hello guys!")
    #schedule.every(20).seconds.do(stockAnalyzer.getStockData)
    #schedule.every(constants.CHECKFREQUENCY).seconds.do(stockAnalyzer.getStockData)
    #schedule.every(constants.CHECKFREQUENCY).seconds.do(stockAnalyzer.getStalkedStocksData)
    #schedule.every(constants.CHECKFREQUENCY).seconds.do(analyzeCryptoPositions.getSellNotificationData)
    schedule.every(constants.CHECKFREQUENCY).seconds.do(analyzeCryptoPositions.getShortTermBuyData)
    #schedule.every(constants.CHECKFREQUENCY).seconds.do(analyzeCryptoPositions.getLossesData)
    

    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)