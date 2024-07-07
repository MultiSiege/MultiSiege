import sys
import os

if os.path.exists(os.path.join(os.getcwd(), 'src')): #if we have compiled there is no need to do this.
    sys.path.append(os.path.join(os.getcwd(), 'src'))
    sys.path.append(os.path.join(os.getcwd(), 'src', 'widgets'))

from .Main.main import MainWindow
from .NewInstance.new_instance import NewInstance
from .InstanceSettings.instance_settings import InstanceSettingsWindow
from .Help.help import HelpWindow
from .GlobalSettings.global_settings import GlobalSettingsWindow
from .Error.error import ErrorWindow
from .Delete.delete import DeleteWindow
from .CreateShortcut.create_shortcut import CreateShortcutWindow
from .ChooseAccount.choose_account import ChooseAccountWindow
from .AddSteamAccount.add_steam_account import AddSteamAccountWindow

#explicitly declare the outwards facing API of this module
__all__ = [
    MainWindow.__name__,
    NewInstance.__name__,
    InstanceSettingsWindow.__name__,
    HelpWindow.__name__,
    GlobalSettingsWindow.__name__,
    ErrorWindow.__name__,
    DeleteWindow.__name__,
    CreateShortcutWindow.__name__,
    ChooseAccountWindow.__name__,
    AddSteamAccountWindow.__name__
]