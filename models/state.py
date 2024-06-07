#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
from models.city import City


class State(BaseModel):
    """ State class """
    name = ""

    @property
    def cities(self):
        '''
        Returns the list of city objects from storage linked
        to the current state
        '''
        city_list = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if city.state == self.id:
                city_list.append(city)
        return city_list
