from sqlalchemy.orm import Session

from app.models.manufacturer import Manufacturer
from app.repositories.base import BaseRepository


class ManufacturerRepository(BaseRepository[Manufacturer]):

    def __init__(self, session: Session):
        super().__init__(Manufacturer, session)

    def get_by_name(self, name: str):
        return (
            self.session.query(Manufacturer)
            .filter(Manufacturer.name.ilike(name))
            .first()
        )
