import gspread

googleSheet_name = 'Test_sheet'
workbook_cred = "./auth.json"

spreadSheet_name = 'Sheet1'

def GoogleSheets(data, cread_file, googleSheet_name, spreadSheet_name):
    gc = gspread.service_account(filename = cread_file)
    sh = gc.open(googleSheet_name).worksheet(spreadSheet_name)
    sh.append_row(str(data['Url']), str(data['Link']), str(data['Status']))
    print(sh)
    return

