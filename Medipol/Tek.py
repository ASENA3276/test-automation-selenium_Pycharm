import os
import pydicom
import imageio

import imageio


dicom_folder = "/Users/asena.karakas/Desktop/Medipol/DICOM"
frames = []

for root, dirs, files in os.walk(dicom_folder):
    for filename in sorted(files):
        if filename == ".DS_Store":  # macOS gizli dosyası atla
            continue
        filepath = os.path.join(root, filename)
        print(f"Dosya işleniyor: {filepath}")
        try:
            ds = pydicom.dcmread(filepath, force=True)
            if 'PixelData' in ds:
                img = ds.pixel_array
                frames.append(img)
                print(f"✅ Görüntü eklendi: {filename}")
            else:
                print(f"⚠️ PixelData yok: {filename}")
        except Exception as e:
            print(f"❌ Hata oluştu: {filename} -> {e}")

if frames:
    output_path = os.path.join(dicom_folder, "tum_goruntuler.mp4")
    imageio.mimsave(output_path, frames, fps=10)
    print(f"🎉 Video başarıyla oluşturuldu: {output_path}")
else:
    print("🚫 Hiçbir geçerli DICOM görüntüsü işlenemedi.")


