from fastapi import Header, HTTPException
from fastapi import Request
import logging


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


# async def get_query_token(token: str, request: Request):
async def get_query_token(request: Request):

    logging.info(request.url.path)
    logging.info(request.headers)
    logging.info(request.query_params)
    if request.url.path == '/docs':
        pass
    # if token != "jessica":
    #    raise HTTPException(status_code=400, detail="No Jessica token provided")
