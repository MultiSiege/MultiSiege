from .Main.main import MainWindow
from .NewInstance.new_instance import NewInstance

#explicitly declare the outwards facing API of this module
__all__ = [
    "MainWindow",
    "NewInstance"
]