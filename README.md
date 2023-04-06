<div align="center">
    <img src="https://user-images.githubusercontent.com/6267663/230347878-f2873a58-f578-4e95-86e0-7bebfd78f4f1.svg" width="300">
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
import klarna
from klarna.models import operations, shared

s = klarna.Klarna(
    security=shared.Security(
        api_key_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.CreateOrderRequest(
    authorization_token="corrupti",
    create_order_request_input=shared.CreateOrderRequestInput(
        auto_capture=False,
        billing_address=shared.Address(
            attention="Attn",
            city="London",
            country="GB",
            email="test.sam@test.com",
            family_name="Andersson",
            given_name="Adam",
            organization_name="provident",
            phone="+44795465131",
            postal_code="W1G 0PW",
            region="OH",
            street_address="33 Cavendish Square",
            street_address2="Floor 22 / Flat 2",
            title="Mr.",
        ),
        custom_payment_method_ids=[
            "quibusdam",
            "unde",
            "nulla",
        ],
        customer=shared.Customer(
            date_of_birth="1978-12-31",
            gender="male",
            last_four_ssn="corrupti",
            national_identification_number="illum",
            organization_entity_type="LIMITED_PARTNERSHIP",
            organization_registration_id="error",
            title="Mr.",
            type="organization",
            vat_id="deserunt",
        ),
        locale="en-GB",
        merchant_data="{"order_specific":[{"substore":"Women's Fashion","product_name":"Women Sweatshirt"}]}",
        merchant_reference1="ON4711",
        merchant_reference2="hdt53h-zdgg6-hdaff2",
        merchant_urls=shared.MerchantUrls(
            authorization="https://www.example-url.com/authorization",
            confirmation="https://www.example-url.com/confirmation",
            notification="https://www.example-url.com/notification",
            push="https://www.example-url.com/push",
        ),
        order_amount=2500,
        order_lines=[
            shared.OrderLine(
                image_url="https://www.exampleobjects.com/logo.png",
                merchant_data="{"customer_account_info":[{"unique_account_identifier":"test@gmail.com","account_registration_date":"2017-02-13T10:49:20Z","account_last_modified":"2019-03-13T11:45:27Z"}]}",
                name="Running shoe",
                product_identifiers=shared.ProductIdentifiers(
                    brand="shoe-brand",
                    category_path="Shoes > Running",
                    color="white",
                    global_trade_item_number="4912345678904",
                    manufacturer_part_number="AD6654412-334.22",
                    size="small",
                ),
                product_url="https://.../AD6654412.html",
                quantity=1,
                quantity_unit="pcs",
                reference="AD6654412",
                subscription=shared.Subscription(
                    interval="WEEK",
                    interval_count=297534,
                    name="debitis",
                ),
                tax_rate=1900,
                total_amount=2500,
                total_discount_amount=500,
                total_tax_amount=475,
                type="physical",
                unit_price=2500,
            ),
            shared.OrderLine(
                image_url="https://www.exampleobjects.com/logo.png",
                merchant_data="{"customer_account_info":[{"unique_account_identifier":"test@gmail.com","account_registration_date":"2017-02-13T10:49:20Z","account_last_modified":"2019-03-13T11:45:27Z"}]}",
                name="Running shoe",
                product_identifiers=shared.ProductIdentifiers(
                    brand="shoe-brand",
                    category_path="Shoes > Running",
                    color="white",
                    global_trade_item_number="4912345678904",
                    manufacturer_part_number="AD6654412-334.22",
                    size="small",
                ),
                product_url="https://.../AD6654412.html",
                quantity=1,
                quantity_unit="pcs",
                reference="AD6654412",
                subscription=shared.Subscription(
                    interval="DAY",
                    interval_count=963663,
                    name="tempora",
                ),
                tax_rate=1900,
                total_amount=2500,
                total_discount_amount=500,
                total_tax_amount=475,
                type="physical",
                unit_price=2500,
            ),
        ],
        order_tax_amount=475,
        purchase_country="GB",
        purchase_currency="GBP",
        shipping_address=shared.Address(
            attention="Attn",
            city="London",
            country="GB",
            email="test.sam@test.com",
            family_name="Andersson",
            given_name="Adam",
            organization_name="suscipit",
            phone="+44795465131",
            postal_code="W1G 0PW",
            region="OH",
            street_address="33 Cavendish Square",
            street_address2="Floor 22 / Flat 2",
            title="Mr.",
        ),
    ),
)
    
res = s.orders.create(req)

if res.order is not None:
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
