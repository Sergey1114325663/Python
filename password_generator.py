import random
import string
import tkinter as tk
from tkinter import messagebox


# Функция генерации пароля на основе указанных параметров
def generate_password(length, use_letters, use_digits, use_punctuation):
    # Создание строки символов на основе выбранных опций
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # Добавляем буквы (верхний и нижний регистр)
    if use_digits:
        characters += string.digits  # Добавляем цифры
    if use_punctuation:
        characters += string.punctuation  # Добавляем специальные символы

    # Проверяем, выбрал ли пользователь хотя бы один тип символов
    if not characters:
        messagebox.showwarning("Предупреждение", "Выберите хотя бы один тип символов.")
        return ""

    # Генерация пароля из случайных символов
    password = ''.join(random.choice(characters) for _ in range(length))

    # Обновляем индикатор сложности после генерации
    update_strength_label(length, use_letters, use_digits, use_punctuation)
    return password


# Функция, вызываемая при нажатии на кнопку "Сгенерировать пароль"
def generate_password_with_ui():
    # Получаем значения из интерфейса
    length = password_length.get()
    use_letters = var_letters.get()
    use_digits = var_digits.get()
    use_punctuation = var_punctuation.get()

    # Генерация пароля и вывод его в поле для пароля
    password = generate_password(length, use_letters, use_digits, use_punctuation)
    entry_password.delete(0, tk.END)  # Очищаем поле перед выводом нового пароля
    entry_password.insert(0, password)


# Функция для копирования пароля в буфер обмена
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        # Очищаем буфер обмена и добавляем туда пароль
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Успех", "Пароль скопирован в буфер обмена.")
    else:
        # Предупреждение, если попытка копирования пустого поля
        messagebox.showwarning("Предупреждение", "Сначала сгенерируйте пароль.")


# Функция для очистки поля с паролем
def clear_password():
    entry_password.delete(0, tk.END)  # Очищаем поле вывода пароля
    strength_label.config(text="Сложность: -")  # Сбрасываем индикатор сложности


# Функция для обновления индикатора сложности пароля
def update_strength_label(length, use_letters, use_digits, use_punctuation):
    # Устанавливаем базовый балл безопасности
    score = 0
    if use_letters:
        score += 1
    if use_digits:
        score += 1
    if use_punctuation:
        score += 1

    # Увеличиваем балл в зависимости от длины пароля
    if length >= 12:
        score += 1  # Высокий балл для длинных паролей
    elif length >= 8:
        score += 0.5  # Средний балл для умеренной длины

    # Определяем сложность на основе набранного балла
    if score >= 3:
        strength = "Высокая"
    elif score >= 2:
        strength = "Средняя"
    else:
        strength = "Низкая"

    # Обновляем текст метки сложности
    strength_label.config(text=f"Сложность: {strength}")


# Создание главного окна приложения
window = tk.Tk()
window.title("Генератор паролей")

# Ползунок для выбора длины пароля
label_length = tk.Label(window, text="Длина пароля:")
label_length.pack(pady=5)
password_length = tk.IntVar(value=12)  # Значение по умолчанию - 12 символов
slider_length = tk.Scale(window, from_=6, to=20, orient=tk.HORIZONTAL, variable=password_length)
slider_length.pack(pady=5)

# Флажки для выбора включаемых типов символов
var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_punctuation = tk.BooleanVar(value=True)

check_letters = tk.Checkbutton(window, text="Буквы (A-Z, a-z)", variable=var_letters)
check_letters.pack(pady=2)
check_digits = tk.Checkbutton(window, text="Цифры (0-9)", variable=var_digits)
check_digits.pack(pady=2)
check_punctuation = tk.Checkbutton(window, text="Спец. символы (!@#)", variable=var_punctuation)
check_punctuation.pack(pady=2)

# Кнопка для генерации пароля
button_generate = tk.Button(window, text="Сгенерировать пароль", command=generate_password_with_ui)
button_generate.pack(pady=10)

# Поле для отображения сгенерированного пароля
entry_password = tk.Entry(window, width=30)
entry_password.pack(pady=5)

# Кнопка для копирования пароля в буфер обмена
button_copy = tk.Button(window, text="Копировать в буфер обмена", command=copy_to_clipboard)
button_copy.pack(pady=5)

# Кнопка для очистки поля с паролем
button_clear = tk.Button(window, text="Очистить", command=clear_password)
button_clear.pack(pady=5)

# Метка для индикатора сложности пароля
strength_label = tk.Label(window, text="Сложность: -")
strength_label.pack(pady=5)

# Запуск основного цикла окна
window.mainloop()