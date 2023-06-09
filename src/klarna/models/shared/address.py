"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from klarna import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Address:
    
    attention: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attention'), 'exclude': lambda f: f is None }})
    r"""‘Attn.’ (if applicable). Only applicable for B2B customers."""
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city'), 'exclude': lambda f: f is None }})
    r"""Customer’s city."""
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""Customer’s country. This value overrides the purchase country if they are different. Should follow the standard of ISO 3166 alpha-2. E.g. GB, US, DE, SE."""
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""Customer’s email address."""
    family_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('family_name'), 'exclude': lambda f: f is None }})
    r"""Customers family name in UTF-8 encoding.
    Cannot be only numbers, must be more than 1 character.
    Allowed special characters: -'’.
    More information can be found [in this link](https://docs.klarna.com/klarna-payments/in-depth-knowledge/customer-data-requirements/#details-needed-per-market)
    """
    given_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('given_name'), 'exclude': lambda f: f is None }})
    r"""Customers given name in UTF-8 encoding.
    Cannot be only numbers, must be more than 1 character.
    Allowed special characters: -'’.
    More information can be found [in this link](https://docs.klarna.com/klarna-payments/in-depth-knowledge/customer-data-requirements/#details-needed-per-market)
    """
    organization_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_name'), 'exclude': lambda f: f is None }})
    r"""Organization name (if applicable). Only applicable for B2B customers."""
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""Phone number. Preferably a mobile phone number."""
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postal_code'), 'exclude': lambda f: f is None }})
    r"""Customer’s postal code. Validation according to Universal Postal Union addressing systems.
    E.g. 12345, W1G OPW.
    """
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""Customer’s region or state - Mandatory for US and AU market. Validations according to ISO 3166-2 format, e.g. OH, NJ, etc."""
    street_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address'), 'exclude': lambda f: f is None }})
    r"""Customer’s street address. Regional formatting is required, as follows:
    UK/US/FR: 33 Cavendish Square
    Rest of EU: De Ruijterkade 7
    """
    street_address2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_address2'), 'exclude': lambda f: f is None }})
    r"""Customer’s street address. Second Line."""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""Customer’s Title. Allowed values per country:
    UK - \"Mr\", \"Ms\"
    DE - \"Herr\", \"Frau\"
    AT: \"Herr, \"Frau\"
    CH: de-CH: \"Herr, \"Frau\" it-CH: \"Sig.\", \"Sig.ra\" fr-CH: \"M\", \"Mme\" 
    BE: \"Dhr.\", \"Mevr.\"
    NL: \"Dhr.\", \"Mevr.\" 
    """
    