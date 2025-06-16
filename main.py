from story_generator import generate_story_or_quote
from text_to_speech import generate_audio
from video_generator import generate_video
from youtube_uploader import upload_video

def main():
    print("🎬 Generazione contenuto...")
    text, is_story = generate_story_or_quote()
    print(f"✅ Testo generato: {text}")

    audio_path = generate_audio(text)
    print(f"🎤 Audio creato: {audio_path}")

    video_path = generate_video(text, audio_path)
    print(f"📽️ Video generato: {video_path}")

    upload_video(video_path, text, is_story)
    print("📤 Video caricato su YouTube Shorts!")

if __name__ == "__main__":
    main()
