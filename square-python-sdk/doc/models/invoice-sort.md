
# Invoice Sort

Identifies the  sort field and sort order.

## Structure

`Invoice Sort`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | `string` |  | Field to use for sorting.<br>*Default: `'INVOICE_SORT_DATE'`* |
| `order` | [`str (Sort Order)`](/doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |

## Example (as JSON)

```json
{
  "field": "field6",
  "order": "DESC"
}
```

