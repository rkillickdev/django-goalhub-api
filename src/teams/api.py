from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

from ninja_jwt.authentication import JWTAuth

from .models import Team
from .schemas import (
    TeamEntryCreateSchema,
    TeamEntryListSchema,
    TeamEntryDetailSchema,
)

router = Router()


# /api/teams/
@router.get("", response=List[TeamEntryListSchema], auth=JWTAuth())
def list_team_entries(request):
    qs = Team.objects.all()
    return qs


# /api/teams/
@router.post("", response=TeamEntryDetailSchema)
def create_team_entry(request, data: TeamEntryCreateSchema):
    print(data)
    obj = Team.objects.create(**data.dict())
    return obj


@router.get("{entry_id}/", response=TeamEntryDetailSchema, auth=JWTAuth())
def get_team_entry(request, entry_id: int):
    obj = get_object_or_404(Team, id=entry_id)
    return obj
