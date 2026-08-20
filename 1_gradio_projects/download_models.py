import os
import zipfile
import requests
import gdown

def download_and_extract():
    
    url = 'https://drive.google.com/uc?id=1O_mtPVYWYGrL8Eg14BQ4OIXmUjq6ebqT'
    gdown.download(url, 'data.zip', quiet=False)


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

if __name__ == "__main__":
    download_and_extract()
