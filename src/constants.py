import enum

GLOBAL_SETTINGS = './global_settings.json'

class MyEnumMeta(enum.EnumMeta): 
    def __contains__(cls, item): 
        try:
            cls(item)
        except ValueError:
            return False
        else:
            return True

class SiegeVersions(enum.Enum, metaclass=MyEnumMeta):
    """
    Enum for all of the siege versions available to be downloaded.
    """
    VANILLA = "Y1S0"
    BLACK_ICE = "Y1S1"
    DUST_LINE = "Y1S2"
    SKULL_RAIN = "Y1S3"
    RED_CROW = "Y1S4"
    VELVET_SHELL = "Y2S1"
    HEALTH = "Y2S2"
    BLOOD_ORCHID = "Y2S3"
    WHITE_NOISE = "Y2S4"
    CHIMERA = "Y3S1"
    PARABELLUM = "Y3S2"
    GRIM_SKY = "Y3S3"
    WIND_BASTION = "Y3S4"
    BURNT_HORIZON = "Y4S1"
    PHANTOM_SIGHT = "Y4S2"
    EMBER_RISE = "Y4S3"
    SHIFTING_TIDES = "Y4S4"
    VOID_EDGE = "Y5S1"
    STEEL_WAVE = "Y5S2"
    SHADOW_LEGACY = "Y5S3"
    NEON_DAWN = "Y5S4"
    CRIMSON_HEIST = "Y6S1"
    NORTH_STAR = "Y6S2"
    CRYSTAL_GUARD = "Y6S3"
    HIGH_CALIBRE = "Y6S4"

class SiegeDepots(enum.IntEnum):
    pass

class Status(enum.Enum):
    """
    Enum to return status codes for if the function was successful.
    """
    SUCCESS = 0
    FAIL = 1

class LogLevel(enum.Enum):
    """
    List of log levels that will be used in the program.
    """
    INFO = "INFO"
    DEBUG = "DEBUG"
    WARNING = "WARNING"
    ERROR = "ERROR"

class Mode(enum.Enum, metaclass=MyEnumMeta):
    """
    Enum for the mode the program is in (light or dark mode)
    """
    LIGHT = "LIGHT"
    DARK = "DARK"