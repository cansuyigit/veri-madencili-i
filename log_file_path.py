import os

# Dosya yolu
log_file_path = 'C:\\path\\to\\logfile.txt'

# Klasörler mevcut değilse oluştur
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

# Boş bir dosya oluştur
with open(log_file_path, 'w') as log_file:
    log_file.write("")  # Dosyayı boş olarak oluşturuyoruz