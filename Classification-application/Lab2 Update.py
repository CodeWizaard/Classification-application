import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from collections import Counter
import matplotlib.pyplot as plt

# Глобальные переменные
processed_data = None
X_train, X_test, y_train, y_test = None, None, None, None


def process_multiclass_dataset(file_path):
    """
    Обрабатывает датасет с несколькими классами, объединяя все классы в один DataFrame.
    """
    try:
        data = pd.read_excel(file_path)
        num_classes = data.shape[1] // 3  # Три столбца на класс (X1, X2, Y)
        combined_data = []

        for i in range(num_classes):
            start_col = i * 3
            subset = data.iloc[:, start_col:start_col + 3].copy()
            subset.columns = ['x1', 'x2', 'Y']
            combined_data.append(subset)

        combined_data = pd.concat(combined_data, ignore_index=True)
        return combined_data

    except Exception as e:
        print(f"Ошибка обработки файла: {e}")
        return None


def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


def knn_classify(test_point, X_train, y_train, k):
    distances = []
    for train_point in X_train:
        distances.append(euclidean_distance(test_point, train_point))

    sorted_indices = np.argsort(distances)
    k_nearest_indices = sorted_indices[:k]
    nearest_labels = [y_train[i] for i in k_nearest_indices]
    label_counts = Counter(nearest_labels)
    return label_counts.most_common(1)[0][0]


def split_dataset(data, test_size=0.2):
    global X_train, X_test, y_train, y_test
    X = data[['x1', 'x2']].values
    y = data['Y'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)


def run_knn_and_plot():
    k_values = [3, 5, 7, 9, 11]
    scores = []
    for k in k_values:
        correct = sum(
            knn_classify(X_test[i], X_train, y_train, k) == y_test[i]
            for i in range(len(X_test))
        )
        scores.append(correct / len(X_test))

    plt.plot(k_values, scores, marker='o')
    plt.xlabel('k')
    plt.ylabel('Accuracy')
    plt.title('k-NN Classification Accuracy')
    plt.grid()
    plt.show()


def choose_file():
    file_path = filedialog.askopenfilename(title="Выберите файл")
    if file_path:
        label.config(text=f"Выбран файл: {file_path}")
        global processed_data
        processed_data = process_multiclass_dataset(file_path)
        if processed_data is not None:
            split_dataset(processed_data)
            button_run.config(image=done_image, state=tk.NORMAL)


# Интерфейс
mainWindow = tk.Tk()
mainWindow.title("k-NN Classifier")
mainWindow.geometry("400x200")

label = tk.Label(mainWindow, text="Выберите файл с данными", font=("Helvetica", 14))
label.pack(pady=10)

# Загрузка изображений
start_image = tk.PhotoImage(file="But.png")  # Первоначальная кнопка
done_image = tk.PhotoImage(file="Done.png")  # Изображение для кнопки после выбора файла
confirm_image = tk.PhotoImage(file="Confirm.png")  # Дополнительное изображение для других кнопок

button_file = tk.Button(mainWindow, image=start_image, command=choose_file, borderwidth=0)
button_file.pack(pady=10)

button_run = tk.Button(mainWindow, image=confirm_image, command=run_knn_and_plot, state=tk.DISABLED, borderwidth=0)
button_run.pack(pady=10)

mainWindow.mainloop()
