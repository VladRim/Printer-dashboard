from sqlalchemy.orm import Session

from app.models.department import Department
from app.repositories.base import BaseRepository


class DepartmentRepository(BaseRepository[Department]):

    def __init__(self, session: Session):
        super().__init__(Department, session)

    def get_by_name(self, name: str):
        return (
            self.session.query(Department)
            .filter(Department.name.ilike(name))
            .first()
        )
