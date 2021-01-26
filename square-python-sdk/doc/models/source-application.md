
# Source Application

Provides information about the application used to generate a change.

## Structure

`Source Application`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product` | [`str (Product)`](/doc/models/product.md) | Optional | Indicates the Square product used to generate an inventory change. |
| `application_id` | `string` | Optional | Read-only Square ID assigned to the application. Only used for<br>[Product](#type-product) type `EXTERNAL_API`. |
| `name` | `string` | Optional | Read-only display name assigned to the application<br>(e.g. `"Custom Application"`, `"Square POS 4.74 for Android"`). |

## Example (as JSON)

```json
{
  "product": "SQUARE_POS",
  "application_id": "application_id4",
  "name": "name0"
}
```

