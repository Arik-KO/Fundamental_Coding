import logging

logging.basicConfig(filename = 'exp_.log', level = logging.DEBUG,
                    format = '	%(asctime)s : %(levelname)s : %(lineno)d : %(message)s' )

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x * y

def division(x, y):
    return x/y

num_a , num_b = 15, 20

if __name__ == "__main__":
    logging.warning(add(num_a, num_b))
    logging.debug(subtract(num_a, num_b))
    logging.debug(multiply(num_a, num_b))
    logging.debug(division(num_a, num_b))