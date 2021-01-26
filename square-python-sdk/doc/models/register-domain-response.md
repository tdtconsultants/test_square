
# Register Domain Response

Defines the fields that are included in the response body of
a request to the [RegisterDomain](#endpoint-registerdomain) endpoint.

Either `errors` or `status` will be present in a given response (never both).

## Structure

`Register Domain Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `status` | [`str (Register Domain Response Status)`](/doc/models/register-domain-response-status.md) | Optional | The status of domain registration. |

## Example (as JSON)

```json
{
  "status": "VERIFIED"
}
```

