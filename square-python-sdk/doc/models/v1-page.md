
# V1 Page

V1Page

## Structure

`V1 Page`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The page's unique identifier. |
| `name` | `string` | Optional | The page's name, if any. |
| `page_index` | `int` | Optional | The page's position in the merchant's list of pages. Always an integer between 0 and 6, inclusive. |
| `cells` | [`List of V1 Page Cell`](/doc/models/v1-page-cell.md) | Optional | The cells included on the page. |

## Example (as JSON)

```json
{
  "id": "id0",
  "name": "name0",
  "page_index": 216,
  "cells": [
    {
      "page_id": "page_id2",
      "row": 10,
      "column": 72,
      "object_type": "ITEM",
      "object_id": "object_id0"
    },
    {
      "page_id": "page_id3",
      "row": 9,
      "column": 73,
      "object_type": "DISCOUNT",
      "object_id": "object_id1"
    },
    {
      "page_id": "page_id4",
      "row": 8,
      "column": 74,
      "object_type": "CATEGORY",
      "object_id": "object_id2"
    }
  ]
}
```

