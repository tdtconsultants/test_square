
# V1 Create Discount Request

## Structure

`V1 Create Discount Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`V1 Discount`](/doc/models/v1-discount.md) | Optional | V1Discount |

## Example (as JSON)

```json
{
  "body": {
    "id": "id6",
    "name": "name6",
    "rate": "rate4",
    "amount_money": {
      "amount": 194,
      "currency_code": "KWD"
    },
    "discount_type": "VARIABLE_AMOUNT"
  }
}
```

