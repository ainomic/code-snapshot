# Code snapshot

Create a snapshot image for your code to share the formatted code anywhere. We use [SHOWCODE api](https://api.showcode.app) to create a PNG image for the specified code snippet.

## Getting started

1. Create an account on [Showcode App](https://api.showcode.app/register) to fetch the API key.
1. Sign in to the account and create an API token:
   1. Token name: _Provide a name to the token which you can remember where it is being used_
   1. Check "read" permissions
   1. Copy the token displayed and store somewhere in safe. __Note: This token won't be shown again, so you need to paste it before you close the window__

   ![Create API token snapshot](https://github.com/ainomic/code-snapshot/blob/0.1.3/Showcode_API_token.png)
1. Export an environment variable to store the token in the terminal: `export SHOWCODE_API_KEY={API Token}`
1. Now, you're ready to use the package in your applications.
