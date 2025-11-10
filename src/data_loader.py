import pandas as pd
import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.config import PROCESSED_DATA_DIR
from src.config import RAW_DATA_PATH


def load_data():
    '''
    load a dataset and return as a DataFrame
    '''
    try:
        logging.info("started loading a raw dataset")
        df=pd.read_csv(RAW_DATA_PATH)
        logging.info("loaded a raw dataset succesfully")
        return df
    except Exception as e:
        logging.info("error in loading a data")
        raise CustomException(e,sys)
    


def splitandsave(df):
    '''
    split dataframe into train and test dataset
    '''

    try:
        
    except Exception as e:
        raise CustomException(e,sys)



