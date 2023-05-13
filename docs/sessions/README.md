# sessions

## Overview

Operations related to sessions

### Available Operations

* [read](#read) - Read an existing payment session
* [read](#read) - Create a new payment session
* [update](#update) - Update an existing payment session

## read

Use this API call to read a Klarna Payments session. You can read the Klarna Payments session at any time after it has been created, to get information about it. This will return all data that has been collected during the session.
Read more on **[Read an existing payment session](https://docs.klarna.com/klarna-payments/other-actions/check-the-details-of-a-payment-session/)**.

### Example Usage

```python
import klarna
from klarna.models import operations

s = klarna.Klarna(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ReadCreditSessionRequest(
    session_id='quis',
)

res = s.sessions.read(req)

if res.session_read is not None:
    # handle response
```

## read

Use this API call to create a Klarna Payments session.<br/>When a session is created you will receive the available `payment_method_categories` for the session, a `session_id` and a `client_token`. The `session_id` can be used to read or update the session using the REST API. The `client_token` should be passed to the browser.
Read more on **[Create a new payment session](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-1-initiate-a-payment/)**.

### Example Usage

```python
import klarna
from klarna.models import shared

s = klarna.Klarna(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.SessionCreateInput(
    acquiring_channel=shared.SessionCreateAcquiringChannelEnum.ECOMMERCE,
    attachment=shared.Attachment(
        body='{"customer_account_info":[{"unique_account_identifier":"test@gmail.com","account_registration_date":"2017-02-13T10:49:20Z","account_last_modified":"2019-03-13T11:45:27Z"}]}',
        content_type='application/vnd.klarna.internal.emd-v2+json',
    ),
    billing_address=shared.Address(
        attention='Attn',
        city='London',
        country='GB',
        email='test.sam@test.com',
        family_name='Andersson',
        given_name='Adam',
        organization_name='veritatis',
        phone='+44795465131',
        postal_code='W1G 0PW',
        region='OH',
        street_address='33 Cavendish Square',
        street_address2='Floor 22 / Flat 2',
        title='Mr.',
    ),
    custom_payment_method_ids=[
        'perferendis',
        'ipsam',
        'repellendus',
    ],
    customer=shared.Customer(
        date_of_birth='1978-12-31',
        gender='male',
        last_four_ssn='sapiente',
        national_identification_number='quo',
        organization_entity_type=shared.CustomerOrganizationEntityTypeEnum.PUBLIC_LIMITED_COMPANY,
        organization_registration_id='at',
        title='Mr.',
        type='organization',
        vat_id='at',
    ),
    design='maiores',
    intent=shared.SessionCreateIntentEnum.BUY,
    locale='en-US',
    merchant_data='{"order_specific":[{"substore":"Women's Fashion","product_name":"Women Sweatshirt"}]}',
    merchant_reference1='ON4711',
    merchant_reference2='hdt53h-zdgg6-hdaff2',
    merchant_urls=shared.MerchantUrls(
        authorization='https://www.example-url.com/authorization',
        confirmation='https://www.example-url.com/confirmation',
        notification='https://www.example-url.com/notification',
        push='https://www.example-url.com/push',
    ),
    options=shared.Options(
        color_border='#FF9900',
        color_border_selected='#FF9900',
        color_details='#FF9900',
        color_text='#FF9900',
        radius_border='5px',
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
                interval_count=800911,
                name='Deanna Sauer MD',
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
                interval=shared.SubscriptionIntervalEnum.MONTH,
                interval_count=582020,
                name='Cassandra Welch',
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
        organization_name='beatae',
        phone='+44795465131',
        postal_code='W1G 0PW',
        region='OH',
        street_address='33 Cavendish Square',
        street_address2='Floor 22 / Flat 2',
        title='Mr.',
    ),
)

res = s.sessions.read(req)

if res.merchant_session is not None:
    # handle response
```

## update

Use this API call to update a Klarna Payments session with new details, in case something in the order has changed and the checkout has been reloaded. Including if the consumer adds a new item to the cart or if consumer details are updated.
Read more on **[Update an existing payment session](https://docs.klarna.com/klarna-payments/other-actions/update-the-cart/)**.

### Example Usage

```python
import klarna
from klarna.models import operations, shared

s = klarna.Klarna(
    security=shared.Security(
        api_key_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateCreditSessionRequest(
    session_input=shared.SessionInput(
        acquiring_channel=shared.SessionAcquiringChannelEnum.ECOMMERCE,
        attachment=shared.Attachment(
            body='{"customer_account_info":[{"unique_account_identifier":"test@gmail.com","account_registration_date":"2017-02-13T10:49:20Z","account_last_modified":"2019-03-13T11:45:27Z"}]}',
            content_type='application/vnd.klarna.internal.emd-v2+json',
        ),
        billing_address=shared.Address(
            attention='Attn',
            city='London',
            country='GB',
            email='test.sam@test.com',
            family_name='Andersson',
            given_name='Adam',
            organization_name='commodi',
            phone='+44795465131',
            postal_code='W1G 0PW',
            region='OH',
            street_address='33 Cavendish Square',
            street_address2='Floor 22 / Flat 2',
            title='Mr.',
        ),
        custom_payment_method_ids=[
            'modi',
            'qui',
        ],
        customer=shared.Customer(
            date_of_birth='1978-12-31',
            gender='male',
            last_four_ssn='impedit',
            national_identification_number='cum',
            organization_entity_type=shared.CustomerOrganizationEntityTypeEnum.GENERAL_PARTNERSHIP,
            organization_registration_id='ipsum',
            title='Mr.',
            type='organization',
            vat_id='excepturi',
        ),
        design='aspernatur',
        intent=shared.SessionIntentEnum.BUY,
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
        options=shared.Options(
            color_border='#FF9900',
            color_border_selected='#FF9900',
            color_details='#FF9900',
            color_text='#FF9900',
            radius_border='5px',
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
                    interval=shared.SubscriptionIntervalEnum.WEEK,
                    interval_count=617636,
                    name='Sheryl Fadel',
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
            organization_name='hic',
            phone='+44795465131',
            postal_code='W1G 0PW',
            region='OH',
            street_address='33 Cavendish Square',
            street_address2='Floor 22 / Flat 2',
            title='Mr.',
        ),
    ),
    session_id='saepe',
)

res = s.sessions.update(req)

if res.status_code == 200:
    # handle response
```
