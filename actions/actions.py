from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from bs4 import BeautifulSoup

class ActionProvideCodeExamples(Action):
    def name(self) -> Text:
        return "action_provide_code_examples"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Replace this with your code logic to provide code examples
        try:
            # Get the user's query from the tracker
            user_query = tracker.latest_message.get('text')

            # Search the Python documentation
            search_url = f"https://docs.python.org/3/search.html?q={user_query}"
            response = requests.get(search_url)
            response.raise_for_status()

            # Parse the search results page using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the first search result's title and URL
            first_result = soup.find('dt', class_='search-results')
            if first_result:
                result_title = first_result.find('a').text
                result_url = first_result.find('a')['href']
                full_url = f"https://docs.python.org/3/{result_url}"

                # Send the response back to the user
                dispatcher.utter_message(text=f"I found a relevant Python documentation page: {result_title}\nYou can read more about it here: {full_url}")
            else:
                dispatcher.utter_message(text="I couldn't find any relevant information in the Python documentation.")
        except Exception as e:
            dispatcher.utter_message(text="An error occurred while searching the Python documentation.")

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

