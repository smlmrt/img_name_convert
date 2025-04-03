import os
import shutil

# Dosyaların bulunduğu klasörün yolu
folder_path = "/path/to/your/folder"  # Kendi klasör yolunuzu buraya yazın

# Yeni dosyaların kaydedileceği klasörün yolu
output_folder_path = "/path/to/your/output_folder"  # Kendi çıkış klasör yolunuzu buraya yazın

# Yeni klasörü oluştur (eğer yoksa)
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)
    print(f"'{output_folder_path}' klasörü oluşturuldu.")

# Yeni dosya adlandırma formatı
new_name_format = "fire"

# Klasördeki tüm dosyaları listele
files = os.listdir(folder_path)

# Sadece dosyaları işle (klasörleri değil)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Dosyaları kopyala ve yeni isimlerle kaydet
for index, file in enumerate(files):
    # Orijinal dosya uzantısını al
    _, file_extension = os.path.splitext(file)
    
    # Eski ve yeni dosya yollarını oluştur
    old_file_path = os.path.join(folder_path, file)
    new_file_name = f"{new_name_format}_{index+1}{file_extension}"
    new_file_path = os.path.join(output_folder_path, new_file_name)
    
    # Dosyayı kopyala ve yeni isimle kaydet
    shutil.copy2(old_file_path, new_file_path)

print(f"{len(files)} dosya başarıyla kopyalandı ve yeniden adlandırıldı!")