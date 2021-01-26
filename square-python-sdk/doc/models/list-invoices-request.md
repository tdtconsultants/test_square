
# List Invoices Request

Describes a `ListInvoice` request.

## Structure

`List Invoices Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` |  | The ID of the location for which to list invoices. |
| `cursor` | `string` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for your original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |
| `limit` | `int` | Optional | The maximum number of invoices to return (200 is the maximum `limit`).<br>If not provided, the server<br>uses a default limit of 100 invoices. |

## Example (as JSON)

```json
{
  "location_id": "location_id4",
  "cursor": "cursor6",
  "limit": 172
}
```

