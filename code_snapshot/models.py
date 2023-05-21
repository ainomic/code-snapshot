"""Models for the code_snapshot library."""
from dataclasses import dataclass


@dataclass
class CodeSnapshotSettings:
    """Settings for the Showcode api."""
    title: str
    showLineNumbers: bool = True
    themeName: str = "github-dark"
    background: str = "ocean"


@dataclass
class CodeSnapshotEditor:
    """Editor for the Showcode api."""
    value: str
    language: str = "python"
