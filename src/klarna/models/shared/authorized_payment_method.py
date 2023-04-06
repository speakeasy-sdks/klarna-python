"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from klarna import utils
from typing import Optional

class AuthorizedPaymentMethodTypeEnum(str, Enum):
    INVOICE = 'invoice'
    FIXED_AMOUNT = 'fixed_amount'
    BASE_ACCOUNT = 'base_account'
    DIRECT_DEBIT = 'direct_debit'
    DIRECT_BANK_TRANSFER = 'direct_bank_transfer'
    B2B_INVOICE = 'b2b_invoice'
    CARD = 'card'
    SLICE_IT_BY_CARD = 'slice_it_by_card'
    PAY_LATER_BY_CARD = 'pay_later_by_card'
    PAY_BY_CARD = 'pay_by_card'
    FIXED_SUM_CREDIT = 'fixed_sum_credit'
    ALTERNATIVE_PAYMENT_METHOD = 'alternative_payment_method'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthorizedPaymentMethod:
    
    type: AuthorizedPaymentMethodTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})  
    number_of_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number_of_days'), 'exclude': lambda f: f is None }})  
    number_of_installments: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number_of_installments'), 'exclude': lambda f: f is None }})  
    