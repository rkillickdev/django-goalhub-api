from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

import helpers
from ninja_jwt.authentication import JWTAuth

from .models import Team
from .schemas import (
    TeamEntryCreateSchema,
    TeamEntryListSchema,
    TeamEntryDetailSchema,
)

router = Router()


# /api/teams/
@router.get(
    "", response=List[TeamEntryListSchema], auth=helpers.api_auth_user_required
)
def list_team_entries(request):
    qs = Team.objects.filter(user=request.user)
    return qs


# /api/teams/
@router.post(
    "", response=TeamEntryDetailSchema, auth=helpers.api_auth_user_or_annon
)
def create_team_entry(request, data: TeamEntryCreateSchema):
    obj = Team(**data.dict())
    print(request.user)
    # obj.user = request.user
    if request.user.is_authenticated:
        obj.user = request.user
    obj.save()
    return obj


@router.get(
    "{entry_id}/",
    response=TeamEntryDetailSchema,
    auth=helpers.api_auth_user_required,
)
def get_team_entry(request, entry_id: int):
    obj = get_object_or_404(Team, id=entry_id, user=request.user)
    return obj
