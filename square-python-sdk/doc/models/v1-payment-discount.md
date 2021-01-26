
# V1 Payment Discount

V1PaymentDiscount

## Structure

`V1 Payment Discount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The discount's name. |
| `applied_money` | [`V1 Money`](/doc/models/v1-money.md) | Optional | - |
| `discount_id` | `string` | Optional | The ID of the applied discount, if available. Discounts applied in older versions of Square Register might not have an ID. |

## Example (as JSON)

```json
{
  "name": "name0",
  "applied_money": {
    "amount": 196,
    "currency_code": "LYD"
  },
  "discount_id": "discount_id8"
}
```

