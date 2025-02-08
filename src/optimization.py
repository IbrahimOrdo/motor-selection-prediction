from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import joblib

def optimize_model():
    # Modeli yükle
    model = joblib.load('model.pkl')
    
    # Hiperparametre optimizasyonu
    param_grid = {'n_neighbors': [3, 5, 7, 9]}
    grid_search = GridSearchCV(model, param_grid, cv=5)
    grid_search.fit(X_train, y_train)
    
    # En iyi parametreleri kaydet
    best_model = grid_search.best_estimator_
    joblib.dump(best_model, 'optimized_model.pkl')
    print("Model optimizasyonu tamamlandı ve kaydedildi.")

if __name__ == "__main__":
    optimize_model()