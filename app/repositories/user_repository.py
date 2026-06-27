from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):

    def __init__(self, session: Session):
        super().__init__(User, session)

    def get_by_username(self, username: str):
        return (
            self.session.query(User)
            .filter(User.username == username)
            .first()
        )
