"""
 CREATED BY: Benjamin Hamlin
 Chapter 3 Question 6
 "Animal Shelter"
 PROMPT:
 An animal shelter, which holds only dogs and cats, operates on a strictly FIFO
 basis. People must adopt either the oldest (based on arrival time) of all animals
 or the oldest cat or dog. Create the data structure to maintain this sstem and implement
 operations enqueue, dequeueAny, dequeueDog, dequeueCat. You may use built in
 LinkedList data structures
 DATE: 12/10/2019
"""

import unittest

class Animal(object):
    def __init__(self,name):
        self.name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self,name):
        self.name = name

class ShelterStack:
    def __init__(self):
        self.q = []
        self.top = 0
        self.dogIndex = None
        self.catIndex = None

    def enqueue(self, animal: Animal):
        if len(self.q) != 0:
            self.top += 1
        if isinstance(animal, Cat) and self.catIndex is None:
            self.catIndex = self.top
        elif isinstance(animal, Dog) and self.dogIndex is None:
            self.dogIndex = self.top
        self.q.append(animal)

    def dequeueAny(self):
        temp = self.q.pop(0)
        if isinstance(temp, Cat):
            cur = self.catIndex
            while not isinstance(self.q[cur], Cat):
                cur += 1
            self.catIndex = cur
        if isinstance(temp, Dog):
            cur = self.dogIndex
            while not isinstance(self.q[cur], Cat):
                cur += 1
            self.dogIndex = cur
        return temp

    def dequeueCat(self):
        temp = None
        if self.catIndex is not None:
            temp = self.q.pop(self.catIndex)
            if temp is Cat:
                cur = self.catIndex
                while not isinstance(self.q[cur], Cat):
                    cur += 1
                self.catIndex = cur
        return temp

    def dequeueDog(self):
        temp = None
        if self.dogIndex is not None:
            temp = self.q.pop(self.dogIndex)
            if temp is Dog:
                cur = self.dogIndex
                while not isinstance(self.q[cur], Cat):
                    cur += 1
                self.dogIndex = cur
        return temp

class TestP6(unittest.TestCase):
    def setUp(self):
        self.q = ShelterStack()

    def tearDown(self):
        self.q = None

    def test_p6_enqueue(self):
        dog1 = Dog("Fluffy")
        dog2 = Dog("Peanut")
        cat1 = Cat("Boots")
        dog3 = Dog("Kaylee")
        self.q.enqueue(dog1)
        self.q.enqueue(dog2)
        self.q.enqueue(cat1)
        self.q.enqueue(dog3)
        self.assertEqual(self.q.q, [dog1,dog2,cat1,dog3])

    def test_p6_dequeueAny(self):
        dog1 = Dog("Fluffy")
        dog2 = Dog("Peanut")
        cat1 = Cat("Boots")
        dog3 = Dog("Kaylee")
        self.q.enqueue(dog1)
        self.q.enqueue(dog2)
        self.q.enqueue(cat1)
        self.q.enqueue(dog3)
        self.assertEqual(self.q.q, [dog1,dog2,cat1,dog3])
        self.assertEqual(self.q.dequeueAny(), dog1)
        self.assertEqual(self.q.q, [dog2,cat1,dog3])

    def test_p6_dequeueDog(self):
        dog1 = Dog("Fluffy")
        dog2 = Dog("Peanut")
        cat1 = Cat("Boots")
        dog3 = Dog("Kaylee")
        self.q.enqueue(dog1)
        self.q.enqueue(dog2)
        self.q.enqueue(cat1)
        self.q.enqueue(dog3)
        self.assertEqual(self.q.q, [dog1,dog2,cat1,dog3])
        self.assertEqual(self.q.dequeueDog(), dog1)
        self.assertEqual(self.q.q, [dog2,cat1,dog3])
        self.assertEqual(self.q.dequeueDog(), dog2)

    def test_p6_dequeueCat(self):
        dog1 = Dog("Fluffy")
        dog2 = Dog("Peanut")
        cat1 = Cat("Boots")
        dog3 = Dog("Kaylee")
        self.q.enqueue(dog1)
        self.q.enqueue(dog2)
        self.q.enqueue(cat1)
        self.q.enqueue(dog3)
        self.assertEqual(self.q.q, [dog1,dog2,cat1,dog3])
        self.assertEqual(self.q.dequeueCat(), cat1)
        self.assertEqual(self.q.q, [dog1,dog2,dog3])
