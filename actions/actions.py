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
class ActionHelloWorld(Action):

    def name(self) -> Text:
         return "action_explain_code"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response=domain["responses"]["utter_ask_code_explanation"]
        dispatcher.utter_message(response[0]["text"])

        return []
   
    def name(self) -> Text:
          return "action_provide_updating_steps"
     
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response=domain["responses"]["utter_ask_how_to_update"]
        dispatcher.utter_message(response[0]["text"])
        dispatcher.utter_attachment("https://www.pythoncentral.io/how-to-update-python/")
     
        
        return []



    def name(self) -> Text:
        return "action_provide_code_examples"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        code_type = tracker.get_slot("code_type")  
        
        
        code_examples = {
            "dictionaries": "my_dict = {'key': 'value'}",
            "for loop": "for item in my_list:\n    print(item)",
            "while loop": "while condition:\n    # do something",
            "if else": "if condition:\n    # do something\nelse:\n    # do something else",
            "tuple": "my_tuple = (1, 2, 3)",
            "list": "my_list = [1, 2, 3]",
        }

        if code_type in code_examples:
            example_code = code_examples[code_type]
            response = f"Sure! Here's an example of {code_type} in Python:\n\n{example_code}"
        else:
            response = "I'm sorry, I don't have an example for that code type."

        dispatcher.utter_message(text=response)
        return []

   
   

