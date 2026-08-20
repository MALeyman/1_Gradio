# Примеры работы моделей на Gradio  
- Сегментация дорожных сцен  
- Детекция ключевых точек лиц  
- Детекция с БПЛА  
- Интерполяция изображений  
- Классификация отзывов IMDb  

--------------------------

## Запуск локально 

### 1. Клонирование репозитория
Склонируйте проект или скачайте его отдельной папкой через [download-directory](https://github.io):
```bash
git clone https://github.com/MALeyman/1_Gradio.git  
```

### 2. Настройка виртуального окружения
Создайте и активируйте виртуальное окружение:
```bash
cd 1_Gradio/1_gradio_projects
# Создание
python -m venv .myenv

# Активация на Linux/macOS
source .myenv/bin/activate

# Активация на Windows
.myenv\Scripts\activate
```

### 3. Установка зависимостей и скачивание моделей
Установите необходимые библиотеки (включая `gdown` для загрузки моделей) и запустите скрипт автоматического скачивания весов:
```bash
pip install -r requirements.txt
python download_models.py
```

### 4. Запуск приложения
```bash
python app.py
```

### 🌍 [Попробовать онлайн на Hugging Face Spaces](https://huggingface.co/spaces/makc-mon173/projects)

------------------------

<img width="1612" height="628" alt="Интерфейс приложения Gradio" src="https://github.com/user-attachments/assets/41f16545-2b2f-4adc-804c-64b6be516628" />




