from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI ()

@app.get ("/")
def demo ():
    return "hello world"