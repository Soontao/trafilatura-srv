from fastapi import FastAPI
from trafilatura import fetch_url, extract
from dataclasses import dataclass
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def index():
  return {"service": "trafilatura service", "status": 200}


class ExtractOptions(BaseModel):
  url: str


class ExtractResponse(BaseModel):
  extracted: str


@app.post("/extract")
async def extract_text(options: ExtractOptions) -> ExtractResponse:
  downloaded = fetch_url(options.url)
  result = extract(downloaded)
  return ExtractResponse(extracted=result)
