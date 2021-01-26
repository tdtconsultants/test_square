
# Invoice Filter

Describes query filters to apply.

## Structure

`Invoice Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_ids` | `List of string` |  | Limits the search to the specified locations. A location is required.<br>In the current implementation, only one location can be specified. |
| `customer_ids` | `List of string` | Optional | Limits the search to the specified customers, within the specified locations.<br>Specifying a customer is optional. In the current implementation,<br>a maximum of one customer can be specified. |

## Example (as JSON)

```json
{
  "location_ids": [
    "location_ids0"
  ],
  "customer_ids": [
    "customer_ids1",
    "customer_ids2"
  ]
}
```

