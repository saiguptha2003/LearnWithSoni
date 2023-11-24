video=YouTube(video_link)
audio=video.streams.filter(only_audio=True,file_extension='mp4').first()
audio.download('static/resources')