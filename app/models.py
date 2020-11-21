from typing import Dict, List, Optional
from enum import Enum
from pydantic import BaseModel, Schema

class Input(BaseModel):
    message: str

class Output(BaseModel):
    output: int