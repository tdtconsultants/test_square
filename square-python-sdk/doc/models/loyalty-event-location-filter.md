
# Loyalty Event Location Filter

Filter events by location.

## Structure

`Loyalty Event Location Filter`

## Fields

| Name | Type | Description |
|  --- | --- | --- |
| `location_ids` | `List of string` | The [location](#type-Location) IDs for loyalty events to query.<br>If multiple values are specified, the endpoint uses<br>a logical OR to combine them. |

## Example (as JSON)

```json
{
  "location_ids": [
    "location_ids0"
  ]
}
```

