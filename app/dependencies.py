from fastapi import Depends, HTTPException, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth import verify_token
from typing import Optional

security = HTTPBearer(auto_error=False)


async def verify_api_key(x_api_key: str = Header(...)):
    from app.core.config import API_KEY

    if x_api_key != API_KEY:
        raise HTTPException(401, "Invalid API key")
    return x_api_key


async def verify_token_dep(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    if not credentials:
        raise HTTPException(401, "Not authenticated")

    token = credentials.credentials
    username = verify_token(token)

    if not username:
        raise HTTPException(401, "Invalid or expired token")

    return username


async def get_current_user_or_none() -> Optional[str]:
    credentials = await security(None)
    if not credentials:
        return None

    token = credentials.credentials
    username = verify_token(token)

    return username
