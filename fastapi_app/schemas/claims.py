from pydantic import BaseModel, Field
from datetime import datetime

class ClaimData(BaseModel):
    claim_id: str
    provider_name: str
    patient_name: str
    amount: float = Field(gt=0, description="Amonut can not be zero or negetive")
    filing_day: datetime | None
    address: str | None
