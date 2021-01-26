
# V1 Employee Role

V1EmployeeRole

## Structure

`V1 Employee Role`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The role's unique ID, Can only be set by Square. |
| `name` | `string` |  | The role's merchant-defined name. |
| `permissions` | [`List of str (V1 Employee Role Permissions)`](/doc/models/v1-employee-role-permissions.md) |  | The role's permissions.<br>See [V1EmployeeRolePermissions](#type-v1employeerolepermissions) for possible values |
| `is_owner` | `bool` | Optional | If true, employees with this role have all permissions, regardless of the values indicated in permissions. |
| `created_at` | `string` | Optional | The time when the employee entity was created, in ISO 8601 format. Is set by Square when the Role is created. |
| `updated_at` | `string` | Optional | The time when the employee entity was most recently updated, in ISO 8601 format. Is set by Square when the Role updated. |

## Example (as JSON)

```json
{
  "id": "id0",
  "name": "name0",
  "permissions": [
    "REGISTER_OPEN_CASH_DRAWER_OUTSIDE_SALE",
    "REGISTER_VIEW_SUMMARY_REPORTS"
  ],
  "is_owner": false,
  "created_at": "created_at2",
  "updated_at": "updated_at4"
}
```

