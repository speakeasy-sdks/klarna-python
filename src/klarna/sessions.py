"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from klarna.models import operations, shared
from typing import Optional

class Sessions:
    r"""Operations related to sessions"""
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def create(self, request: shared.SessionCreateInput) -> operations.CreateCreditSessionResponse:
        r"""Create a new payment session
        Use this API call to create a Klarna Payments session.<br/>When a session is created you will receive the available `payment_method_categories` for the session, a `session_id` and a `client_token`. The `session_id` can be used to read or update the session using the REST API. The `client_token` should be passed to the browser.
        Read more on **[Create a new payment session](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-1-initiate-a-payment/)**.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/payments/v1/sessions'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateCreditSessionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.MerchantSession])
                res.merchant_session = out
        elif http_res.status_code in [400, 403]:
            pass

        return res

    def read(self, request: operations.ReadCreditSessionRequest) -> operations.ReadCreditSessionResponse:
        r"""Read an existing payment session
        Use this API call to read a Klarna Payments session. You can read the Klarna Payments session at any time after it has been created, to get information about it. This will return all data that has been collected during the session.
        Read more on **[Read an existing payment session](https://docs.klarna.com/klarna-payments/other-actions/check-the-details-of-a-payment-session/)**.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ReadCreditSessionRequest, base_url, '/payments/v1/sessions/{session_id}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ReadCreditSessionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SessionRead])
                res.session_read = out
        elif http_res.status_code in [403, 404]:
            pass

        return res

    def update(self, request: operations.UpdateCreditSessionRequest) -> operations.UpdateCreditSessionResponse:
        r"""Update an existing payment session
        Use this API call to update a Klarna Payments session with new details, in case something in the order has changed and the checkout has been reloaded. Including if the consumer adds a new item to the cart or if consumer details are updated.
        Read more on **[Update an existing payment session](https://docs.klarna.com/klarna-payments/other-actions/update-the-cart/)**.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateCreditSessionRequest, base_url, '/payments/v1/sessions/{session_id}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "session_input", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateCreditSessionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    