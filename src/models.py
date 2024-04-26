from pydantic import BaseModel, StrictStr, Field, field_validator, ValidationInfo, field_serializer
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
    mode: Mode | str = Mode.LIGHT # sometimes we are importing from a file so need to convert to the enum first
    instances_folder: str = './instances'
    mods_folder: str = './mods'
    check_for_update_on_start: bool = True

    @field_validator('mode')
    def check_valid_mode(cls, v: Mode | str, info: ValidationInfo) -> Mode:
        if isinstance(v, str):
            if v not in Mode:
                #in case we get an invalid mode from people tampering with the file, we will just reset it back to the default.
                return Mode.LIGHT
            return Mode[v]
        return v
    
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
    name: str 
    username: str
    version: SiegeVersions
    instance_directory: str
    siege_directory: str

    @field_validator('instance_directory', 'siege_directory')
    @classmethod
    def check_folder(cls, v: str, info: ValidationInfo) -> str:
        if not os.path.isdir(v):
            raise ValueError(f'The path for {info.field_name} must lead to an existing directory.')
        return v
    
    @field_serializer('version', when_used='json')
    def convert_version_to_str(version: SiegeVersions) -> str:
        return version.value
