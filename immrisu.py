import matplotlib.pyplot as plt
import numpy as np

# Параметры
k = 4  # Число стадий в конвейере
t = 1  # Время выполнения одной стадии (в секундах)
num_tasks = 10  # Количество задач

# Время отклика без конвейера
time_without_pipeline = [i * k * t for i in range(1, num_tasks + 1)]

# Время отклика с конвейером
time_with_pipeline = [max(k * t, i * t) for i in range(1, num_tasks + 1)]

# Время окончания каждой задачи
tasks = np.arange(1, num_tasks + 1)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(tasks, time_without_pipeline, label='Без конвейера', marker='o')
plt.plot(tasks, time_with_pipeline, label='С конвейером', marker='o')
plt.title('График времени отклика задач с и без использования конвейера')
plt.xlabel('Номер задачи')
plt.ylabel('Время завершения (с)')
plt.grid(True)
plt.legend()
plt.show()
