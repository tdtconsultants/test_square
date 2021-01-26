
# V1 List Fees Response

## Structure

`V1 List Fees Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List of V1 Fee`](/doc/models/v1-fee.md) | Optional | - |

## Example (as JSON)

```json
{
  "items": [
    {
      "id": "id7",
      "name": "name7",
      "rate": "rate3",
      "calculation_phase": "FEE_TOTAL_PHASE",
      "adjustment_type": "TAX"
    },
    {
      "id": "id8",
      "name": "name8",
      "rate": "rate2",
      "calculation_phase": "FEE_SUBTOTAL_PHASE",
      "adjustment_type": "TAX"
    }
  ]
}
```

