
# Catalog Subscription Plan

Describes a subscription plan. For more information, see
[Set Up and Manage a Subscription Plan](https://developer.squareup.com/docs/subscriptions-api/setup-plan).

## Structure

`Catalog Subscription Plan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The name of the plan. |
| `phases` | [`List of Subscription Phase`](/doc/models/subscription-phase.md) | Optional | A list of SubscriptionPhase containing the [SubscriptionPhase](#type-SubscriptionPhase) for this plan. |

## Example (as JSON)

```json
{
  "name": "name0",
  "phases": [
    {
      "uid": "uid5",
      "cadence": "EVERY_FOUR_MONTHS",
      "periods": 241,
      "recurring_price_money": {
        "amount": 193,
        "currency": "MOP"
      },
      "ordinal": 207
    },
    {
      "uid": "uid6",
      "cadence": "QUARTERLY",
      "periods": 242,
      "recurring_price_money": {
        "amount": 194,
        "currency": "MRO"
      },
      "ordinal": 208
    }
  ]
}
```

