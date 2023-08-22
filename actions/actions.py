# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionMessage(Action):
    def name(self):
        return "action_Love"
    def run(self,dispatcher,tracker,domain):
        name=tracker.get_slot('name')
        dispatcher.utter_message(f"name is {name}")
        return []