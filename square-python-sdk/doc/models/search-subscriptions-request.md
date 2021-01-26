
# Search Subscriptions Request

Defines parameters in a
[SearchSubscriptions](#endpoint-subscriptions-searchsubscriptions) endpoint
request.

## Structure

`Search Subscriptions Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `string` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |
| `limit` | `int` | Optional | The upper limit on the number of subscriptions to return<br>in the response.<br><br>Default: `200` |
| `query` | [`Search Subscriptions Query`](/doc/models/search-subscriptions-query.md) | Optional | Represents a query (including filtering criteria) used to search for subscriptions. |

## Example (as JSON)

```json
{
  "query": {
    "filter": {
      "customer_ids": [
        "CHFGVKYY8RSV93M5KCYTG4PN0G"
      ],
      "location_ids": [
        "S8GWD5R9QB376"
      ]
    }
  }
}
```

