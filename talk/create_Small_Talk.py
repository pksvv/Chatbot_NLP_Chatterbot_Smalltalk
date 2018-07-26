# -*- coding: utf-8 -*-
import json
import pandas as  pd


def main():

 with open('SmallTalk.json', encoding='utf-8') as json_data:
    data = json.load(json_data)
    print(data)
    
 smalltalks=pd.read_excel("SmallTalk.xlsx")

 response = []
 for index, row in smalltalks.iterrows():

   response.append(data[row['Answer']])

 smalltalks = smalltalks.assign(responses = response)

 print (smalltalks.head())

 smalltalks.to_excel('responses.xlsx')

 data = {}
 values = []

 for index, row in smalltalks.iterrows():
      for item in row['responses']:
        value = '["' + str(row['Question']) + '" , "' + item + '"],'

        values.append (value)

 data['conversations'] = str(values)
 json_data = json.dumps(data)
   
 file = open('chatbot.json','w') 
 
 file.write(str(json_data)) 

 file.close() 

if __name__=='__main__':
    main()

