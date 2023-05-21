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

## Installation

1. Create a virtual environment: `conda create -n code-snapshot-test-env -y python=3.8`
1. Activate the environment: `conda activate code-snapshot-test-env`
1. Install the package `pip install -i https://test.pypi.org/simple/ code-snapshot`

## Usage

1. Set the Showcode API token as an environment variable following [Getting started](#getting-started) section
1. Write a python script as following:

   ```python
   from code_snapshot.code_snapshot import CodeSnapshot
   from code_snapshot.models import CodeSnapshotSettings, CodeSnapshotEditor

   if __name__ == "__main__":
      settings=CodeSnapshotSettings(
         title="Hello world in Python",
      )
      editor=CodeSnapshotEditor(
         value="""
   def greet(name):
      print(f"Hello {name}!")

   greet("World")
         """
      )
      cs = CodeSnapshot()
      cs.save_snapshot(settings, editor, filepath="./code_snapshot.png")

   ```

1. Run the python script `python main.py`. This should generate a file `code_snapshot.png` in the same directory as `main.py`.
1. It should look like this:
   ![code_snapshot](https://github.com/ainomic/code-snapshot/blob/0.1.5/code_snapshot.png)
1. You can use `cs.generate_snapshot(settings, editor)` to consume `bytes` if required.
