
# Search Orders Source Filter

Filter based on order `source` information.

## Structure

`Search Orders Source Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_names` | `List of string` | Optional | Filters by [Source](#type-ordersource) `name`. Will return any orders<br>with with a `source.name` that matches any of the listed source names.<br><br>Max: 10 source names. |

## Example (as JSON)

```json
{
  "source_names": [
    "source_names8"
  ]
}
```

