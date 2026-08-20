import os
import zipfile
import gdown

def download_and_extract():
    url = 'https://drive.google.com/uc?id=13Z5VjNKBO8zGFzC5ML3hMrUW2ynQGhsb'
    archive_name = 'data.zip'
    extract_dir = '.'

    print("Начинается загрузка тяжелых файлов и моделей из Google Drive...")
    gdown.download(url, archive_name, quiet=False)

    if not os.path.exists(archive_name):
        print(" Ошибка: Файл не был скачан.")
        return

    print("Распаковка архива...")
    with zipfile.ZipFile(archive_name, 'r') as zip_ref:
        # Поочередная распаковка файлов для экономии ОЗУ
        for file in zip_ref.namelist():
            zip_ref.extract(file, extract_dir)
            
    print("Очистка временных файлов...")
    os.remove(archive_name)
    print("Все модели успешно загружены и готовы к работе!")

if __name__ == "__main__":
    download_and_extract()
