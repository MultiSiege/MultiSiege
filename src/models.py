from pydantic import BaseModel, field_validator, ValidationInfo, field_serializer
from constants import *
import os

#======================#
#GLOBAL SETTINGS MODELS#
#======================#

class AccountModel(BaseModel):
    username: str
    password: str

class FeaturesModel(BaseModel):
    mode: Mode = Mode.LIGHT
    instances_folder: str = os.path.join(os.getcwd(), 'instances')
    mods_folder: str = os.path.join(os.getcwd(), 'mods')
    check_for_update_on_start: bool = True
    
    @field_serializer('mode', when_used='json')
    def convert_mode_to_str(mode: Mode) -> str:
        return mode.value
    
    @field_validator('instances_folder', 'mods_folder')
    @classmethod
    def check_folder(cls, v: str, info: ValidationInfo) -> str:
        if not os.path.isdir(v):
            os.mkdir(v)
        return v

class GlobalSettingsModel(BaseModel):
    features: FeaturesModel = FeaturesModel()
    accounts: list[AccountModel] = []

#========================#
#INSTANCE SETTINGS MODELS#
#========================#

class InstanceSettingsModel(BaseModel):
    instance_name: str 
    username: str
    version: SiegeVersions
    
    @field_serializer('version', when_used='json')
    def convert_version_to_str(version: SiegeVersions) -> str:
        return version.value
