# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RolesEnum(str, enum.Enum):
    """
    * `READ` - READ
    * `WRITE` - WRITE
    * `OWNER` - OWNER
    """

    READ = "READ"
    WRITE = "WRITE"
    OWNER = "OWNER"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        owner: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RolesEnum.READ:
            return read()
        if self is RolesEnum.WRITE:
            return write()
        if self is RolesEnum.OWNER:
            return owner()
