
# Retrieve Catalog Object Request

## Structure

`Retrieve Catalog Object Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_related_objects` | `bool` | Optional | If `true`, the response will include additional objects that are related to the<br>requested object, as follows:<br><br>If the `object` field of the response contains a `CatalogItem`, its associated<br>`CatalogCategory`, `CatalogTax`, `CatalogImage` and `CatalogModifierList` objects will<br>be returned in the `related_objects` field of the response. If the `object` field of<br>the response contains a `CatalogItemVariation`, its parent `CatalogItem` will be returned<br>in the `related_objects` field of the response.<br><br>Default value: `false` |
| `catalog_version` | `long|int` | Optional | Requests objects as of a specific version of the catalog. This allows you to retrieve historical<br>versions of objects. The value to retrieve a specific version of an object can be found<br>in the version field of [CatalogObject](#type-catalogobject)s. |

## Example (as JSON)

```json
{
  "include_related_objects": false,
  "catalog_version": 126
}
```

