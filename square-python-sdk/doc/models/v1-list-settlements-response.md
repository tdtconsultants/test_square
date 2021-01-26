
# V1 List Settlements Response

## Structure

`V1 List Settlements Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List of V1 Settlement`](/doc/models/v1-settlement.md) | Optional | - |

## Example (as JSON)

```json
{
  "items": [
    {
      "id": "id7",
      "status": "SENT",
      "total_money": {
        "amount": 53,
        "currency_code": "PGK"
      },
      "initiated_at": "initiated_at9",
      "bank_account_id": "bank_account_id7"
    },
    {
      "id": "id8",
      "status": "FAILED",
      "total_money": {
        "amount": 54,
        "currency_code": "PHP"
      },
      "initiated_at": "initiated_at0",
      "bank_account_id": "bank_account_id8"
    }
  ]
}
```

