from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.search_service import SearchService

router = APIRouter(prefix="/search", tags=["Search"])

service = SearchService()


@router.get("/")
def search(q: str, db: Session = Depends(get_db)):
    return service.search(db, q)
