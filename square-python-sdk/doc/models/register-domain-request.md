
# Register Domain Request

Defines the parameters that can be included in the body of
a request to the [RegisterDomain](#endpoint-registerdomain) endpoint.

## Structure

`Register Domain Request`

## Fields

| Name | Type | Description |
|  --- | --- | --- |
| `domain_name` | `string` | A domain name as described in RFC-1034 that will be registered with ApplePay |

## Example (as JSON)

```json
{
  "domain_name": "example.com"
}
```

