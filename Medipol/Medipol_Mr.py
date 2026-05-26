import os
import pydicom
import imageio
import cv2  # pip install opencv-python

def to_uint8(img):
    img = img.astype(float)
    img = (img - img.min()) / (img.max() - img.min())  # normalize 0-1 arası
    img = (img * 255).astype('uint8')
    return img

dicom_folder = "/Users/asena.karakas/Desktop/Medipol/DICOM"
frames = []
ref_shape = None

for root, dirs, files in os.walk(dicom_folder):
    for filename in sorted(files):
        if filename == ".DS_Store":
            continue
        filepath = os.path.join(root, filename)
        print(f"Dosya işleniyor: {filepath}")
        try:
            ds = pydicom.dcmread(filepath, force=True)
            if 'PixelData' in ds:
                img = ds.pixel_array

                if ref_shape is None:
                    ref_shape = img.shape  # ilk görüntünün boyutunu al
                else:
                    # boyut farklı ise resize et
                    if img.shape != ref_shape:
                        img = cv2.resize(img, (ref_shape[1], ref_shape[0]))

                img = to_uint8(img)  # uint8'e dönüştür
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

