from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Team
from .schemas import TeamEntryListSchema, TeamEntryDetailSchema

router = Router()


@router.get("", response=List[TeamEntryListSchema])
def list_team_entries(request):
    qs = Team.objects.all()
    return qs


@router.get("{entry_id}/", response=TeamEntryDetailSchema)
def get_team_entry(request, entry_id: int):
    obj = get_object_or_404(Team, id=entry_id)
    return obj
