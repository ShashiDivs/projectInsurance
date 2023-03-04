from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys

def test_logger_and_exception():
    try:
        logging.info('starting the test logger and exception')
        result = 3/10
        print(result)
        logging.info('ending point of the test logger and exception')
    except Exception as e:
        logging.Debug(str(e))
        raise InsuranceException(e,sys)


if __name__ == "__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)


    
