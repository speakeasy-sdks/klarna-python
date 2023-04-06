"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class SubscriptionIntervalEnum(str, Enum):
    r"""The cadence unit for this."""
    DAY = 'DAY'
    WEEK = 'WEEK'
    MONTH = 'MONTH'
    YEAR = 'YEAR'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Subscription:
    
    interval: SubscriptionIntervalEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval') }})
    r"""The cadence unit for this."""  
    interval_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval_count') }})
    r"""The number of intervals"""  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the subscription product"""  
    