import logging

logger = logging.Logger('unittesting',level=0)
logger.setLevel(0)

def logresult(test):

    def wrapper():
        print("entered wrapper")
        res = test()
        if res :
            logger.error(test.__name__)
        else :
            logger.error("failed")
    return wrapper
