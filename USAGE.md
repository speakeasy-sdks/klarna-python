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