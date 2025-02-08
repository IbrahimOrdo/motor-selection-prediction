import pandas as pd
import numpy as np

# Rastgele veri oluştur
np.random.seed(42)
n = 1000  # Örnek sayısı

data = {
    'Name': [f'User_{i}' for i in range(n)],
    'Age': np.random.randint(18, 65, n),
    'Height': np.random.randint(150, 200, n),
    'Weight': np.random.randint(50, 120, n),
    'Gender': np.random.choice(["Man", "Woman"], size=n),
    'MaritalStatus': np.random.choice(['Single', 'Married'], n),
    'Preferred Motorcycle': np.random.choice(['Honda', 'Yamaha', 'Kawasaki', 'BMW'], n)
}

# # DataFrame'e dönüştür
# df = pd.DataFrame(data)
# df.to_csv('simulated_motor_data.csv', index=False)