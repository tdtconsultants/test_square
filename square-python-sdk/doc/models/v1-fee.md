
# V1 Fee

V1Fee

## Structure

`V1 Fee`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The fee's unique ID. |
| `name` | `string` | Optional | The fee's name. |
| `rate` | `string` | Optional | The rate of the fee, as a string representation of a decimal number. A value of 0.07 corresponds to a rate of 7%. |
| `calculation_phase` | [`str (V1 Fee Calculation Phase)`](/doc/models/v1-fee-calculation-phase.md) | Optional | - |
| `adjustment_type` | [`str (V1 Fee Adjustment Type)`](/doc/models/v1-fee-adjustment-type.md) | Optional | - |
| `applies_to_custom_amounts` | `bool` | Optional | If true, the fee applies to custom amounts entered into Square Point of Sale that are not associated with a particular item. |
| `enabled` | `bool` | Optional | If true, the fee is applied to all appropriate items. If false, the fee is not applied at all. |
| `inclusion_type` | [`str (V1 Fee Inclusion Type)`](/doc/models/v1-fee-inclusion-type.md) | Optional | - |
| `type` | [`str (V1 Fee Type)`](/doc/models/v1-fee-type.md) | Optional | - |
| `v2_id` | `string` | Optional | The ID of the CatalogObject in the Connect v2 API. Objects that are shared across multiple locations share the same v2 ID. |

## Example (as JSON)

```json
{
  "id": "id0",
  "name": "name0",
  "rate": "rate0",
  "calculation_phase": "FEE_TOTAL_PHASE",
  "adjustment_type": "TAX"
}
```

