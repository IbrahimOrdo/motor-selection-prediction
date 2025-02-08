from src.data_collection import collect_data
from src.data_preprocessing import preprocess_data
from src.data_analysis import analyze_data
from src.model_training import train_model
from src.prediction import predict
from src.optimization import optimize_model

if __name__ == "__main__":
    collect_data()
    preprocess_data()
    analyze_data()
    train_model()
    predict()
    optimize_model()