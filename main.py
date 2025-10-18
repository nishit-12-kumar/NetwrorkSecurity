from NetworkSecurity.components.data_ingestion import DataIngestion
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.entity.config_entity import DataIngestionConfig , DataValidationConfig
from NetworkSecurity.entity.config_entity import TrainingPipelineConfig 
from NetworkSecurity.components.data_validation import DataValidation

import sys


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()

        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)

        logging.info("Initiate the data ingestion...")

        dataingestionartifact = data_ingestion.initiate_data_ingestion()

        logging.info("Data Inititation Completed.")
        print(dataingestionartifact)

        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        data_validation =  DataValidation(dataingestionartifact , datavalidationconfig)

        logging.info("Initiate the Data Validation...")

        datavalidationartifact = data_validation.initiate_data_validation()

        logging.info("Data Validation Completed...")         
        print(datavalidationartifact)


    except Exception as e:
        raise NetworkSecurityException(e,sys)

