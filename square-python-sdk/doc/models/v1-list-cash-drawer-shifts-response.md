
# V1 List Cash Drawer Shifts Response

## Structure

`V1 List Cash Drawer Shifts Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List of V1 Cash Drawer Shift`](/doc/models/v1-cash-drawer-shift.md) | Optional | - |

## Example (as JSON)

```json
{
  "items": [
    {
      "id": "id7",
      "event_type": "ENDED",
      "opened_at": "opened_at5",
      "ended_at": "ended_at9",
      "closed_at": "closed_at9"
    },
    {
      "id": "id8",
      "event_type": "OPEN",
      "opened_at": "opened_at6",
      "ended_at": "ended_at0",
      "closed_at": "closed_at0"
    }
  ]
}
```

