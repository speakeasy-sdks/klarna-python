# klarna-orders

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install klarna-orders
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        api_key_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.CancelAuthorizationRequest(
    authorization_token="corrupti",
)
    
res = s.authorizations.cancel(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### authorizations

* `cancel` - Cancel an existing authorization

### orders

* `create` - Create a new order

### sessions

* `create` - Create a new payment session
* `read` - Read an existing payment session
* `update` - Update an existing payment session

### tokens

* `purchase` - Generate a consumer token
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
