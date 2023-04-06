<div align="center">
    <img src="https://user-images.githubusercontent.com/6267663/230347878-f2873a58-f578-4e95-86e0-7bebfd78f4f1.svg">
    <h1>Python SDK</h1>
   <p>An effortless integration. Designed for growth.</p>
   <a href="https://docs.klarna.com/"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000&style=for-the-badge" /></a>
   <a href="https://github.com/speakeasy-sdks/klarna-python/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/klarna-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/speakeasy-sdks/klarna-python/releases"><img src="https://img.shields.io/github/v/release/speakeasy-sdks/klarna-python?sort=semver&style=for-the-badge" /></a>
</div>


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
