#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog:
    
    def sound(self):
        return 'Bark'
class Cat:

    def sound(self):
        return 'Meow'
