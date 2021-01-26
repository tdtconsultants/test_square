
# Search Subscriptions Query

Represents a query (including filtering criteria) used to search for subscriptions.

## Structure

`Search Subscriptions Query`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter` | [`Search Subscriptions Filter`](/doc/models/search-subscriptions-filter.md) | Optional | Represents a set of SearchSubscriptionsQuery filters used to limit the set of Subscriptions returned by SearchSubscriptions. |

## Example (as JSON)

```json
{
  "filter": {
    "customer_ids": [
      "customer_ids3",
      "customer_ids2"
    ],
    "location_ids": [
      "location_ids4"
    ]
  }
}
```

