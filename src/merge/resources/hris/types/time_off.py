# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .remote_data import RemoteData
from .time_off_approver import TimeOffApprover
from .time_off_employee import TimeOffEmployee
from .time_off_request_type import TimeOffRequestType
from .time_off_status import TimeOffStatus
from .time_off_units import TimeOffUnits


class TimeOff(pydantic.BaseModel):
    """
    # The TimeOff Object
    ### Description
    The `TimeOff` object is used to represent all employees' Time Off entries.

    ### Usage Example
    Fetch from the `LIST TimeOffs` endpoint and filter by `ID` to show all time off requests.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    employee: typing.Optional[TimeOffEmployee] = pydantic.Field(description="The employee requesting time off.")
    approver: typing.Optional[TimeOffApprover] = pydantic.Field(
        description="The Merge ID of the employee with the ability to approve the time off request."
    )
    status: typing.Optional[TimeOffStatus] = pydantic.Field(
        description=(
            "The status of this time off request.\n"
            "\n"
            "* `REQUESTED` - REQUESTED\n"
            "* `APPROVED` - APPROVED\n"
            "* `DECLINED` - DECLINED\n"
            "* `CANCELLED` - CANCELLED\n"
            "* `DELETED` - DELETED\n"
        )
    )
    employee_note: typing.Optional[str] = pydantic.Field(description="The employee note for this time off request.")
    units: typing.Optional[TimeOffUnits] = pydantic.Field(
        description=(
            "The measurement that the third-party integration uses to count time requested.\n"
            "\n"
            "* `HOURS` - HOURS\n"
            "* `DAYS` - DAYS\n"
        )
    )
    amount: typing.Optional[float] = pydantic.Field(
        description="The time off quantity measured by the prescribed “units”."
    )
    request_type: typing.Optional[TimeOffRequestType] = pydantic.Field(
        description=(
            "The type of time off request.\n"
            "\n"
            "* `VACATION` - VACATION\n"
            "* `SICK` - SICK\n"
            "* `PERSONAL` - PERSONAL\n"
            "* `JURY_DUTY` - JURY_DUTY\n"
            "* `VOLUNTEER` - VOLUNTEER\n"
            "* `BEREAVEMENT` - BEREAVEMENT\n"
        )
    )
    start_time: typing.Optional[dt.datetime] = pydantic.Field(
        description="The day and time of the start of the time requested off."
    )
    end_time: typing.Optional[dt.datetime] = pydantic.Field(
        description="The day and time of the end of the time requested off."
    )
    remote_was_deleted: typing.Optional[bool]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
