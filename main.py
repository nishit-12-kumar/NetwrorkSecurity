from NetworkSecurity.components.data_ingestion import DataIngestion
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging

from NetworkSecurity.entity.config_entity import DataIngestionConfig , DataValidationConfig , DataTransformationConfig ,ModelTrainerConfig
from NetworkSecurity.entity.config_entity import TrainingPipelineConfig 
from NetworkSecurity.components.data_validation import DataValidation
from NetworkSecurity.components.data_transformation import DataTransformation 
from NetworkSecurity.components.model_trainer import ModelTrainer


import sys


if __name__ == "__main__":
    try:
        ## Data Ingestion...
        trainingpipelineconfig = TrainingPipelineConfig()

        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)

        logging.info("Initiate the data ingestion...")

        dataingestionartifact = data_ingestion.initiate_data_ingestion()

        logging.info("Data Inititation Completed.")
        print(dataingestionartifact)


        ## Data Validation...
        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        data_validation =  DataValidation(dataingestionartifact , datavalidationconfig)

        logging.info("Initiate the Data Validation...")

        datavalidationartifact = data_validation.initiate_data_validation()

        logging.info("Data Validation Completed...")         
        print(datavalidationartifact)


        ## Data Transformation...
        datatransformationconfig = DataTransformationConfig(trainingpipelineconfig)
        data_transformation =  DataTransformation(datavalidationartifact , datatransformationconfig)

        logging.info("Initiate the Data Transformation...")

        datatransformationartifact = data_transformation.initiate_data_transformation()

        logging.info("Data Transformation Completed...")         
        print(datatransformationartifact)


        ## Model Trainer...
        modeltrainerconfig = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer =  ModelTrainer(model_trainer_config=modeltrainerconfig , data_transformation_artifact=datatransformationartifact)

        logging.info("Initiate the Model Trainer...")

        modeltrainerartifact = model_trainer.initiate_model_trainer()

        logging.info("Model Trainer Completed...")         
        print(modeltrainerartifact)




    except Exception as e:
        raise NetworkSecurityException(e,sys)

