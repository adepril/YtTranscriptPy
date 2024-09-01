from youtube_transcript_api import YouTubeTranscriptApi

# ID de la vidéo YouTube (extrait de l'URL après "v=")
video_id = "59-Q_Crg5wE"

try:
    # Récupération de la transcription
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Affichage de la transcription
    for entry in transcript:
        print(
            f"{entry['start']:.2f} - {entry['start'] + entry['duration']:.2f}: {entry['text']}"
        )

except Exception as e:
    print(f"Une erreur s'est produite : {e}")
