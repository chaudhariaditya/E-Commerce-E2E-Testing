import inspect
import logging

class LogGenerator:
    @staticmethod
    def logen():
        name=inspect.stack()[1][3]
        logger=logging.getLogger(name)
        logfile=logging.FileHandler("D:\\Ajio\\Logs\\Product.log")
        format=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger