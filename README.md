## Game created in python with pygame inspired by Swords and Sandals

---
### GUIDELINES
#### ***1. Imports hierarchy***
*Modules should be imported from top as follows:*
- import complete built-ins modules
- specific objects from built-ins modules
- complete third-party libraries
- specific elements from third-party libraries
- complete project modules
- specific elements from project modules

Example:
```
import os
from math import atan

import pygame
from sqlalchemy import create_engine

import gui
from data.data_manager import EnvironmentDB
```
---