from sqlalchemy.orm import Session

from app.models.location import Location
from app.repositories.base import BaseRepository


class LocationRepository(BaseRepository[Location]):

    def __init__(self, session: Session):
        super().__init__(Location, session)

    def search(self, query: str):
        return (
            self.session.query(Location)
            .filter(
                Location.room.ilike(f"%{query}%")
                | Location.building.ilike(f"%{query}%")
            )
            .all()
        )
