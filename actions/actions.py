from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from googlesearch import search

class ActionProvideCodeExamples(Action):
    def name(self) -> Text:
        return "action_provide_code_examples"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
        
            user_query = next(tracker.get_latest_entity_values('code_type'),None)
            code_examples = {
                "dictionaries": "my_dict = {'key': 'value'}",
                "for loop": "for item in my_list:\n    print(item)",
                "while loop": "while condition:\n    # do something",
                "if else": "if condition:\n    # do something\nelse:\n    # do something else",
                "tuple": "my_tuple = (1, 2, 3)",
                "list": "my_list = [1, 2, 3]",
            }

            tz_string = code_examples.get(user_query, None)
            dispatcher.utter_message(tz_string)
            if not tz_string:
                msg = f"is {user_query} spelled correctly?"
                dispatcher.utter_message(text=msg)

            # for i in code_examples:
            #     if (i == user_query):
            #         dispatcher.utter_message(code_examples[i])

        
            #     else:
            #         dispatcher.utter_message(i)
            #         dispatcher.utter_message("fuck off!")
            # dispatcher.utter_message(user_query)

        except:
            dispatcher.utter_massage(text="Sorry for the inconvenience, something went wrong! please try again.")

        return []

class ActionExplainCode(Action):
    def name(self) -> Text:
        return "action_explain_code"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Replace this with your code logic to explain code
        dispatcher.utter_message(text="Sure! Here's an explanation for the code snippet.")
        return []

class ActionProvideErrorAssistance(Action):
    def name(self) -> Text:
        return "action_provide_error_assistance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Replace this with your code logic to provide error assistance
        dispatcher.utter_message(text="Here's some assistance for the error message or code snippet.")
        return []

class ActionExplainConcept(Action):
    def name(self) -> Text:
        return "action_explain_concept"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Replace this with your code logic to explain a concept
        dispatcher.utter_message(text="Sure! Here's an explanation for the requested concept.")
        return []

class ActionProvideUpdatingSteps(Action):
    def name(self) -> Text:
        return "action_provide_updating_steps"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            user_query = next(tracker.get_latest_entity_values('update_type'),None)
            update_examples = {
                'pip': 'pip install --upgrade pip',
                'python': 'go to https://www.python.org/downloads/ and download the latest version of python and install it',
                'packages': 'pip install { package_name } --upgrade',
                'package': 'pip install { package_name } --upgrade',
                'libraries': 'pip install { library_name } --U',
                'library': 'pip install { library_name } --U',
                'module': 'pip install { module_name } --U or --upgrade',
                'modules': 'pip install { module_name } --U or --upgrade'
            }

            tz_string = update_examples.get(user_query, None)
            dispatcher.utter_message(tz_string)
            if not tz_string:
                msg = f"is {user_query} spelled correctly?"
                dispatcher.utter_message(text=msg)

        except:
            dispatcher.utter_message(text='Sorry for the inconvenience, something went wrong! please try again.')

        return []

class ActionUtterGoodbye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_goodbye")
        return []

# Add more actions as needed for other parts of your domain
