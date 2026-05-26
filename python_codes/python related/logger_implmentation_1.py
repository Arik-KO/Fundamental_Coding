import logging
import logger_implementation_2

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


formatter = logging.Formatter('	%(asctime)s : %(levelname)s : %(lineno)d : %(message)s')

file_handler = logging.FileHandler('exp_.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)




def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x * y

def division(x, y):


    try:
        result = x /y
    except ZeroDivisionError:
        logger.exception('tried to divide by zero')
    else:
        return result

num_a , num_b = 15, 0

if __name__ == "__main__":
    logger.debug(add(num_a, num_b))
    logger.debug(subtract(num_a, num_b))
    logger.debug(multiply(num_a, num_b))
    logger.debug(division(num_a, num_b))