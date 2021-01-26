
# Order Fulfillment Updated

## Structure

`Order Fulfillment Updated`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `string` | Optional | The order's unique ID. |
| `version` | `int` | Optional | Version number which is incremented each time an update is committed to the order.<br>Orders that were not created through the API will not include a version and<br>thus cannot be updated.<br><br>[Read more about working with versions](https://developer.squareup.com/docs/orders-api/manage-orders#update-orders) |
| `location_id` | `string` | Optional | The ID of the merchant location this order is associated with. |
| `state` | [`str (Order State)`](/doc/models/order-state.md) | Optional | The state of the order. |
| `created_at` | `string` | Optional | Timestamp for when the order was created in RFC 3339 format. |
| `updated_at` | `string` | Optional | Timestamp for when the order was last updated in RFC 3339 format. |
| `fulfillment_update` | [`List of Order Fulfillment Updated Update`](/doc/models/order-fulfillment-updated-update.md) | Optional | The fulfillments that were updated with this version change. |

## Example (as JSON)

```json
{
  "order_id": "order_id6",
  "version": 172,
  "location_id": "location_id4",
  "state": "CANCELED",
  "created_at": "created_at2"
}
```

