from fastapi import APIRouter

from app.api.endpoints import user

main_router = APIRouter()
for router in (user.router,):
    main_router.include_router(router)
