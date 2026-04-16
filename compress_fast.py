#!/usr/bin/env python3
import os
import sys
import moviepy

def compress_video_fast(input_path, output_path, target_size_mb=2.0):
    """Comprimir video rápidamente a tamaño objetivo"""

    # Cargar video
    clip = moviepy.VideoFileClip(input_path)
    orig_size = os.path.getsize(input_path) / (1024 * 1024)

    print(f"Video original: {orig_size:.2f} MB")
    print(f"Duración: {clip.duration:.1f}s, FPS: {clip.fps}, Resolución: {clip.size}")

    # Calcular bitrate objetivo (en kbps)
    duration_seconds = clip.duration
    target_size_bytes = target_size_mb * 1024 * 1024
    target_bitrate = int((target_size_bytes * 8) / duration_seconds / 1000)

    print(f"Bitrate objetivo: {target_bitrate} kbps")

    # Comprimir con bitrate calculado
    clip.write_videofile(
        output_path,
        codec='libx264',
        audio_codec='aac',
        bitrate=f"{target_bitrate}k",
        logger=None
    )

    clip.close()

    # Verificar resultado
    if os.path.exists(output_path):
        new_size = os.path.getsize(output_path) / (1024 * 1024)
        reduction = ((orig_size - new_size) / orig_size) * 100
        print(f"✓ Video comprimido: {new_size:.2f} MB ({reduction:.1f}% reducción)")
        return True

    return False

if __name__ == "__main__":
    video_path = r"D:\Nimo Main\game20\TemplateData\loading.mp4"
    output_path = r"D:\Nimo Main\game20\TemplateData\loading_fast.mp4"

    if compress_video_fast(video_path, output_path, target_size_mb=1.8):
        # Reemplazar original
        backup_path = video_path + ".backup"
        if not os.path.exists(backup_path):
            os.rename(video_path, backup_path)
        os.rename(output_path, video_path)
        print("✓ Video reemplazado exitosamente")
    else:
        print("✗ Error en compresión")