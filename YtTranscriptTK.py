from youtube_transcript_api import YouTubeTranscriptApi
import tkinter as tk
from tkinter import scrolledtext

def afficher_texte(texte):
    fenetre = tk.Tk()
    fenetre.title("Transcription traduite")
    fenetre.geometry("600x400")

    zone_texte = scrolledtext.ScrolledText(fenetre, wrap=tk.WORD)
    zone_texte.pack(expand=True, fill='both')
    zone_texte.insert(tk.END, texte)

    fenetre.mainloop()

# Menu interactif
video_id = input("Entrez l'ID de la vidéo YouTube : ")


try:
    # Récupération de la liste des transcriptions disponibles
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    # Sélection de la transcription (par défaut, la première disponible)
    transcript = transcript_list.find_transcript(['en'])

    # Traduction de la transcription en français
    translated_transcript = transcript.translate('fr')

    # Récupération du contenu traduit
    translated_content = translated_transcript.fetch()

    texte_complet = ""

    # Traitement de la transcription traduite
    for entry in translated_content:
        # text = f"{entry['start']:.2f} - {entry['start'] + entry['duration']:.2f}: {entry['text']}\n"
        text = f"{entry['text']}"
        texte_complet += text
        print(text)
        """if sortie_audio:
            engine.say(entry['text'])
            engine.runAndWait()"""


    # Affichage de la fenêtre avec le texte récupéré
    afficher_texte(texte_complet)
 

except Exception as e:
    print(f"Une erreur s'est produite : {e}")