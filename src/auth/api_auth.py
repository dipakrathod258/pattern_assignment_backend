from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader
from config.http_configs import HttpStatusCodes

API_KEY_NAME = "access-token"
api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
        api_key_query: str = Security(api_key_query),
        api_key_header: str = Security(api_key_header),
):
    """This function provides the security to our API. This function returns True or False based on whether
     access-token received in API request header is as same as what is expected"""

    api_key = "37mid0DAL9RPo2H"

    if api_key_query == api_key:
        return api_key_query
    elif api_key_header == api_key:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HttpStatusCodes.HTTP_403_FORBIDDEN_ERROR, detail="API auth Credentials are Invalid"
        )
