import pandas as pd

data = [['id=com.whatsapp',"http://www.whatsapp.com/legal/#Privacy"],['id=com.instagram.android',"http://help.instagram.com/"],
        ['id=com.netflix.mediaclient',"http://www.netflix.com/privacy"],['id=com.disney.disneyplus',"https://privacy.thewaltdisneycompany.com/en/current-privacy-policy/"],
        ['id=com.amazon.imdb.tv.mobile.app',"https://www.amazon.com/gp/help/customer/display.html?nodeId=201909010&pop-up=1"],['id=com.tubitv',"https://tubitv.com/privacy.html"],
        ['id=com.whatsapp',"http://www.whatsapp.com/legal/#Privacy"],['id=com.instagram.android',"http://help.instagram.com/"],
        ['id=com.amazon.avod.thirdpartyclient',"http://www.amazon.com/gp/help/customer/display.html?nodeId=468496"],['id=com.hulu.plus',"https://www.hulu.com/privacy"]]

df = pd.DataFrame(data,columns=['ID','URL'],dtype=float)
df1 =df.to_csv('sample.csv')
# print(df)
# print(df.loc[[1]])