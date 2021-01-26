
# Get Break Type Response

The response to a request to get a `BreakType`. Contains
the requested `BreakType` objects. May contain a set of `Error` objects if
the request resulted in errors.

## Structure

`Get Break Type Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `break_type` | [`Break Type`](/doc/models/break-type.md) | Optional | A defined break template that sets an expectation for possible `Break`<br>instances on a `Shift`. |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "break_type": {
    "break_name": "Lunch Break",
    "created_at": "2019-02-21T17:50:00Z",
    "expected_duration": "PT30M",
    "id": "lA0mj_RSOprNPwMUXdYp",
    "is_paid": true,
    "location_id": "059SB0E0WCNWS",
    "updated_at": "2019-02-21T17:50:00Z",
    "version": 1
  }
}
```

