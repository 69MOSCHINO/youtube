from moviepy.editor import *
import random

def generate_video(text, audio_path, output_path="final_video.mp4"):
    clip = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=10)
    audio = AudioFileClip(audio_path)
    clip = clip.set_audio(audio)

    txt_clip = TextClip(text, fontsize=70, color='white', size=(1000, None), method='caption', align='center')
    txt_clip = txt_clip.set_position('center').set_duration(audio.duration)

    final = CompositeVideoClip([clip, txt_clip])
    final.write_videofile(output_path, fps=24, audio_codec='aac')
    return output_path