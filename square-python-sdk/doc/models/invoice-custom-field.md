
# Invoice Custom Field

An additional seller-defined and customer-facing field to include on the invoice. For more information,
see [Custom fields](https://developer.squareup.com/docs/invoices-api/overview#custom-fields).

## Structure

`Invoice Custom Field`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `label` | `string` | Optional | The label or title of the custom field. This field is required for a custom field. |
| `value` | `string` | Optional | The text of the custom field. If omitted, only the label is rendered. |
| `placement` | [`str (Invoice Custom Field Placement)`](/doc/models/invoice-custom-field-placement.md) | Optional | Indicates where to render a custom field on the Square-hosted invoice page and in emailed or PDF<br>copies of the invoice. |

## Example (as JSON)

```json
{
  "label": "label0",
  "value": "value2",
  "placement": "ABOVE_LINE_ITEMS"
}
```

