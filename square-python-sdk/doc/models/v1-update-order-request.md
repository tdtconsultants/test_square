
# V1 Update Order Request

V1UpdateOrderRequest

## Structure

`V1 Update Order Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`str (V1 Update Order Request Action)`](/doc/models/v1-update-order-request-action.md) |  | - |
| `shipped_tracking_number` | `string` | Optional | The tracking number of the shipment associated with the order. Only valid if action is COMPLETE. |
| `completed_note` | `string` | Optional | A merchant-specified note about the completion of the order. Only valid if action is COMPLETE. |
| `refunded_note` | `string` | Optional | A merchant-specified note about the refunding of the order. Only valid if action is REFUND. |
| `canceled_note` | `string` | Optional | A merchant-specified note about the canceling of the order. Only valid if action is CANCEL. |

## Example (as JSON)

```json
{
  "action": "COMPLETE",
  "shipped_tracking_number": "shipped_tracking_number0",
  "completed_note": "completed_note0",
  "refunded_note": "refunded_note4",
  "canceled_note": "canceled_note0"
}
```

