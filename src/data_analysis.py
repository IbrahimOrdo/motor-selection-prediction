import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_data():
    # İşlenmiş veriyi yükle
    data = pd.read_csv('data/processed/cleaned_motor_data.csv')
    data = data.drop(columns=["Name"])
    
    # Korelasyon matrisi
    corr_matrix = data.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title("Korelasyon Matrisi")
    plt.show()

if __name__ == "__main__":
    analyze_data()