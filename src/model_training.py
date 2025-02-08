import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

def train_model():
    # İşlenmiş veriyi yükle
    data = pd.read_csv('data/processed/cleaned_motor_data.csv')
    data = data.drop(columns=["Name"])
    
    # Bağımsız ve bağımlı değişkenleri ayır
    X = data.drop('Preferred Motorcycle', axis=1)
    y = data['Preferred Motorcycle']
    
    # Veriyi eğitim ve test setlerine ayır
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Modeli oluştur ve eğit
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    
    # Modeli kaydet
    joblib.dump(model, 'model.pkl')
    print("Model eğitildi ve kaydedildi.")

if __name__ == "__main__":
    train_model()