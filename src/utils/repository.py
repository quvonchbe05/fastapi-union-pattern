from abc import ABC, abstractmethod

from sqlalchemy import select
from src.db.db import async_session_maker

class AbstractRepository(ABC):
    @abstractmethod 
    async def find_all():
        raise NotImplementedError
    
    
class SQLAlchemyRepository(AbstractRepository):
    model = None
    
    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            response = await session.scalars(stmt)
            return response