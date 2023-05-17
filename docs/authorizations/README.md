# authorizations

## Overview

Operations related to authorizations

### Available Operations

* [cancel](#cancel) - Cancel an existing authorization

## cancel

Use this API call to cancel/release an authorization. If the `authorization_token` received during a Klarna Payments won’t be used to place an order immediately you could release the authorization.
Read more on **[Cancel an existing authorization](https://docs.klarna.com/klarna-payments/other-actions/cancel-an-authorization/)**.

### Example Usage

```python
import klarna
from klarna.models import operations

s = klarna.Klarna(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.CancelAuthorizationRequest(
    authorization_token='provident',
)

res = s.authorizations.cancel(req)

if res.status_code == 200:
    # handle response
```
