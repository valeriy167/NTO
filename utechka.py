import numpy as np
import random

# Тестовые данные: давление в трубопроводе (моделируем норму и аномалии)
pressure_data = np.concatenate([
    np.random.normal(loc=4, scale=0.5, size=100),  # Нормальное давление
    np.random.normal(loc=2.5, scale=0.3, size=20)  # Аномалии (утечки)
])

def detect_leak(data, threshold=3.0):
    anomalies = []
    for i, p in enumerate(data):
        if p < threshold:
            anomalies.append((i, p))
    return anomalies

# Пример использования
leaks = detect_leak(pressure_data)
print(f"Обнаружено утечек: {len(leaks)}")  # [[2]][[7]]