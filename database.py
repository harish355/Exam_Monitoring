from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2 import service_account
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds=None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1Fv-h0PnjML7vv8tTyAmehig6GoUQNp8BoqClQkdJz90'
service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
sheet = service.spreadsheets()


def read(celll):
	result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=celll).execute()
	values=result.get('values',[])
	if values!=[]:
		return(values[0])
	else:
		pass


def write(data,cell):
	aoa=[[data]]
	request=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=cell,valueInputOption="USER_ENTERED",body={"values":aoa}).execute()
	print(request)