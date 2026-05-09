"""
Simple Controller to use Shaka as a media controller.
"""

from typing import TYPE_CHECKING

from ..config import APP_SHAKA
from .media import BaseMediaPlayer

if TYPE_CHECKING:
    from ..generated.cast_channel_pb2 import CastMessage


class ShakaController(BaseMediaPlayer):
    """Controller to interact with Shaka app namespace."""

    def __init__(self) -> None:
        super().__init__(supporting_app_id=APP_SHAKA)

    def receive_message(self, message: "CastMessage", data: dict) -> bool:
        """Called when a message is received."""
        self._check_shaka_broadcast(data)
        return super().receive_message(message, data)
