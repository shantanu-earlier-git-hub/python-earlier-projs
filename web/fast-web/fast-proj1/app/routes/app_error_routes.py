from fastapi import APIRouter

from app.models import AppException

router = APIRouter(
    prefix="/error",
    tags=["errors"],
    responses={404: {"description": "Not found"}},
    include_in_schema=False,
    dependencies=[],
)


@router.get("/")
async def handle_error(app_exception: AppException):
    return app_exception
