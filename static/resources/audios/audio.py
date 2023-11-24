from pytube import YouTube
import pandas as pd
video_link = "https://www.youtube.com/watch?v=_r9pWWYjBFw&list=PLp5zSGEKWyU6WmoXIS0bgnqp3dZHgPIeC"


# dataframe=pd.read_csv('static/resources/audios/audio.csv')
# for i in range(len(dataframe)):
#     video_link=dataframe['link'][i]
#     video=YouTube(video_link)
#     audio=video.streams.filter(only_audio=True,file_extension='mp4').first()
#     x=audio.download('static/resources/audios/audiofiles')
#     print(audio.title)

# dataframe=pd.read_csv('static/resources/audio.csv')
import os 
absoute_path=os.path.abspath('static/resources/audios/audiofiles')
relative_path='resources/audios/audiofiles' 
fullpath=os.path.join(absoute_path,relative_path)
print(fullpath)
