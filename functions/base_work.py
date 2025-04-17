import os
import re

from collections import defaultdict

from PySide6.QtCore import QObject, Signal, Slot


class BaseWork(QObject):
    """Base class for all work classes."""
    progress = Signal(int)
    status = Signal(str)
    finished = Signal()
    error = Signal(str)
    