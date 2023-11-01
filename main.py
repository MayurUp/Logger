import logging
import traceback
import time
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


message = 'passing the varibale'
format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s'

def log(message):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(message+"debug")
    logging.info(message+"info")
    logging.warning(message+"warning")
    logging.error(message+"error")
    logging.critical(message+"critical")
    return logging

# path_var = 'var/www/html'
# file_name = message+ error

def log2():
    logging.basicConfig(level=logging.DEBUG, format=format,filename='employee.log',datefmt='%m/%d/%Y %H:%M:%S')
    logging.debug(message+"debug")
    logging.info(message+"info")
    logging.warning(message+"warning")
    logging.error(message+"error")
    logging.critical(message+"critical")
    return logging

def log3():
    try:
        a = [1, 2, 3]
        val = a[4]
    except:
        logging.error('This is a %s', traceback.format_exc())
    # except IndexError as e:
    #     logging.error(e, exc_info=True)
        return logging

def rotating_file_handler():
    logger= logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    #roll over after 2KB,and keep backup logs app.log.1,app.log.2,etc.
    # handler = RotatingFileHandler('app.log',maxBytes=2000,backupCount=5)

    #s,m,h,d,midnight,w0
    handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
    logger.addHandler(handler)
    for i in range(6):
        logger.info('Hello world!'+str(i))
        time.sleep(10)

if __name__ == '__main__':
    log3()

