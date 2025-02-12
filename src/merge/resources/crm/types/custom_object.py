# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .remote_field import RemoteField


class CustomObject(pydantic.BaseModel):
    """
    # The CustomObject Object
    ### Description
    The `Custom Object` record refers to an instance of a Custom Object Class.
    ### Usage Example
    TODO
    """

    object_class: typing.Optional[str]
    fields: typing.Optional[typing.Dict[str, typing.Any]]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    id: typing.Optional[str]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    remote_fields: typing.Optional[typing.List[RemoteField]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
