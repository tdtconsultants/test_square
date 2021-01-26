
# Cancel Invoice Request

Describes a `CancelInvoice` request.

## Structure

`Cancel Invoice Request`

## Fields

| Name | Type | Description |
|  --- | --- | --- |
| `version` | `int` | The version of the [invoice](#type-invoice) to cancel.<br>If you do not know the version, you can call<br>[GetInvoice](#endpoint-Invoices-GetInvoice) or [ListInvoices](#endpoint-Invoices-ListInvoices). |

## Example (as JSON)

```json
{
  "version": 0
}
```

