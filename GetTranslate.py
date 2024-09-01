from youtube_transcript_api import YouTubeTranscriptApi
import pyttsx3

# ID de la vidéo YouTube (extrait de l'URL après "v=")
video_id = "59-Q_Crg5wE"

# Initialisation du moteur de synthèse vocale
engine = pyttsx3.init()

try:
    # Récupération de la liste des transcriptions disponibles
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    # Sélection de la transcription (par défaut, la première disponible)
    transcript = transcript_list.find_transcript(['en'])  # ou une autre langue si disponible

    # Traduction de la transcription en français
    translated_transcript = transcript.translate('fr')

    # Récupération du contenu traduit
    translated_content = translated_transcript.fetch()

    # Affichage et lecture de la transcription traduite
    for entry in translated_content:
        text = f"{entry['start']:.2f} - {entry['start'] + entry['duration']:.2f}: {entry['text']}"
        print(text)
        engine.say(entry['text'])
        engine.runAndWait()

except Exception as e:
    print(f"Une erreur s'est produite : {e}")