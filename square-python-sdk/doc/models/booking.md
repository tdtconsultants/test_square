
# Booking

Represents a booking as a time-bound service contract for a seller's staff member to provide a specified service
at a given location to a requesting customer in one or more appointment segments.

## Structure

`Booking`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | A unique ID of this object representing a booking. |
| `version` | `int` | Optional | The revision number for the booking used for optimistic concurrency. |
| `status` | [`str (Booking Status)`](/doc/models/booking-status.md) | Optional | Supported booking statuses. |
| `created_at` | `string` | Optional | The timestamp specifying the creation time of this booking. |
| `updated_at` | `string` | Optional | The timestamp specifying the most recent update time of this booking. |
| `start_at` | `string` | Optional | The timestamp specifying the starting time of this booking. |
| `location_id` | `string` | Optional | The ID of the [Location](#type-location) object representing the location where the booked service is provided. |
| `customer_id` | `string` | Optional | The ID of the [Customer](#type-Customer) object representing the customer attending this booking |
| `customer_note` | `string` | Optional | The free-text field for the customer to supply notes about the booking. For example, the note can be preferences that cannot be expressed by supported attributes of a relevant [CatalogObject](#type-CatalogObject) instance. |
| `seller_note` | `string` | Optional | The free-text field for the seller to supply notes about the booking. For example, the note can be preferences that cannot be expressed by supported attributes of a specific [CatalogObject](#type-CatalogObject) instance.<br>This field should not be visible to customers. |
| `appointment_segments` | [`List of Appointment Segment`](/doc/models/appointment-segment.md) | Optional | A list of appointment segments for this booking. |

## Example (as JSON)

```json
{
  "id": "id0",
  "version": 172,
  "status": "CANCELLED_BY_SELLER",
  "created_at": "created_at2",
  "updated_at": "updated_at4"
}
```

