"""
Contacts package

Exports Contact and ContactManager class
"""

from .models import Contact
from .manager import ContactManager
from .validators import *

__all__ = ["Contact", "ContactManager"]