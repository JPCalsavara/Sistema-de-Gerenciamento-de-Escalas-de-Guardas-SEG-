import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Autenticação
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("googleCredentions.json", scope)
client = gspread.authorize(creds)
spreadsheet_id="1Z5f842pF-kbhgB3BgoC645gjJZhA465UPEI7cDFViZE"

# Acessar a planilha
spreadsheet = client.open_by_key(spreadsheet_id)
print("Conectado com sucesso!")
