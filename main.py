from youtube_transcript_api import YouTubeTranscriptApi
import pyttsx3
import tkinter as tk
from tkinter import scrolledtext, messagebox

def afficher_texte(texte):
    fenetre_texte = tk.Toplevel(root)
    fenetre_texte.title("Transcription traduite")
    fenetre_texte.geometry("600x400")

    zone_texte = scrolledtext.ScrolledText(fenetre_texte, wrap=tk.WORD)
    zone_texte.pack(expand=True, fill='both')
    zone_texte.insert(tk.END, texte)

def traiter_video():
    video_id = entry_id.get()
    sortie_audio = var_audio.get()

    if not video_id:
        messagebox.showerror("Erreur", "Veuillez entrer un ID de vidéo.")
        return

    engine = pyttsx3.init() if sortie_audio else None

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en'])
        translated_transcript = transcript.translate('fr')
        translated_content = translated_transcript.fetch()

        texte_complet = ""

        for entry in translated_content:
            text = f"{entry['start']:.2f} - {entry['start'] + entry['duration']:.2f}: {entry['text']}\n"
            texte_complet += text
            print(text)
            if sortie_audio:
                engine.say(entry['text'])
                engine.runAndWait()

        afficher_texte(texte_complet)

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("YouTube Transcript")
root.geometry("300x150")

# Champ de saisie pour l'ID de la vidéo
tk.Label(root, text="ID de la vidéo YouTube :").pack()
entry_id = tk.Entry(root, width=40)
entry_id.pack()

# Option pour la sortie audio
var_audio = tk.BooleanVar()
tk.Checkbutton(root, text="Sortie audio", variable=var_audio).pack()

# Bouton pour lancer le traitement
tk.Button(root, text="Traiter la vidéo", command=traiter_video).pack(pady=10)

root.mainloop()