"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from klarna import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssetUrls:
    
    descriptive: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('descriptive'), 'exclude': lambda f: f is None }})
    r"""URL of the descriptive asset. Using this dynamic asset will make sure that any copy update of Klarna will automatically be propagated."""
    standard: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('standard'), 'exclude': lambda f: f is None }})
    r"""URL of the standard asset. Using this dynamic asset will make sure that any copy update of Klarna will automatically be propagated."""
    