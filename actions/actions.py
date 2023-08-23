from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from googlesearch import search

class ActionProvideCodeExamples(Action):
    def name(self) -> Text:
        return "action_provide_code_examples"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Replace this with your code logic to provide code examples
        try:
            # Get the user's query from the tracker
            user_query = tracker.latest_message.get('text')

            # Perform Google search
            search_results = list(search(user_query, num=1, stop=1, pause=2))  # Fetch the first result

            if search_results:
                first_result_url = search_results[0]
                # Send the response back to the user
                dispatcher.utter_message(text=f"I found a relevant result: {first_result_url}")
            else:
                dispatcher.utter_message(text="I couldn't find any relevant search results.")

        except Exception as e:
            dispatcher.utter_message(text="An error occurred while searching.")

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
        # Replace this with your code logic to provide updating steps
        dispatcher.utter_message(text="Here are the steps to update Python or Pip.")
        return []

class ActionUtterGoodbye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_goodbye")
        return []

# Add more actions as needed for other parts of your domain
