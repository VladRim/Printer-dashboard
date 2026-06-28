from sqlalchemy.orm import Session

from app.repositories.search_repository import SearchRepository


class SearchService:

    def __init__(self):
        self.repo = SearchRepository()

    def search(self, db: Session, text: str):

        result = self.repo.search(db, text)

        # будущая точка расширения:
        # - score ranking
        # - fuzzy search
        # - AI matching

        return result
