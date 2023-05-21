"""CodeSnapshot class for interacting with the Showcode api."""
import os

import requests

from code_snapshot.models import CodeSnapshotEditor, CodeSnapshotSettings


class CodeSnapshot:
    """CodeSnapshot class for interacting with the Showcode api."""
    __BASE_URL__ = "https://api.showcode.app"

    def __init__(self, showcode_api_key: str = None) -> None:
        """Initialize the CodeSnapshot class using `showcode_api_key` (either in argument, or setting environment variable `SHOWCODE_API_KEY`)."""
        if showcode_api_key is None:
            showcode_api_key = os.environ.get("SHOWCODE_API_KEY")
        self.showcode_api_key = showcode_api_key

    def generate_snapshot(self, settings: CodeSnapshotSettings, editor: CodeSnapshotEditor) -> bytes:
        """Generate a snapshot using `settings` and `editor` objects."""
        url = f"{self.__BASE_URL__}/generate"
        headers = {
            "Authorization": f"Bearer {self.showcode_api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        data = {
            "settings": settings.__dict__,
            "editors": [
                editor.__dict__,
            ],
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            return response.content
        else:
            raise Exception(
                f"Failed to generate screenshot. Status code: {response.status_code}. Response: {response.json()}"
            )

    def save_snapshot(self, settings: CodeSnapshotSettings, editor: CodeSnapshotEditor, filepath: str) -> None:
        """Save a snapshot to `filepath` using `settings` and `editor` objects."""
        dir = os.path.dirname(filepath)
        if not os.path.exists(dir):
            raise Exception(
                f"Directory does not exist or unreachable: {dir} for filepath: {filepath}")

        screenshot = self.generate_snapshot(settings, editor)
        with open(filepath, "wb") as file:
            file.write(screenshot)
