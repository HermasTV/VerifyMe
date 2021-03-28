import logging

logger = logging.Logger('unittesting',level=0)
logger.setLevel(0)

def logresult(test):

    def wrapper():
        print("Testing : "+test.__name__)
        res = test()
        print(res)
        # if res :
        #     logger.error('')
        # else :
        #     logger.error("failed")
    return wrapper
