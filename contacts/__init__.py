"""
Contacts package

Exports Contact and ContactManager class
"""

from .models import Contact
from .manager import ContactManager

__all__ = ["Contact", "ContactManager"]