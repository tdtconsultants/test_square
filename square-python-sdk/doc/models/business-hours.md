
# Business Hours

Represents the hours of operation for a business location.

## Structure

`Business Hours`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `periods` | [`List of Business Hours Period`](/doc/models/business-hours-period.md) | Optional | The list of time periods during which the business is open. There may be at most 10<br>periods per day. |

## Example (as JSON)

```json
{
  "periods": [
    {
      "day_of_week": "MON",
      "start_local_time": "start_local_time5",
      "end_local_time": "end_local_time7"
    },
    {
      "day_of_week": "SUN",
      "start_local_time": "start_local_time6",
      "end_local_time": "end_local_time8"
    },
    {
      "day_of_week": "SAT",
      "start_local_time": "start_local_time7",
      "end_local_time": "end_local_time9"
    }
  ]
}
```

