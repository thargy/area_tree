"""Custom types for area_tree."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import AreaTreeApiClient
    from .coordinator import BlueprintDataUpdateCoordinator


type AreaTreeConfigEntry = ConfigEntry[AreaTreeData]


@dataclass
class AreaTreeData:
    """Data for the Blueprint integration."""

    client: AreaTreeApiClient
    coordinator: BlueprintDataUpdateCoordinator
    integration: Integration
