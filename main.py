from pytube import YouTube
import easygui

def Download(link):
    youtubeObject = YouTube(link)
    youtubeMedia = youtubeObject.streams.get_audio_only()
    youtubeMedia.download(easygui.diropenbox("Seleccione el directorio donde lo guardara", "Guardar"))

link = easygui.enterbox("Ingrese el link del video a convertir: ", "YouTube audio download")
Download(link)