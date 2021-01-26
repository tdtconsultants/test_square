
# Delete Invoice Request

Describes a `DeleteInvoice` request.

## Structure

`Delete Invoice Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `int` | Optional | The version of the [invoice](#type-invoice) to delete.<br>If you do not know the version, you can call [GetInvoice](#endpoint-Invoices-GetInvoice) or<br>[ListInvoices](#endpoint-Invoices-ListInvoices). |

## Example (as JSON)

```json
{
  "version": 172
}
```

