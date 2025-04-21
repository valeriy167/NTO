from sklearn.linear_model import LinearRegression
import numpy as np

# Тестовые данные: историческое потребление (например, за 30 дней)
X = np.array(range(30)).reshape(-1, 1)
y = np.sin(X).flatten() * 10 + np.random.normal(0, 1, 30)  # Сезонные колебания

# Обучение модели
model = LinearRegression()
model.fit(X, y)

# Прогноз на следующий день
next_day = np.array([[31]])
prediction = model.predict(next_day)
print(f"Прогноз потребления: {prediction[0]:.2f} м³/сутки")  # [[6]][[8]]