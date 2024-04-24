import os
from datetime import datetime
from typing import Optional, Annotated, List

import motor.motor_asyncio
from fastapi import FastAPI, Body, Header
from pydantic import BaseModel, Field, BeforeValidator, ConfigDict
from starlette import status

MONGO_CONNECT = os.getenv("MONGO_CONNECT", "mongodb://localhost:27017")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_CONNECT)
database = db = client.get_database("sms")
sms_collection = database.get_collection("sms_collection")

# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]


class SmsModel(BaseModel):
    """
    Single SMS record.
    """
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    phone: str = Field(...)
    message: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.now)
    headers: List[str] = Field(default=[])
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": "6629309a8be4bc9597a22e92",
                "phone": "+79950000000",
                "message": "Hello World",
                "created_at": "2024-04-24T20:30:55.793000",
                "headers": ["x-request-id: 12345-11-123-12", "Authorization: bearer"]
            }
        },
    )


class SmsCollection(BaseModel):
    """
    A container holding a list of `SmsModel` instances.
    """
    data: List[SmsModel]


app = FastAPI()


@app.post(
    "/api/messages/sms",
    response_description="Add new sms",
    response_model=SmsModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_sms(sms: SmsModel = Body(...),
                     authorization: Annotated[str | None, Header()] = None,
                     x_request_id: Annotated[str | None, Header()] = None
                     ):
    """
    Create new SMS
    """
    sms.headers = []
    if x_request_id:
        sms.headers.append(f'x-request-id: {x_request_id}')
    if authorization:
        sms.headers.append(f'Authorization: {authorization}')
    new_sms = await sms_collection.insert_one(
        sms.model_dump(by_alias=True, exclude=["id"])
    )
    created_sms = await sms_collection.find_one(
        {"_id": new_sms.inserted_id}
    )
    return created_sms


@app.get(
    "/api/messages/sms",
    response_description="List all sms",
    response_model=SmsCollection,
    response_model_by_alias=False,
)
async def list_sms():
    """
    List all SMSes in DB.

    The response is unpaginated and limited to 1000 results.
    """
    return SmsCollection(data=await sms_collection.find().to_list(1000))