import os
import sys
import json

from dotenv import load_dotenv

import certifi
import pandas as pd
import numpy as np
import pymango

from networksecurity.exception.exception import NetworksecurityException
from networksecurity.logger.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworksecurityException(e,sys)
        
    def csv_tojson_convertor(self):
        try:
            pass
        except Exception as e:
            raise NetworksecurityException(e,sys)
        
    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworksecurityException(e,sys)
        
        
if __name__=='__main__':
    pass