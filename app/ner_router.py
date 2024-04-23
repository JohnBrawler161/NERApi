from fastapi import APIRouter

from app.models import NERData
from app.ner_service import NERService

router = APIRouter(prefix="/nre")


@router.post("/")
async def process_nre(data: NERData) -> list[dict]:
    service = NERService()

    data = service.process(data)
    print(data)

    return data
