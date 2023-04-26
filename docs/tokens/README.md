# tokens

## Overview

Operations related to token

### Available Operations

* [purchase](#purchase) - Generate a consumer token

## purchase

Use this API call to create a Klarna Customer Token.<br/>After having obtained an `authorization_token` for a successful authorization, this can be used to create a purchase token instead of placing the order. Creating a Klarna Customer Token results in Klarna storing customer and payment method details.
Read more on **[Generate a consumer token](https://docs.klarna.com/klarna-payments/in-depth-knowledge/customer-token/)**.

### Example Usage

```python
import klarna
from klarna.models import operations, shared

s = klarna.Klarna(
    security=shared.Security(
        api_key_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.PurchaseTokenRequest(
    authorization_token="nemo",
    customer_token_creation_request=shared.CustomerTokenCreationRequest(
        billing_address=shared.Address(
            attention="Attn",
            city="London",
            country="GB",
            email="test.sam@test.com",
            family_name="Andersson",
            given_name="Adam",
            organization_name="minima",
            phone="+44795465131",
            postal_code="W1G 0PW",
            region="OH",
            street_address="33 Cavendish Square",
            street_address2="Floor 22 / Flat 2",
            title="Mr.",
        ),
        customer=shared.Customer(
            date_of_birth="1978-12-31",
            gender="male",
            last_four_ssn="excepturi",
            national_identification_number="accusantium",
            organization_entity_type="LIMITED_PARTNERSHIP",
            organization_registration_id="culpa",
            title="Mr.",
            type="organization",
            vat_id="doloribus",
        ),
        description="sapiente",
        intended_use="SUBSCRIPTION",
        locale="en-GB",
        purchase_country="GB",
        purchase_currency="GBP",
    ),
)

res = s.tokens.purchase(req)

if res.customer_token_creation_response is not None:
    # handle response
```
