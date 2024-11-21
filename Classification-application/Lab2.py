import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

processed_data = None
X_train, X_test, y_train, y_test = None, None, None, None

import pandas as pd
from sklearn.model_selection import train_test_split

# Глобальные переменные для хранения данных
X_train, X_test, y_train, y_test = None, None, None, None


def split_dataset(data, test_size=0.2, random_state=42):
    """
    Делит данные на тренировочную и тестовую выборки.

    Параметры:
        data (pd.DataFrame): Входные данные со столбцами x1, x2 и Y.
        test_size (float): Доля данных для тестовой выборки (по умолчанию 0.2).
        random_state (int): Значение для воспроизводимости разбиения (по умолчанию 42).

    Возвращает:
        None: Результаты сохраняются в глобальных переменных.
    """
    global X_train, X_test, y_train, y_test

    try:
        # Разделение на признаки (X) и метки классов (y)
        X = data[['x1', 'x2']].values
        y = data['Y'].values

        # Разделение на тренировочную и тестовую выборки
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        print("Данные успешно разделены:")
        print(f"Размер тренировочной выборки: {X_train.shape[0]} объектов")
        print(f"Размер тестовой выборки: {X_test.shape[0]} объектов")
    except Exception as e:
        print(f"Произошла ошибка при разделении данных: {e}")


def process_dataset(file_path):
    """
    Обрабатывает датасет, объединяя данные из всех классов в единую таблицу.

    Параметры:
        file_path (str): Путь к Excel-файлу с исходными данными.

    Возвращает:
        pd.DataFrame: Объединенные данные со столбцами x1, x2 и Y.
    """
    try:
        # Загрузка исходного файла
        data = pd.read_excel(file_path)

        # Инициализация списка для хранения данных
        combined_data = []

        # Обработка данных по колонкам (шаг 3)
        num_classes = data.shape[1] // 3  # Число классов
        for i in range(num_classes):
            start_col = i * 3
            subset = data.iloc[:, start_col:start_col + 3]  # Берем 3 колонки для текущего класса
            subset.columns = ['x1', 'x2', 'Y']  # Переименовываем колонки
            combined_data.append(subset)

        # Объединение всех классов в единый DataFrame
        combined_data = pd.concat(combined_data, ignore_index=True)

        print("Обработанные данные:")
        print(combined_data)  # Вывод первых строк для проверки
        return combined_data

    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")
        return None

mainWindow = tk.Tk()  # Инициализация главного окна
mainWindow.configure(bg="#f0f0f0")  # Установка цвета, например, светло-синего
mainWindow.title("Мое окно")  # Установка заголовка окна
mainWindow.geometry("600x600")  # Установка размеров окна (ширина x высота)

label = tk.Label(
    mainWindow,
    text="Добро пожаловать, выберите датасет",
    font=("Helvetica", 20),      # Установка шрифта Helvetica размером 16
    fg="#333333"                 # Тёмно-серый цвет текста
)
label.pack(pady=10)  # Выравнивание метки и отступ сверху
def create_supporting_interface():
    label1 = tk.Label(
        mainWindow,
        text="Введите процент обучающий выборки",
        font=("Helvetica", 20),  # Установка шрифта Helvetica размером 16
        fg="#333333"  # Тёмно-серый цвет текста
    )
    label1.pack(pady=10)
    entry = tk.Entry(
        mainWindow,
        font=("Helvetica", 12),  # Шрифт и размер текста
        fg="#333333",  # Цвет текста (темно-серый)
        bg="#e6e6e6",  # Цвет фона (светло-серый)
        insertbackground="black",  # Цвет курсора
        width=30,  # Ширина поля
        borderwidth=3,  # Толщина рамки
        relief="ridge"  # Стиль рамки (гладкий вид)
    )
    entry.pack(pady=10)
    ConfirmButton = tk.Button(
        mainWindow,
        image=chek_image,  # Установка изображения на фон кнопки
        command=on_сonfirm_click,
        borderwidth=0
    )
    ConfirmButton.pack(pady=10)  # Добавление кнопки с отступом
def on_сonfirm_click():
    print(1)
def on_button_click():
    label.config(text="Датасет выбран")
    choose_file()
def choose_file():
    file_path = filedialog.askopenfilename(title="Выберите файл")
    if file_path:
        label.config(text=f"Выбран файл: {file_path}")
        create_supporting_interface()
        button.config(image=new_image)
        processed_data = process_dataset(file_path)
        split_dataset(processed_data)
        print(f"Размер processed_data: {processed_data.shape}")
        print(f"Размер тренировочной выборки: {X_train.shape}")
        print(f"Размер тестовой выборки: {X_test.shape}")


start_image = tk.PhotoImage(file="But.png")  # Путь к первому изображению
new_image = tk.PhotoImage(file="Done.png")
chek_image = tk.PhotoImage(file="Confirm.png")
button = tk.Button(
    mainWindow,
    image=start_image,  # Установка изображения на фон кнопки
    command=on_button_click,
    borderwidth=0
)

button.pack(pady=10)  # Добавление кнопки с отступом
mainWindow.mainloop()