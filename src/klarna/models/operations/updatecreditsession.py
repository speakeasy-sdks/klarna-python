"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import session as shared_session
from typing import Optional


@dataclasses.dataclass
class UpdateCreditSessionRequest:
    
    session_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'session_id', 'style': 'simple', 'explode': False }})
    r"""session_id"""  
    session_input: shared_session.SessionInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""session_request"""  
    

@dataclasses.dataclass
class UpdateCreditSessionResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    