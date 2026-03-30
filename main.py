from fastapi import FastAPI, File, UploadFile, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel, Field, field_validator
from config.app import VIRUS_TOTAL_API_KEY
from service.virus_total import upload_file_to_virus_total, get_file_scan_report
from util.retry import retry

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

ALLOWED_TYPES = ["image/jpeg", "image/jpg",, "image/png", "application/pdf"]
MAX_FILE_SIZE = 10 * 1024 * 1024

@app.post("/file/scan/")
@limiter.limit("5/minute")
async def create_upload_file(file: UploadFile):
  if file.content_type not in ALLOWED_TYPES:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST
    )
  if file.size > MAX_FILE_SIZE:
    raise HTTPException(
      status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
    )
  upload_response = upload_file_to_virus_total(file)
  file_hash = upload_response.get("resource")
  report_response = retry(get_file_scan_report, "response_code", 1, delay=2, retries=100, file_hash=file_hash)
  return report_response