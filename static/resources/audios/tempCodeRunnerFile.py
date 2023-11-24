dataframe=pd.read_csv('static/resources/audios/audio.csv')
# for i in range(len(dataframe)):
#     video_link=dataframe['link'][i]
#     video=YouTube(video_link)
#     audio=video.streams.filter(only_audio=True,file_extension='mp4').first()
#     x=audio.download('static/resources/audios/audiofiles')
#     print(audio.title)