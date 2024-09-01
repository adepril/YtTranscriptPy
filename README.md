Python script that retrieves the transcription of a youtube video by giving its ID.
This transcription is translated in French (configure other language) and TTS module spoken aloud.


main.py :
This script provides a user-friendly graphical interface to retrieve, translate, and display the transcript of a YouTube video. 
Users can input the video ID, choose whether to enable audio output, and obtain the transcript translated into French. 
The script utilizes the YouTube Transcript API to fetch the transcript, translates it, and offers a text-to-speech option. 
It's a convenient tool for quickly accessing YouTube video content in a language different from the original, making it useful for language learners, researchers, or anyone needing quick access to video content in a translated form.


YtTranscriptTK.py : 
This Tkinter implementation allows us to enter the youtube video ID and display the transcription in a window.

YtTranscriptTK_audio.py : 
This script allows us to enter the youtube video ID and display the transcription in a window and speak aloud with a TTS module.