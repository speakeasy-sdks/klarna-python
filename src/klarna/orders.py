"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from klarna.models import operations, shared
from typing import Optional

class Orders:
    r"""Operations related to orders"""
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
        
    def create(self, request: operations.CreateOrderRequest) -> operations.CreateOrderResponse:
        r"""Create a new order
        Use this API call to create a new order. Placing an order towards Klarna means that the Klarna Payments session will be closed and that an order will be created in Klarna's system.<br/>When you have received the `authorization_token` for a successful authorization you can place the order. Among the other order details in this request, you include a URL to the confirmation page for the customer.<br/>When the Order has been successfully placed at Klarna, you need to handle it either through the Merchant Portal or using [Klarna’s Order Management API](#order-management-api).
        Read more on **[Create a new order](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-3-create-an-order/)**.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateOrderRequest, base_url, '/payments/v1/authorizations/{authorizationToken}/order', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "create_order_request_input", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateOrderResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Order])
                res.order = out
        elif http_res.status_code in [400, 403, 404, 409]:
            pass

        return res

    