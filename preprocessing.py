import numpy as np 
import pandas as pd



class Tokenizer:

    def __init__(self, data):
        self.data = data 

    def trToEn(self):
        mappings = {
            ("Evet","Hayır") : ("Yes","No"), 
            ("Erkek","Kadın") : ("Male","Female"),
            ("Marmara","Ege","Karadeniz","Akdeniz","İç Anadolu", "Doğu Anadolu", "Güneydoğu") : 
                    ("Marmara","Aegean","Black Sea","Mediterrenian","Central Anatolia","Eastern Anatolia","Southeast"), 
            ("İlkokul","Ortaokul","Lise","Ön Lisans","Lisans", "Lisans Üstü") : 
                    ("Primary School","Middle School","High School","Associate's Degree","University","Master's Degree"), 
        }
        
        for old_values, new_values in mappings.items():

            self.data.replace(old_values, new_values, inplace = True)
        return self.data 
    
    def categoricalToNumerical(self):
        self.data['Gender'].replace(
            {'Male' : 0, 'Female' : 1}, inplace=True
        )
        self.data['Region'].replace(
            {
                'Marmara' : 0,
                'Southeast' : 1,
                'Mediterrenian' : 2, 
                'Eastern Anatolia' : 3,
                'Central Anatolia' : 4,
                'Black Sea' : 5,
                'Aegean' : 6
            }, inplace=True
        )
        self.data['Education'].replace(
            {
                'University' : 0 , 
                'High School' : 1, 
                "Associate's Degree" : 2, 
                "Master's Degree" : 3, 
                'Primary School' : 4,
                'Middle School': 5
            }, inplace=True
        )
        self.data['Party'].replace({'IYI PARTI' : 0 , 'AKP' : 1 , 'DIĞER' : 2 , 'HDP' : 3 , 'CHP' : 4 , 'MHP' : 5}, inplace=True)
        self.data['Age'].replace(
            {
                '0-18' : 0,
                '18-30' : 1,
                '30-50' : 2,
                '50-60' : 3,
                '60+' : 4
            }, inplace=True
        )
        for quiestion in self.data.iloc[:, 4:14]:
            self.data[quiestion].replace({'Yes' : 1, 'No' : 0}, inplace=True)    
        
        return self.data


class One_Hot_Encoder:

    def __init__(self, data):
        self.data = data
