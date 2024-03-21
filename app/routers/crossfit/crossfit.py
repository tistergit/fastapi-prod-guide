from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.utilities.logger import logger
from app.utilities.mdb import get_db_session

from .models import Users
from .schemas import NotFoundException, UserModel

router = APIRouter()




@router.get(
    "/{id}",
    response_model=UserModel,
    responses={
        404: {"description": "Not Found", "model": NotFoundException},
    },
)
async def get_user(
    id: str = Path(description="Todo ID"),
    session: AsyncSession = Depends(get_db_session)
) -> UserModel:
    """
    Get a User
    """
    u = await session.get(Users, id)
    logger.info("user : %s "  %  u)
    if u is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist",
        )
    return UserModel(
        id=u.id,
        name=u.name,
        email=u.email,
    )
