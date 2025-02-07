from typing import List
import json
from django.shortcuts import get_object_or_404
from ninja import Router

import helpers
from ninja_jwt.authentication import JWTAuth

from .forms import TeamCreateForm

from .models import Team
from .schemas import (
    TeamEntryCreateSchema,
    TeamEntryListSchema,
    TeamEntryDetailSchema,
    ErrorTeamEntryCreateSchema,
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
    "",
    response={201: TeamEntryDetailSchema, 400: ErrorTeamEntryCreateSchema},
    auth=helpers.api_auth_user_or_annon,
)
def create_team_entry(request, data: TeamEntryCreateSchema):
    form = TeamCreateForm(data.dict())
    if not form.is_valid():
        # Commented out code below would work if using a standard from rather than Model Form

        # cleaned_data = form.cleaned_data
        # obj = Team(**cleaned_data.dict())

        # Below turns json data into a dictionary
        form_errors = json.loads(form.errors.as_json())
        print(form_errors)
        return 400, form_errors
    obj = form.save(commit=False)
    print(request.user)
    # obj.user = request.user
    if request.user.is_authenticated:
        obj.user = request.user
    obj.save()
    return 201, obj


@router.get(
    "{entry_id}/",
    response=TeamEntryDetailSchema,
    auth=helpers.api_auth_user_required,
)
def get_team_entry(request, entry_id: int):
    obj = get_object_or_404(Team, id=entry_id, user=request.user)
    return obj
