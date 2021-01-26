
# Get Team Member Wage Response

A response to a request to get a `TeamMemberWage`. Contains
the requested `TeamMemberWage` objects. May contain a set of `Error` objects if
the request resulted in errors.

## Structure

`Get Team Member Wage Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_wage` | [`Team Member Wage`](/doc/models/team-member-wage.md) | Optional | The hourly wage rate that a team member will earn on a `Shift` for doing the job<br>specified by the `title` property of this object. |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "team_member_wage": {
    "hourly_rate": {
      "amount": 2000,
      "currency": "USD"
    },
    "id": "pXS3qCv7BERPnEGedM4S8mhm",
    "team_member_id": "33fJchumvVdJwxV0H6L9",
    "title": "Manager"
  }
}
```

