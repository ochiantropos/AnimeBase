from kivy.uix.screenmanager import Screen
from abc import abstractmethod,ABC

import sys, os.path
pool_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/pool/')
main_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/pool/main/')

sys.path.append(pool_dir)
sys.path.append(main_dir)

from header_pool import HeaderPool
from menu_pool import MenuPool
from main_find_people_pool import MainFindPeoplePool

class AbstructFindPeopleScreen(ABC):
    pass
        

class FindPeopleScreen(Screen):
    pass