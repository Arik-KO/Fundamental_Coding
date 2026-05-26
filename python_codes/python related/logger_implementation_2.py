import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s)')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f"created employee : {self.fullname} - {self.email})")

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


emp1 = Employee('Garret', 'Smith')
em2 = Employee('Jey', 'Smith')
em3 = Employee('Jafar', 'Zehran')