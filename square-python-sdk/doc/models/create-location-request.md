
# Create Location Request

Request object for the [CreateLocation](#endpoint-createlocation) endpoint.

## Structure

`Create Location Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location` | [`Location`](/doc/models/location.md) | Optional | - |

## Example (as JSON)

```json
{
  "location": {
    "address": {
      "address_line_1": "1234 Peachtree St. NE",
      "administrative_district_level_1": "GA",
      "locality": "Atlanta",
      "postal_code": "30309"
    },
    "description": "My new location.",
    "facebook_url": "null",
    "name": "New location name"
  }
}
```

