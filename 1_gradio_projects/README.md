
# Примеры работы моделей на Gradio  
- Сегментация дорожных сцен  
- Детекция ключевых точек лиц  
- Детекция с БПЛА  
- Интерполяция изображений  
- Классификация отзывов IMDb  

--------------------------

## Запуск локально 

### Скачать проект в папку  
```
# Скачать проект в папку  
git clone https://github.com/MALeyman/1_Gradio.git  

```
### Либо с ресурса  https://download-directory.github.io/  

### Перейти в папку проекта 

### Создать окружение
```
python -m venv .myenv

```

### Активировать окружение
```
# На Линукс
source .myenv/bin/activate

# На Виндовс
.myenv\Scripts\activate.bat

```

### Установить зависимости  
```
pip install -r requirements.txt
```

### Скачать модели, файлы.
#### Запустить скрипт  __main.ipynb__  
#### Либо:  
```
import gdown
url = 'https://drive.google.com/uc?id=13Z5VjNKBO8zGFzC5ML3hMrUW2ynQGhsb'
gdown.download(url, 'data.zip', quiet=False)

import zipfile
import os

# Путь к скачанному архиву
zip_path = "data.zip"
# Каталог для распаковки (можно указать '.', если нужно в текущую папку)
extract_dir = "."

# Распаковка архива
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print("Архив распакован")

# Удаление архива
os.remove(zip_path)
print("Архив удален")
```
### ЗАПУСК
```
python app.py
```


###  [Сайт](https://huggingface.co/spaces/makc-mon173/projects)

------------------------

<img width="1612" height="628" alt="image" src="https://github.com/user-attachments/assets/41f16545-2b2f-4adc-804c-64b6be516628" />

