from fastapi import FastAPI, File, UploadFile
from config.app import VIRUS_TOTAL_API_KEY
from service.virus_total import upload_file_to_virus_total, get_file_scan_report
from util.retry import retry

app = FastAPI()

@app.post("/file/scan/")
async def create_upload_file(file: UploadFile):
  upload_response = upload_file_to_virus_total(file)
  file_hash = upload_response.get("resource")
  report_response = retry(get_file_scan_report, "response_code", 1, delay=2, retries=100, file_hash=file_hash)
  return report_response