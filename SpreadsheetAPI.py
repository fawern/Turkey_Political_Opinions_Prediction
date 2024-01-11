import pandas as pd 
import gspread


class SheetData:
    def __init__(self, json_file, form_name, works_sheet, columns, data_path):
        self.json_file = json_file
        self.form_name = form_name
        self.works_sheet = works_sheet
        self.columns = columns
        self.data_path = data_path

    def getData(self):
        sa = gspread.service_account(filename=self.json_file)

        wb = sa.open(self.form_name)

        ws = wb.worksheet(self.works_sheet)

        data = pd.DataFrame(ws.get_all_records())
        
        data.columns = self.columns

        data.to_csv(self.data_path, index=False)
    
