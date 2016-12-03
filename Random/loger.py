import logging
logging.basicConfig(filename='file.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start')
logging.debug('end')
