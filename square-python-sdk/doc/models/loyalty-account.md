
# Loyalty Account

Describes a loyalty account. For more information, see
[Loyalty Overview](https://developer.squareup.com/docs/loyalty/overview).

## Structure

`Loyalty Account`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The Square-assigned ID of the loyalty account. |
| `mappings` | [`List of Loyalty Account Mapping`](/doc/models/loyalty-account-mapping.md) |  | The list of mappings that the account is associated with.<br>Currently, a buyer can only be mapped to a loyalty account using<br>a phone number. Therefore, the list can only have one mapping. |
| `program_id` | `string` |  | The Square-assigned ID of the [loyalty program](#type-LoyaltyProgram) to which the account belongs. |
| `balance` | `int` | Optional | The available point balance in the loyalty account.<br><br>Your application should be able to handle loyalty accounts that have a negative point balance (`balance` is less than 0). This might occur if a seller makes a manual adjustment or as a result of a refund or exchange. |
| `lifetime_points` | `int` | Optional | The total points accrued during the lifetime of the account. |
| `customer_id` | `string` | Optional | The Square-assigned ID of the [customer](#type-Customer) that is associated with the account. |
| `enrolled_at` | `string` | Optional | The timestamp when enrollment occurred, in RFC 3339 format. |
| `created_at` | `string` | Optional | The timestamp when the loyalty account was created, in RFC 3339 format. |
| `updated_at` | `string` | Optional | The timestamp when the loyalty account was last updated, in RFC 3339 format. |

## Example (as JSON)

```json
{
  "id": "id0",
  "mappings": [
    {
      "id": "id4",
      "type": "type6",
      "value": "value6",
      "created_at": "created_at8"
    }
  ],
  "program_id": "program_id0",
  "balance": 64,
  "lifetime_points": 88,
  "customer_id": "customer_id8",
  "enrolled_at": "enrolled_at0"
}
```

