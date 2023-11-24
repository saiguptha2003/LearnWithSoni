def getParagraphDetails(id):
    try:
        print(id)
        dataframe=pd.read_csv(r'static\resources\paragraph.csv',encoding= 'unicode_escape')
        
        dataframe=dataframe[dataframe['paragraph_id']==id.strip()]
        return dataframe.to_dict('records')
    except:
        print("not found")
        