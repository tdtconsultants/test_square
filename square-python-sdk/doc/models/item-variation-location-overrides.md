
# Item Variation Location Overrides

Price and inventory alerting overrides for a `CatalogItemVariation` at a specific `Location`.

## Structure

`Item Variation Location Overrides`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Optional | The ID of the `Location`. |
| `price_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `pricing_type` | [`str (Catalog Pricing Type)`](/doc/models/catalog-pricing-type.md) | Optional | Indicates whether the price of a CatalogItemVariation should be entered manually at the time of sale. |
| `track_inventory` | `bool` | Optional | If `true`, inventory tracking is active for the `CatalogItemVariation` at this `Location`. |
| `inventory_alert_type` | [`str (Inventory Alert Type)`](/doc/models/inventory-alert-type.md) | Optional | Indicates whether Square should alert the merchant when the inventory quantity of a CatalogItemVariation is low. |
| `inventory_alert_threshold` | `long|int` | Optional | If the inventory quantity for the variation is less than or equal to this value and `inventory_alert_type`<br>is `LOW_QUANTITY`, the variation displays an alert in the merchant dashboard.<br><br>This value is always an integer. |

## Example (as JSON)

```json
{
  "location_id": "location_id4",
  "price_money": {
    "amount": 202,
    "currency": "BBD"
  },
  "pricing_type": "FIXED_PRICING",
  "track_inventory": false,
  "inventory_alert_type": "NONE"
}
```

