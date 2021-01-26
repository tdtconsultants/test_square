
# Obtain Token Request

## Structure

`Obtain Token Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `string` |  | The Square-issued ID of your application, available from the<br>[application dashboard](https://connect.squareup.com/apps). |
| `client_secret` | `string` |  | The Square-issued application secret for your application, available<br>from the [application dashboard](https://connect.squareup.com/apps). |
| `code` | `string` | Optional | The authorization code to exchange.<br>This is required if `grant_type` is set to `authorization_code`, to indicate that<br>the application wants to exchange an authorization code for an OAuth access token. |
| `redirect_uri` | `string` | Optional | The redirect URL assigned in the [application dashboard](https://connect.squareup.com/apps). |
| `grant_type` | `string` |  | Specifies the method to request an OAuth access token.<br>Valid values are: `authorization_code`, `refresh_token`, and `migration_token` |
| `refresh_token` | `string` | Optional | A valid refresh token for generating a new OAuth access token.<br>A valid refresh token is required if `grant_type` is set to `refresh_token` ,<br>to indicate the application wants a replacement for an expired OAuth access token. |
| `migration_token` | `string` | Optional | Legacy OAuth access token obtained using a Connect API version prior<br>to 2019-03-13. This parameter is required if `grant_type` is set to<br>`migration_token` to indicate that the application wants to get a replacement<br>OAuth access token. The response also returns a refresh token.<br>For more information, see [Migrate to Using Refresh Tokens](https://developer.squareup.com/docs/authz/oauth/migration). |
| `scopes` | `List of string` | Optional | __OPTIONAL__<br><br>A JSON list of strings representing the permissions the application is requesting.<br>For example: "`["MERCHANT_PROFILE_READ","PAYMENTS_READ","BANK_ACCOUNTS_READ"]`"<br>The access token returned in the response is granted the permissions<br>that comprise the intersection between the requested list of permissions, and those<br>that belong to the provided refresh token. |
| `short_lived` | `bool` | Optional | __OPTIONAL__<br><br>A boolean indicating a request for a short-lived access token.<br>The short-lived access token returned in the response will expire in 24 hours. |

## Example (as JSON)

```json
{
  "client_id": "APPLICATION_ID",
  "client_secret": "APPLICATION_SECRET",
  "code": "CODE_FROM_AUTHORIZE",
  "grant_type": "authorization_code"
}
```

