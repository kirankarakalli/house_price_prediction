import pandas as pd
import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.config import PROCESSED_DATA_DIR
from src.config import RAW_DATA_PATH,TEST_SIZE,RANDOM_STATE
from sklearn.model_selection import train_test_split

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
        CustomException(e,sys)
    

def preprocess_data(df):
    '''
    Handles a missing values and duplicates
    '''

    try:
        logging.info("preprocess a dataset")

        missing=df.isnull().sum().sum()

        if missing>0:
            df.fillna(0,inplace=True)
        else:
            logging.info("Dataset has no missing value")

        logging.info("preprocess is done")
        return df
    
    except Exception as e:
        CustomException(e,sys)



def splitandsave(df):
    '''
    split dataframe into train and test dataset
    '''

    try:
        logging.info("spliting a dataset into train and test dataset")
        X=df.drop('Price',axis=1)
        y=df['Price']

        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=TEST_SIZE,random_state=RANDOM_STATE)

        X_train.to_csv(os.path.join(PROCESSED_DATA_DIR,'X_train.csv'),index=False)
        X_test.to_csv(os.path.join(PROCESSED_DATA_DIR,'X_test.csv'),index=False)
        y_train.to_csv(os.path.join(PROCESSED_DATA_DIR,'y_train.csv'),index=False)
        y_test.to_csv(os.path.join(PROCESSED_DATA_DIR,'y_test.csv'),index=False)

        logging.info("sucessfully splited a dataset into train and test")
        
    except Exception as e:
        logging.info("error in spliting a dataset")
        CustomException(e,sys)
    




def main():

    try:
        logging.info("load and preprocess is start")
        df=load_data()
        df=preprocess_data(df)
        splitandsave(df)
        logging.info("split a dataset sucessfully")

    except Exception as e:
        CustomException(e,sys)


if __name__=="__main__":
    main()