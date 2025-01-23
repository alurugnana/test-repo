from fastapi import APIRouter, Depends
from core.auth import get_auth

from services.app_details import fetch_app_details

router = APIRouter()


@router.get(
    "/api/services/ts",
    dependencies=[Depends(get_auth)],
)
def get_app_details():
    app_details = fetch_app_details()
    return app_details


