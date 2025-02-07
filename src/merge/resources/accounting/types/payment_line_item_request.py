# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .payment_line_item_request_related_object_type import PaymentLineItemRequestRelatedObjectType


class PaymentLineItemRequest(pydantic.BaseModel):
    """
    # The PaymentLineItem Object
    ### Description
    The `PaymentLineItem` object is an applied-to-line on a `Payment` that can either be a `Invoice`, `CreditNote`, or `JournalEntry`.

    ### Usage Example
    `Payment` will have a field called `applied-to-lines` which will be an array of `PaymentLineItemSerializer` objects that can either be a `Invoice`, `CreditNote`, or `JournalEntry`.
    """

    applied_amount: typing.Optional[str] = pydantic.Field(description="The amount of the PaymentLineItem.")
    related_object_type: typing.Optional[PaymentLineItemRequestRelatedObjectType]
    related_object_id: typing.Optional[str] = pydantic.Field(
        description="UUID of the related_object_type associated to this PaymentLineItem."
    )
    applied_date: typing.Optional[dt.datetime] = pydantic.Field(description="Applied date of the PaymentLineItem")
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
