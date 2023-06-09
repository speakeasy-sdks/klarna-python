"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address as shared_address
from ..shared import customer as shared_customer
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from klarna import utils
from typing import Optional

class CustomerTokenCreationRequestIntendedUseEnum(str, Enum):
    r"""Intended use for the token."""
    SUBSCRIPTION = 'SUBSCRIPTION'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomerTokenCreationRequest:
    
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""Description of the purpose of the token."""
    intended_use: CustomerTokenCreationRequestIntendedUseEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('intended_use') }})
    r"""Intended use for the token."""
    locale: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('locale') }})
    r"""RFC 1766 customer's locale."""
    purchase_country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purchase_country') }})
    r"""ISO 3166 alpha-2 purchase country."""
    purchase_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purchase_currency') }})
    r"""ISO 4217 purchase currency."""
    billing_address: Optional[shared_address.Address] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address'), 'exclude': lambda f: f is None }})
    customer: Optional[shared_customer.Customer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer'), 'exclude': lambda f: f is None }})
    