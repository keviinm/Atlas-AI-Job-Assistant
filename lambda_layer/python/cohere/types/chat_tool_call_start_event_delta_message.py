# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .tool_call_v2 import ToolCallV2
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ChatToolCallStartEventDeltaMessage(UncheckedBaseModel):
    tool_calls: typing.Optional[ToolCallV2] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
