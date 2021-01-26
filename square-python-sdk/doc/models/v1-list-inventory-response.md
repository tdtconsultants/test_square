
# V1 List Inventory Response

## Structure

`V1 List Inventory Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List of V1 Inventory Entry`](/doc/models/v1-inventory-entry.md) | Optional | - |

## Example (as JSON)

```json
{
  "items": [
    {
      "variation_id": "variation_id5",
      "quantity_on_hand": 93.37
    },
    {
      "variation_id": "variation_id4",
      "quantity_on_hand": 93.38
    }
  ]
}
```

