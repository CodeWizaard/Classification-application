import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
    data = pd.read_csv(file_path, encoding="utf-8-sig")
    print(data)
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