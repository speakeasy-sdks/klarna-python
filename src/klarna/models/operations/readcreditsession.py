"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import session_read as shared_session_read
from typing import Optional


@dataclasses.dataclass
class ReadCreditSessionRequest:
    
    session_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'session_id', 'style': 'simple', 'explode': False }})
    r"""session_id"""
    

@dataclasses.dataclass
class ReadCreditSessionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    session_read: Optional[shared_session_read.SessionRead] = dataclasses.field(default=None)
    r"""successful operation"""
    