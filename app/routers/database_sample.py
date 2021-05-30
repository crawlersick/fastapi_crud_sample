from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from ..tables.sampledbobj import sampledbobj
from ..dataconfig import get_db
import logging


router = APIRouter()


@router.get("/test1/")
async def test1(db: Session = Depends(get_db)):
    res = db.query(sampledbobj).all()
    logging.info(res)

    return [{"username": "Rick"}, {"username": "Morty"}]

