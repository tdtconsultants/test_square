
# Create Loyalty Account Request

A request to create a new loyalty account.

## Structure

`Create Loyalty Account Request`

## Fields

| Name | Type | Description |
|  --- | --- | --- |
| `loyalty_account` | [`Loyalty Account`](/doc/models/loyalty-account.md) | Describes a loyalty account. For more information, see<br>[Loyalty Overview](https://developer.squareup.com/docs/loyalty/overview). |
| `idempotency_key` | `string` | A unique string that identifies this `CreateLoyaltyAccount` request.<br>Keys can be any valid string, but must be unique for every request. |

## Example (as JSON)

```json
{
  "idempotency_key": "ec78c477-b1c3-4899-a209-a4e71337c996",
  "loyalty_account": {
    "mappings": [
      {
        "type": "PHONE",
        "value": "+14155551234"
      }
    ],
    "program_id": "d619f755-2d17-41f3-990d-c04ecedd64dd"
  }
}
```

