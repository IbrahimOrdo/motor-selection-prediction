import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os
from enum import Enum
import json


def preprocess_data():
    # Ham veriyi yükle
    data = pd.read_csv('data/simulated/simulated_motor_data.csv')

    # Eksik verileri doldur veya çıkar
    data.dropna(inplace=True)

    # Kategorik sütunlar
    categorical_columns = ['Gender', 'MaritalStatus', 'Preferred Motorcycle']

    # LabelEncoder sözlüğü
    label_mappings = {}
    # Label encoding işlemi
    label_encoder = LabelEncoder()
    for col in categorical_columns:
        data[col] = label_encoder.fit_transform(data[col])
        label_mappings[col] = {idx: label for idx, label in enumerate(label_encoder.classes_)}

    # **Enum sınıflarını oluştur**
    enum_classes = {}
    for col, mapping in label_mappings.items():
        class_name = col.replace(" ", "")  # Boşlukları kaldırarak isimlendirme yapıyoruz
        enum_code = f"class {class_name}:\n"
        for key, value in mapping.items():
            enum_code += f"    {value.upper().replace(' ', '_')} = {key}\n"
        enum_classes[col] = enum_code    

    # **Enum kodlarını bir dosyaya kaydet**
    with open("data/processed/enums.py", "w", encoding="utf-8") as f:
        for code in enum_classes.values():
            f.write(code + "\n\n")

    # **LabelEncoder eşleşmelerini JSON olarak kaydet**
    os.makedirs("data/processed", exist_ok=True)
    with open("data/processed/label_mappings.json", "w", encoding="utf-8") as json_file:
        json.dump(label_mappings, json_file, indent=4, ensure_ascii=False)

        
    # Sayısal verileri normalize et
    scaler = StandardScaler()
    data[['Age', 'Height', 'Weight']] = scaler.fit_transform(data[['Age', 'Height', 'Weight']])   
        
    # İşlenmiş veriyi kaydet
    if not os.path.exists('data/processed'):
        os.makedirs('data/processed')
    data.to_csv('data/processed/cleaned_motor_data.csv', index=False)
    print("Veri ön işleme tamamlandi ve kaydedildi.")
    print("Kategorik veriler sayısallaştırıldı, Enum sınıfları ve JSON dosyası oluşturuldu.")

if __name__ == "__main__":
    preprocess_data()