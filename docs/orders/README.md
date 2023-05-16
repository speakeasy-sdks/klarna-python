# orders

## Overview

Operations related to orders

### Available Operations

* [read](#read) - Create a new order

## read

Use this API call to create a new order. Placing an order towards Klarna means that the Klarna Payments session will be closed and that an order will be created in Klarna's system.<br/>When you have received the `authorization_token` for a successful authorization you can place the order. Among the other order details in this request, you include a URL to the confirmation page for the customer.<br/>When the Order has been successfully placed at Klarna, you need to handle it either through the Merchant Portal or using [Klarna’s Order Management API](#order-management-api).
Read more on **[Create a new order](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-3-create-an-order/)**.

### Example Usage

```python
import klarna
from klarna.models import operations, shared

s = klarna.Klarna(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.CreateOrderRequest(
    authorization_token='distinctio',
    create_order_request_input=shared.CreateOrderRequestInput(
        auto_capture=False,
        billing_address=shared.Address(
            attention='Attn',
            city='London',
            country='GB',
            email='test.sam@test.com',
            family_name='Andersson',
            given_name='Adam',
            organization_name='quibusdam',
            phone='+44795465131',
            postal_code='W1G 0PW',
            region='OH',
            street_address='33 Cavendish Square',
            street_address2='Floor 22 / Flat 2',
            title='Mr.',
        ),
        custom_payment_method_ids=[
            'nulla',
            'corrupti',
            'illum',
        ],
        customer=shared.Customer(
            date_of_birth='1978-12-31',
            gender='male',
            last_four_ssn='vel',
            national_identification_number='error',
            organization_entity_type=shared.CustomerOrganizationEntityTypeEnum.SOLE_TRADER,
            organization_registration_id='suscipit',
            title='Mr.',
            type='organization',
            vat_id='iure',
        ),
        locale='en-GB',
        merchant_data='{"order_specific":[{"substore":"Women's Fashion","product_name":"Women Sweatshirt"}]}',
        merchant_reference1='ON4711',
        merchant_reference2='hdt53h-zdgg6-hdaff2',
        merchant_urls=shared.MerchantUrls(
            authorization='https://www.example-url.com/authorization',
            confirmation='https://www.example-url.com/confirmation',
            notification='https://www.example-url.com/notification',
            push='https://www.example-url.com/push',
        ),
        order_amount=2500,
        order_lines=[
            shared.OrderLine(
                image_url='https://www.exampleobjects.com/logo.png',
                merchant_data='{"customer_account_info":[{"unique_account_identifier":"test@gmail.com","account_registration_date":"2017-02-13T10:49:20Z","account_last_modified":"2019-03-13T11:45:27Z"}]}',
                name='Running shoe',
                product_identifiers=shared.ProductIdentifiers(
                    brand='shoe-brand',
                    category_path='Shoes > Running',
                    color='white',
                    global_trade_item_number='4912345678904',
                    manufacturer_part_number='AD6654412-334.22',
                    size='small',
                ),
                product_url='https://.../AD6654412.html',
                quantity=1,
                quantity_unit='pcs',
                reference='AD6654412',
                subscription=shared.Subscription(
                    interval=shared.SubscriptionIntervalEnum.YEAR,
                    interval_count=56713,
                    name='Ricky Hoppe',
                ),
                tax_rate=1900,
                total_amount=2500,
                total_discount_amount=500,
                total_tax_amount=475,
                type='physical',
                unit_price=2500,
            ),
            shared.OrderLine(
                image_url='https://www.exampleobjects.com/logo.png',
                merchant_data='{"customer_account_info":[{"unique_account_identifier":"test@gmail.com","account_registration_date":"2017-02-13T10:49:20Z","account_last_modified":"2019-03-13T11:45:27Z"}]}',
                name='Running shoe',
                product_identifiers=shared.ProductIdentifiers(
                    brand='shoe-brand',
                    category_path='Shoes > Running',
                    color='white',
                    global_trade_item_number='4912345678904',
                    manufacturer_part_number='AD6654412-334.22',
                    size='small',
                ),
                product_url='https://.../AD6654412.html',
                quantity=1,
                quantity_unit='pcs',
                reference='AD6654412',
                subscription=shared.Subscription(
                    interval=shared.SubscriptionIntervalEnum.YEAR,
                    interval_count=528895,
                    name='Miriam Huel',
                ),
                tax_rate=1900,
                total_amount=2500,
                total_discount_amount=500,
                total_tax_amount=475,
                type='physical',
                unit_price=2500,
            ),
        ],
        order_tax_amount=475,
        purchase_country='GB',
        purchase_currency='GBP',
        shipping_address=shared.Address(
            attention='Attn',
            city='London',
            country='GB',
            email='test.sam@test.com',
            family_name='Andersson',
            given_name='Adam',
            organization_name='ab',
            phone='+44795465131',
            postal_code='W1G 0PW',
            region='OH',
            street_address='33 Cavendish Square',
            street_address2='Floor 22 / Flat 2',
            title='Mr.',
        ),
    ),
)

res = s.orders.read(req)

if res.order is not None:
    # handle response
```
