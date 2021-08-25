import time
import math
import os
import random
import re
import sys


class Agent:

    '''
    Constructor of the Agent class
    '''
    def __init__(self, id, name, version, os, inventory, modules, status):
        self.setId(id)
        self.setName(name)
        self.setVersion(version)
        self.setOs(os)
        self.setInventory(inventory)
        self.setModules(modules)
        self.setStatus(status)

    '''
    Fuction to set id var
    param id
    '''
    def setId(self, id):
        self._id = id
    
    '''
    Fuction to get id var
    return id
    '''
    def getId(self):
        return self._id

    '''
    Fuction to set name var
    param name
    '''
    def setName(self, name):
        self._name = name

    '''
    Fuction to get name var
    return name
    '''
    def getName(self):
        return self._name

    '''
    Fuction to set version var
    param version
    '''
    def setVersion(self, version):
        self._version = version

    '''
    Fuction to get version var
    return version
    '''
    def getVersion(self):
        return self._version

    '''
    Fuction to set os var
    param os
    '''
    def setOs(self, os):
        self._os = os

    '''
    Fuction to get os var
    return os
    '''
    def getOs(self):
        return self._os

    '''
    Fuction to set inventory var
    param inventory
    '''
    def setInventory(self, inventory):
        self._inventory = inventory

    '''
    Fuction to get inventory var
    return inventory
    '''
    def getInventory(self):
        return self._inventory

    '''
    Fuction to set modules var
    param modules
    '''
    def setModules(self, modules):
        self._modules = modules

    '''
    Fuction to get modules var
    return modules
    '''
    def getModules(self):
        return self._modules

    '''
    Fuction to set status var
    param status
    '''
    def setStatus(self, status):
        self._status = status

    '''
    Fuction to get status var
    return status
    '''
    def getStatus(self):
        return self._status


    '''
    Fuction to print agent information
    '''
    def showAttr(self):
        print(f'Id: {self.getId()}')
        print(f'Name: {self.getName()}')
        print(f'Version: {self.getVersion()}')
        print(f'Os: {self.getOs()}')        
        print(f'Inventory: {self.getInventory()}')
        print(f'Modules: {self.getModules()}')
        print(f'Status: {self.getStatus()}')
        
                        



