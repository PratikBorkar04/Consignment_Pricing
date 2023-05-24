import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.component.data_transformation import DataTransformation
from src.component.data_transformation import DataTransformationConfig

from src.component.model_trainer import ModelTrainerConfig
from src.component.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')



class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion")
        try:
            df = pd.read_csv("https://raw.githubusercontent.com/PratikBorkar04/consignment_pricing/main/notebook/dataset/CatBoosting_dataset.csv")
            logging.info("Entered the dataset")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index = False,header=True)

            logging.info("Train test initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header=True)
            logging.info("Ingestion Completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path 
            )
        except Exception as ex:
            raise CustomException(ex,sys)
        
if __name__== "__main__":
    obj = DataIngestion()
    #obj.initiate_data_ingestion() # DATA INGESTION CODE TO CREATE ARTIFACT TRAIN,TEST DATA

    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    result = data_transformation.initiate_data_transformation(train_data, test_data)
    train_arr = result[0]
    test_arr = result[1]
    
    
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr) )
