
# Dispute Evidence File

A file to be uploaded as dispute evidence.

## Structure

`Dispute Evidence File`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filename` | `string` | Optional | The file name including the file extension. For example: "receipt.tiff". |
| `filetype` | `string` | Optional | Dispute evidence files must be application/pdf, image/heic, image/heif, image/jpeg, image/png, or image/tiff formats. |

## Example (as JSON)

```json
{
  "filename": "filename2",
  "filetype": "filetype2"
}
```

