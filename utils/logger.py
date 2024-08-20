import logging

def setup_logger(name):
    # Setting up a basic logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler