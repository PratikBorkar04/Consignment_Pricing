import sys
from dataclasses import dataclass
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

import numpy as np 
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn import preprocessing
from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            label_encoder = preprocessing.LabelEncoder()
            categorical_columns = ['country', 'vendor', 'shipment_mode', 'location']
            
            for i in categorical_columns:
                train_df[i]= label_encoder.fit_transform(train_df[i])

            for j in categorical_columns:
                test_df[j]= label_encoder.fit_transform(test_df[j])
            

            logging.info(f"Perfom label encoding")
            
            target_column_name="freight_cost"

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            logging.info(f"Column dropping perform")            
            train_arr = np.c_[
                input_feature_train_df, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[input_feature_test_df, np.array(target_feature_test_df)]

            return (                
                train_arr,
                test_arr,
            )
        except Exception as e:
            raise CustomException(e,sys)
