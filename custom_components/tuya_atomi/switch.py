
"""Support for Tuya switches."""
from __future__ import annotations


from typing import Any


from tuya_iot import TuyaDevice, TuyaDeviceManager


from homeassistant.components.switch import (
    SwitchDeviceClass,
    SwitchEntity,
    SwitchEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback


from . import HomeAssistantTuyaData
from .base import TuyaEntity
from .const import DOMAIN, TUYA_DISCOVERY_NEW, DPCode


# All descriptions can be found here. Mostly the Boolean data types in the
# default instruction set of each category end up being a Switch.
# https://developer.tuya.com/en/docs/iot/standarddescription?id=K9i5ql6waswzq
SWITCHES: dict[str, tuple[SwitchEntityDescription, ...]] = {
    # Electric Blanket
    # https://developer.tuya.com/en/docs/iot/categorydr?id=Kaiuz22dyc66p
    "dr": (
        SwitchEntityDescription(
            key=DPCode.SWITCH,
            translation_key="Power (default)",
            icon="mdi:power",
        ),
        SwitchEntityDescription(
            key=DPCode.SWITCH_1,
            icon="mdi:power",
        ),
        SwitchEntityDescription(
            key=DPCode.SWITCH_2,
            translation_key="Power (side)",
            icon="mdi:power",
        ),
        SwitchEntityDescription(
            key=DPCode.PREHEAT,
            translation_key="Preheat (default)",
            icon="mdi:heating-coil",
        ),
        SwitchEntityDescription(
            key=DPCode.PREHEAT_1,
            name="Preheat",
            icon="mdi:heating-coil",
        ),
        SwitchEntityDescription(
            key=DPCode.PREHEAT_2,
            translation_key="Preheat (side)",
            icon="mdi:heating-coil",
        ),
    ),
    # Smart Kettle
    # https://developer.tuya.com/en/docs/iot/fbh?id=K9gf484m21yq7
    "bh": (
        SwitchEntityDescription(
            key=DPCode.START,
            translation_key="start",
            icon="mdi:kettle-steam",
        ),
        SwitchEntityDescription(
            key=DPCode.WARM,
            translation_key="heat_preservation",
            entity_category=EntityCategory.CONFIG,
        ),
    ),
    # EasyBaby
    # Undocumented, might have a wider use
    "cn": (
        SwitchEntityDescription(
            key=DPCode.DISINFECTION,
            translation_key="disinfection",
            icon="mdi:bacteria",
        ),
        SwitchEntityDescription(
            key=DPCode.WATER,
            translation_key="water",
            icon="mdi:water",
        ),
            icon="mdi:power",
        ),
        SwitchEntityDescription(
            key=DPCode.SWITCH_2,
            translation_key="Power (side)",
            icon="mdi:power",
        ),
        SwitchEntityDescription(
            key=DPCode.PREHEAT,
            translation_key="Preheat (default)",
            icon="mdi:heating-coil",
        ),
        SwitchEntityDescription(
            key=DPCode.PREHEAT_1,
            translation_key="Preheat",
            icon="mdi:heating-coil",
        ),
        SwitchEntityDescription(
            key=DPCode.PREHEAT_2,
            translation_key="Preheat (side)",
            icon="mdi:heating-coil",
        ),
    ),
    # Smart Kettle
    # https://developer.tuya.com/en/docs/iot/fbh?id=K9gf484m21yq7
    "bh": (
        SwitchEntityDescription(
            key=DPCode.START,
            translation_key="start",
            icon="mdi:kettle-steam",
        ),
        SwitchEntityDescription(
            key=DPCode.WARM,
            translation_key="heat_preservation",
            entity_category=EntityCategory.CONFIG,
        ),
    ),
    # EasyBaby
    # Undocumented, might have a wider use
    "cn": (
        SwitchEntityDescription(
            key=DPCode.DISINFECTION,
            translation_key="disinfection",
            icon="mdi:bacteria",
        ),
        SwitchEntityDescription(
            key=DPCode.WATER,
            translation_key="water",
            icon="mdi:water",
        ),
