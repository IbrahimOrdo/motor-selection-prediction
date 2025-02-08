import pandas as pd
import os

def collect_data():
    # Örnek: CSV dosyasından veri okuma (veya API/web scraping ile veri toplama)
    url = "https://example.com/motor_verileri.csv"
    data = pd.read_csv(url)
    
    # Ham veriyi kaydet
    if not os.path.exists('data/raw'):
        os.makedirs('data/raw')
    data.to_csv('data/raw/motor_verileri.csv', index=False)
    print("Veri toplandı ve kaydedildi.")

if __name__ == "__main__":
    collect_data()