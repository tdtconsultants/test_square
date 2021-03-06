
# Dispute

Represents a dispute a cardholder initiated with their bank.

## Structure

`Dispute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_id` | `string` | Optional | The unique ID for this `Dispute`, generated by Square. |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `reason` | [`str (Dispute Reason)`](/doc/models/dispute-reason.md) | Optional | The list of possible reasons why a cardholder might initiate a<br>dispute with their bank. |
| `state` | [`str (Dispute State)`](/doc/models/dispute-state.md) | Optional | The list of possible dispute states. |
| `due_at` | `string` | Optional | The time when the next action is due, in RFC 3339 format. |
| `disputed_payment` | [`Disputed Payment`](/doc/models/disputed-payment.md) | Optional | The payment the cardholder disputed. |
| `evidence_ids` | `List of string` | Optional | The IDs of the evidence associated with the dispute. |
| `card_brand` | [`str (Card Brand)`](/doc/models/card-brand.md) | Optional | Indicates a card's brand, such as `VISA` or `MASTERCARD`. |
| `created_at` | `string` | Optional | The timestamp when the dispute was created, in RFC 3339 format. |
| `updated_at` | `string` | Optional | The timestamp when the dispute was last updated, in RFC 3339 format. |
| `brand_dispute_id` | `string` | Optional | The ID of the dispute in the card brand system, generated by the card brand. |
| `reported_date` | `string` | Optional | The timestamp when the dispute was reported, in RFC 3339 format. |
| `version` | `int` | Optional | The current version of the `Dispute`. |
| `location_id` | `string` | Optional | The ID of the location where the dispute originated. |

## Example (as JSON)

```json
{
  "dispute_id": "dispute_id2",
  "amount_money": {
    "amount": 186,
    "currency": "NGN"
  },
  "reason": "NOT_AS_DESCRIBED",
  "state": "EVIDENCE_REQUIRED",
  "due_at": "due_at2"
}
```

