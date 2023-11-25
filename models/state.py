from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete-orphan', backref='state')

    # Getter attribute for FileStorage
    @property
    def cities(self):
        """Returns the list of City instances with state_id equals to the current State.id"""
        from models import storage
        city_objs = storage.all(City)
        return [city for city in city_objs.values() if city.state_id == self.id]
