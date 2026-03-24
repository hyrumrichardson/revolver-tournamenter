from google.oauth.service_account import Credentials
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = "revolverleague-674306930412.json"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

sheets_service = build("sheets", "v4", credentials=creds)
drive_service = build("drive", "v3", credentials=creds)

spreadsheet_body = {
    "properties": {"title": "My Python-Created Sheet"}
}

new_sheet = sheets_service.spreadsheets().create(
    body=spreadsheet_body,
    fields="spreadsheetId"
).execute()

spreadsheet_id = new_sheet["spreadsheetId"]
print("Spreadsheet ID:", spreadsheet_id)

print(f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}")