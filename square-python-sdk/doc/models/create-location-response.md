
# Create Location Response

Response object returned by the [CreateLocation](#endpoint-createlocation) endpoint.

## Structure

`Create Location Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Information on errors encountered during the request. |
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
    "capabilities": [
      "CREDIT_CARD_PROCESSING"
    ],
    "coordinates": {
      "latitude": 33.788567,
      "longitude": -84.466947
    },
    "country": "US",
    "created_at": "2019-07-19T17:58:25Z",
    "currency": "USD",
    "description": "My new location.",
    "id": "LOCATION_ID",
    "instagram_username": "instagram",
    "language_code": "en-US",
    "mcc": "1234",
    "merchant_id": "MERCHANT_ID",
    "name": "New location name",
    "status": "ACTIVE",
    "twitter_username": "twitter",
    "type": "PHYSICAL",
    "website_url": "examplewebsite.com"
  }
}
```

