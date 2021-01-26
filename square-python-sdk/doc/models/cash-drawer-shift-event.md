
# Cash Drawer Shift Event

## Structure

`Cash Drawer Shift Event`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The unique ID of the event. |
| `employee_id` | `string` | Optional | The ID of the employee that created the event. |
| `event_type` | [`str (Cash Drawer Event Type)`](/doc/models/cash-drawer-event-type.md) | Optional | The types of events on a CashDrawerShift.<br>Each event type represents an employee action on the actual cash drawer<br>represented by a CashDrawerShift. |
| `event_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `created_at` | `string` | Optional | The event time in ISO 8601 format. |
| `description` | `string` | Optional | An optional description of the event, entered by the employee that<br>created the event. |

## Example (as JSON)

```json
{
  "id": "id0",
  "employee_id": "employee_id0",
  "event_type": "OTHER_TENDER_CANCELLED_PAYMENT",
  "event_money": {
    "amount": 148,
    "currency": "HTG"
  },
  "created_at": "created_at2"
}
```

