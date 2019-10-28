#!/usr/bin/env python3
"""
This module contains a Snips app that answers questions about your Snips
assistant.
"""

from datetime import datetime
import importlib
from pathlib import Path
import socket
from urllib.error import URLError

import arrow
import psutil

from snipskit.apps import SnipsAppMixin
from snipskit.hermes.apps import HermesSnipsApp
from snipskit.hermes.decorators import intent
from snipskit.services import version
from snipskit.tools import latest_snips_version

# Use the assistant's language.
i18n = importlib.import_module('translations.' + SnipsAppMixin().assistant['language'])
INTENT_TURN_ON = 'zeliha:turn_on'
RESULT_ASSISTANT_NAME = 'einschalten'

class AssistantInformation(HermesSnipsApp):
    """
    This app answers questions about your Snips assistant.
    """

    @intent(i18n.INTENT_TURN_ON)
    def handle_assistant_name(self, hermes, intent_message):
        """Handle the intent AssistantName."""
        name = self.assistant['name']

        result_sentence = i18n.RESULT_ASSISTANT_NAME.format(name)
        hermes.publish_end_session(intent_message.session_id, result_sentence)


if __name__ == "__main__":
    AssistantInformation()
