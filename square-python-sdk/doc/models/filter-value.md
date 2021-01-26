
# Filter Value

A filter to select resources based on an exact field value. For any given
value, the value can only be in one property. Depending on the field, either
all properties can be set or only a subset will be available.

Refer to the documentation of the field.

## Structure

`Filter Value`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `all` | `List of string` | Optional | A list of terms that must be present on the field of the resource. |
| `any` | `List of string` | Optional | A list of terms where at least one of them must be present on the<br>field of the resource. |
| `none` | `List of string` | Optional | A list of terms that must not be present on the field the resource |

## Example (as JSON)

```json
{
  "all": [
    "all1",
    "all2"
  ],
  "any": [
    "any6"
  ],
  "none": [
    "none1",
    "none2",
    "none3"
  ]
}
```

