from pydantic import BaseModel, field_validator, ValidationInfo, field_serializer
from constants import *
import os

#======================#
#GLOBAL SETTINGS MODELS#
#======================#

class AccountModel(BaseModel):
    username: str
    password: str

    @field_validator('username', 'password')
    def check_alphanumeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            # info.field_name is the name of the field being validated
            is_alphanumeric = v.replace(' ', '').isalnum()
            assert is_alphanumeric, f'{info.field_name} must be alphanumeric'
        return v

class FeaturesModel(BaseModel):
    mode: Mode = Mode.LIGHT
    instances_folder: str = './instances'
    mods_folder: str = './mods'
    check_for_update_on_start: bool = True
    
    @field_serializer('mode', when_used='json')
    def convert_mode_to_str(mode: Mode) -> str:
        return mode.value
    
    @field_validator('instances_folder', 'mods_folder')
    @classmethod
    def check_folder(cls, v: str, info: ValidationInfo) -> str:
        if not os.path.isdir(v):
            raise ValueError(f'The path for {info.field_name} must lead to an existing directory.')
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
