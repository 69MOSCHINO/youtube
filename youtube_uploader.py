def upload_video(video_path, title, is_story):
    print(f"[Mock upload] Carico '{video_path}' su YouTube come {'Storia' if is_story else 'Motivazione'} con titolo: {title[:60]}...")
    # Puoi inserire qui l'integrazione con YouTube Data API