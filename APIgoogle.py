import pandas as pd
import csv
import gspread


# https://docs.google.com/forms/d/1Lkjwpv1W9-mMo3JdeEEylN6S93gHUZQUFw8GXppT3nw/edit

sa = gspread.service_account(filename="./data/secimanket-b6fdb3dc03a2.json")

wb = sa.open("Secim")

ws = wb.worksheet("Form Yanıtları 1")

all_rows = ws.get_all_records()

googledf = pd.read_csv("./data/googleAPI.csv")

googledf_list = []

for i in range(len(googledf)):
    googledf_list.append(googledf["Timestamp"][i].split(" ")[1])


googledf_list_date = []

for i in range(len(googledf)):
    googledf_list_date.append(googledf["Timestamp"][i].split(" ")[0])


for row in range(0, len(all_rows)):
    time = (all_rows[row]["Tarih"],)
    gender = (all_rows[row]["Cinsiyet ?"],)
    age = (all_rows[row]["Yas ?"],)
    region = (all_rows[row]["Coğrafi bölge ?"],)
    education = (all_rows[row]["Eğitim ?"],)
    qst1 = (all_rows[row]["Ekonomik durumumuzun iyi olduğunu düşünüyor musunuz?"],)
    qst2 = (all_rows[row]["Eğitimde reforma ihtiyaç var mı?"],)
    qst3 = (
        all_rows[row][
            "Özelleştirmelerin ( örneğin devlet kurumlarının özel sektöre satılması veya devredilmesi  ) geri alınmasını destekler misiniz?"
        ],
    )
    qst4 = (
        all_rows[row][
            "Devletin bazı suçlar için idam gibi cezaları kullanması gerektiğini düşünüyor musunuz?"
        ],
    )
    qst5 = (all_rows[row]["Gazetecilerimizi yeterince tarafsız buluyor musunuz?"],)
    qst6 = (
        all_rows[row][
            "22:00'den sonra alkollü içki satışının yasaklanmasını destekliyor musunuz?"
        ],
    )
    qst7 = (all_rows[row]["Laik bir devlette yaşamak istiyor musunuz?"],)
    qst8 = (all_rows[row]["Kürtaj yasağını destekliyor musunuz?"],)
    qst9 = (
        all_rows[row][
            "Olağanüstü halin (OHAL) özgürlükleri kısıtladığını düşünüyor musunuz?"
        ],
    )
    qst10 = (all_rows[row]["Parlamentoya yeni bir parti girmesini ister misiniz?"],)
    party = (all_rows[row]["Hangi siyasi partiyi destekliyorsunuz ? "],)

    added_row = [
        time[0],
        gender[0],
        age[0],
        region[0],
        education[0],
        qst1[0],
        qst2[0],
        qst3[0],
        qst4[0],
        qst5[0],
        qst6[0],
        qst7[0],
        qst8[0],
        qst9[0],
        qst10[0],
        party[0],
    ]

    if time[0].split(" ")[1] not in googledf_list:
        with open(
            "./data/googleAPI.csv", mode="a", encoding="utf-8", newline="\n"
        ) as file:
            opinion = csv.writer(file)
            opinion.writerow(added_row)
