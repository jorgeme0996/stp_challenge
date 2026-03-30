from config.app import VIRUS_TOTAL_API_KEY
from fastapi import UploadFile
import requests

def upload_file_to_virus_total(file: UploadFile):
  url = "https://www.virustotal.com/vtapi/v2/file/scan"

  files = { "file": file.file }
  headers = {
    "accept": "application/json"
  }

  params = {
    "apikey": VIRUS_TOTAL_API_KEY
  }

  response = requests.post(url, files=files, headers=headers, params=params)
  return response.json()

def get_file_scan_report(file_hash: str):
  url = "https://www.virustotal.com/vtapi/v2/file/report"
  params = {
    "apikey": VIRUS_TOTAL_API_KEY,
    "resource": file_hash
  }
  response = requests.get(url, params=params)
  return response.json()