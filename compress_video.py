#!/usr/bin/env python3
import os
import sys

# Asegurarse que moviepy está instalado
try:
    from moviepy.editor import VideoFileClip
except ImportError:
    print("Instalando moviepy...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "moviepy", "-q"])
    from moviepy.editor import VideoFileClip

video_path = r"D:\Nimo Main\game20\TemplateData\loading.mp4"
output_path = r"D:\Nimo Main\game20\TemplateData\loading_compressed.mp4"

print("Cargando video...")
clip = VideoFileClip(video_path)
print(f"Video: {clip.duration:.1f}s, {clip.fps} fps, {clip.size}")

orig_size = os.path.getsize(video_path) / (1024 * 1024)
print(f"Tamaño original: {orig_size:.2f} MB")

print("Comprimiendo (esto puede tomar un tiempo)...")
# Comprimir a calidad media para web
clip.write_videofile(
    output_path, 
    codec='libx264',
    audio_codec='aac',
    bitrate="1500k",
    verbose=False,
    logger=None
)
clip.close()

if os.path.exists(output_path):
    comp_size = os.path.getsize(output_path) / (1024 * 1024)
    reduction = ((orig_size - comp_size) / orig_size) * 100
    print(f"\n✓ Comprimido: {comp_size:.2f} MB (reducción: {reduction:.1f}%)")
    
    # Reemplazar original
    backup_path = video_path + ".backup"
    os.rename(video_path, backup_path)
    os.rename(output_path, video_path)
    print(f"✓ Archivos reemplazados")
