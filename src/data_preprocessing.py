import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os

def preprocess_data():
    # Ham veriyi yükle
    data = pd.read_csv('data/simulated/simulated_motor_data.csv')
    
    # Eksik verileri doldur veya çıkar
    data.dropna(inplace=True)
    
    # Kategorik verileri sayısallaştır
    label_encoder = LabelEncoder()
    #data['Yakıt_Türü'] = label_encoder.fit_transform(data['Yakıt_Türü'])
    data['Gender'] = label_encoder.fit_transform(data['Gender'])
    data['MaritalStatus'] = label_encoder.fit_transform(data['MaritalStatus'])
    data['Preferred Motorcycle'] = label_encoder.fit_transform(data['Preferred Motorcycle'])
     
    
    # Sayısal verileri normalize et
    scaler = StandardScaler()
    #data[['Güç', 'Tork', 'Ağırlık']] = scaler.fit_transform(data[['Güç', 'Tork', 'Ağırlık']])
    data[['Age', 'Height', 'Weight']] = scaler.fit_transform(data[['Age', 'Height', 'Weight']])

    
    # İşlenmiş veriyi kaydet
    if not os.path.exists('data/processed'):
        os.makedirs('data/processed')
    data.to_csv('data/processed/cleaned_motor_data.csv', index=False)
    print("Veri ön işleme tamamlandi ve kaydedildi.")

if __name__ == "__main__":
    preprocess_data()