import pandas as pd
import joblib

def predict():
    # Modeli yükle
    model = joblib.load('model.pkl')
    
    # Yeni kullanıcı bilgileri
    new_user = pd.DataFrame({
        'Age': [30],
        'Height': [177],
        'Weight': [70],
        'Gender': [1],  # 1: Erkek, 0: Kadın  
        'MaritalStatus': [1]
    })
    
    # Tahmin yap
    print(model.feature_names_in_)

    recommended_motors = model.predict_proba(new_user)
    top_3_motors = recommended_motors.argsort()[0][-3:]
    print(f"Önerilen Motorlar: {top_3_motors}")

if __name__ == "__main__":
    predict()