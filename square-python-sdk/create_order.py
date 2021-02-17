{
    "idempotency_key": "09548a31-d4fc-4ae1-8be7-fe91429ea8fa",
    "location_id": "L4SN6DDDDRS2G",
    "order": {
      "location_id": "L4SN6DDDDRS2G",
      "customer_id": "Z592ZZJWJ8VVVEJXMHSADT4630",
      "discounts": [
        {
          "percentage": "12",
          "scope": "LINE_ITEM",
          "type": "UNKNOWN_DISCOUNT",
          "uid": "1",
          "name": "jjjj"
        }
      ],
      "fulfillments": [
        {
          "shipment_details": {
            "recipient": {
              "customer_id": "Z592ZZJWJ8VVVEJXMHSADT4630",
              "display_name": "Raul",
              "email_address": "raul@test.com",
              "phone_number": "1234567890"
            },
            "shipping_note": "A shipping note",
            "shipping_type": "Express",
            "tracking_number": "1234567891234567",
            "tracking_url": "trakingtrak.com",
            "carrier": "UPS"
          },
          "state": "PROPOSED",
          "type": "SHIPMENT"
        }
      ],
      "line_items": [
        {
          "quantity": "416",
          "catalog_object_id": "HGHG3PZRGHQQGGPRJ62WGUSK",
          "applied_discounts": [
            {
              "discount_uid": "1"
            }
          ],
          "applied_taxes": [
            {
              "tax_uid": "1"
            }
          ]
        }
      ],
      "state": "OPEN",
      "taxes": [
        {
          "percentage": "6",
          "scope": "ORDER",
          "type": "INCLUSIVE",
          "uid": "1",
          "name": "Tax1"
        }
      ]
    }
  }'