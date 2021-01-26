
# Search Availability Request

## Structure

`Search Availability Request`

## Fields

| Name | Type | Description |
|  --- | --- | --- |
| `query` | [`Search Availability Query`](/doc/models/search-availability-query.md) | Query conditions to search for availabilities of bookings. |

## Example (as JSON)

```json
{
  "query": {
    "filter": {
      "start_at_range": {
        "start_at": "start_at0",
        "end_at": "end_at2"
      },
      "location_id": "location_id8",
      "segment_filters": [
        {
          "service_variation_id": "service_variation_id0",
          "team_member_id_filter": {
            "all": [
              "all9"
            ],
            "any": [
              "any8",
              "any9"
            ],
            "none": [
              "none3"
            ]
          }
        }
      ],
      "booking_id": "booking_id8"
    }
  }
}
```

