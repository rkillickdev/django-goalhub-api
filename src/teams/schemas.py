from typing import List, Any
from datetime import datetime
from ninja import Schema


class TeamEntryCreateSchema(Schema):
    # Create -> Data
    # TeamEntryIn
    name: str


class ErrorTeamEntryCreateSchema(Schema):
    # Create -> Data
    # TeamEntryIn
    name: List[Any]
    # non_field_errors: List[dict] = []


class TeamEntryListSchema(Schema):
    # List -> Data
    # TeamEntryOut
    id: int
    name: str


class TeamEntryDetailSchema(Schema):
    # Get -> Data
    # TeamEntryOut
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
