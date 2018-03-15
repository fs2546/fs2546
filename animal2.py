#! /usr/bin/env python3
class Animal(object):
  owner = 'jack'
  def __init__(self,name):
    self._name = name
  @classmethod 
  def get_owner(cls):
    return cls.owner 
  def get_name(self):
    return self._name
  def set_name(self, value):
    self._name = value
  def make_sound(self):
    pass
class Dog(Animal):
  def make_sound(self):
    print(self.get_name() + ' ' + 'is making sound wang wang wang')
class Cat(Animal):
  def make_sound(self):
    print(self.get_name() + ' ' + 'is making sound miu miu miu')

animals = [Dog('wangcai'), Cat('Kitty'), Dog('mark'),Cat('Betty')]
for animal in animals:
  animal.make_sound()
print(Animal.get_owner())
print(Cat.get_owner())
