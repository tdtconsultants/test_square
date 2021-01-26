
# Order Line Item Pricing Blocklists Blocked Discount

A discount to block from applying to a line item. The discount must be
identified by either `discount_uid` or `discount_catalog_object_id`, but not both.

## Structure

`Order Line Item Pricing Blocklists Blocked Discount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | Unique ID of the `BlockedDiscount` within the order. |
| `discount_uid` | `string` | Optional | The `uid` of the discount that should be blocked. Use this field to block<br>ad-hoc discounts. For catalog discounts use the `discount_catalog_object_id` field. |
| `discount_catalog_object_id` | `string` | Optional | The `catalog_object_id` of the discount that should be blocked.<br>Use this field to block catalog discounts. For ad-hoc discounts use the<br>`discount_uid` field. |

## Example (as JSON)

```json
{
  "uid": "uid0",
  "discount_uid": "discount_uid4",
  "discount_catalog_object_id": "discount_catalog_object_id2"
}
```

