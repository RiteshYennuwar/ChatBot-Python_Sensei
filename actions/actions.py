from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import random
import requests

# class ActionProvideCodeExamples(Action):
#     def name(self) -> Text:
#         return "action_provide_code_examples"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         user_query = next(tracker.get_latest_entity_values('code_type'),None)
#         code_examples = {
#             "dictionaries": "my_dict = {'key': 'value'}",
#             "for loop": "for item in my_list:\n    print(item)",
#             "while loop": "while condition:\n    # do something",
#             "if else": "if condition:\n    # do something\nelse:\n    # do something else",
#             "tuple": "my_tuple = (1, 2, 3)",
#             "list": "my_list = [1, 2, 3]",
#         }

#         tz_string = code_examples.get(user_query, None)
#         dispatcher.utter_message(tz_string)
#         if not tz_string:
#             msg = f"is {user_query} spelled correctly?"
#             dispatcher.utter_message(text=msg)

#         # for i in code_examples:
#         #     if (i == user_query):
#         #         dispatcher.utter_message(code_examples[i])

        
#         #     else:
#         #         dispatcher.utter_message(i)
#         #         dispatcher.utter_message("fuck off!")
#         # dispatcher.utter_message(user_query)

#         return []

# class ActionExplainCode(Action):
#     def name(self) -> Text:
#         return "action_explain_code"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Replace this with your code logic to explain code
#         dispatcher.utter_message(text="Sure! Here's an explanation for the code snippet.")
#         return []

class ActionExplainConcept(Action):
    def name(self) -> Text:
        return "action_explain_concept"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_concept = next(tracker.get_latest_entity_values('code_type'),None)
        with open('../data/python_concepts.JSON', 'r') as file:
            concepts_data = json.load(file)
        try:
            relevant_info = None
            for concept in concepts_data:
                if concept['name'].lower() == user_concept.lower() or user_concept.lower() in [alias.lower() for alias in concept.get('alias', [])]:
                    relevant_info = concept
                    break
                elif 'subconcepts' in concept:
                    for subconcept in concept['subconcepts']:
                        if subconcept['name'].lower() == user_concept.lower() or user_concept.lower() in [alias.lower() for alias in subconcept.get('alias', [])]:
                            relevant_info = subconcept
                            break
                        
            if relevant_info and 'subconcepts' in relevant_info and 'description' in relevant_info and 'examples' in relevant_info:
                subconcepts = relevant_info['subconcepts']
                buttons = [{"title": subconcept['name'], "payload": f"/provide_example{{\"concept\":\"{subconcept['name']}\"}}"} for subconcept in subconcepts]
                response = f"Sure! Here are some subconcepts of {user_concept}:\n"
                description = relevant_info['description']
                random_example = random.choice(relevant_info['examples'])
                response = f"\n{description}\n\nHere's an example of {user_concept}:\n{random_example}"
                dispatcher.utter_message(text=response, buttons=buttons)

            elif relevant_info and 'subconcepts' in relevant_info and 'description' in relevant_info:
                subconcepts = relevant_info['subconcepts']
                buttons = [{"title": subconcept['name'], "payload": f"/provide_example{{\"concept\":\"{subconcept['name']}\"}}"} for subconcept in subconcepts]
                response = f"Sure! Here are some subconcepts of {user_concept}:\n"
                description = relevant_info['description']
                response = f"\n{description}"    
                dispatcher.utter_message(text=response, buttons=buttons)

            elif relevant_info and 'description' in relevant_info and 'examples' in relevant_info:
                description = relevant_info['description']
                random_example = random.choice(relevant_info['examples'])
                response = f"{description}\n\nHere's an example of {user_concept}:\n{random_example}"
                dispatcher.utter_message(text=response)

            elif relevant_info and 'description' in relevant_info:
                description = relevant_info['description']
                response = f"{description}"
                dispatcher.utter_message(text=response)
            else:
                response = "I am sorry! there is no such concept in my database, I am still learning or please check your spelling and try again"
                dispatcher.utter_message(text=response)


        except:
            dispatcher.utter_message('Sorry! Something went wrong while fetching data, please try again.')
        return []


class ActionProvideErrorAssistance(Action):
    def name(self) -> Text:
        return "action_provide_error_assistance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Replace this with your code logic to provide error assistance

        query = tracker.latest_message.get("text")  # Get the user's query
        try:
            if query:
                api_url = f"https://api.stackexchange.com/2.3/search?order=desc&sort=activity&tagged=python&intitle={query}&site=stackoverflow"

                response = requests.get(api_url)
                data = response.json()

                if response.status_code == 200:
                    results = data.get("items", [])[:3]  # Get the top 3 results

                    if results:
                        for idx, result in enumerate(results, start=1):
                            title = result.get("title", "N/A")
                            link = result.get("link", "")

                            # Retrieve the answer for the question
                            answer_api_url = f"https://api.stackexchange.com/2.3/questions/{result['question_id']}/answers?order=desc&sort=activity&site=stackoverflow&filter=!nNPvSNdWme"
                            answer_response = requests.get(answer_api_url)
                            answer_data = answer_response.json()
                            answers = answer_data.get("items", [])

                            if answers:
                                answer_body = answers[-1].get("body", "No answer available.")
                            else:
                                answer_body = "No answer available."

                            response_message = f"**Result {idx}**:\nTitle: {title}\nLink: {link}\n\nAnswer:\n{answer_body}"
                            dispatcher.utter_message(response_message)
                    else:
                        dispatcher.utter_message("No results found on Stack Overflow.")
                else:
                    dispatcher.utter_message("Sorry, I couldn't fetch Stack Overflow data at the moment.PLease check your network conncetivity.")
            else:
                dispatcher.utter_message("I didn't understand your query.Can you rephrase it.")
        except:
            dispatcher.utter_message("Sorry! Something went wrong while fetching data, please try again.")   
        return []



# class ActionProvideUpdatingSteps(Action):
#     def name(self) -> Text:
#         return "action_provide_updating_steps"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Replace this with your code logic to provide updating steps
#         dispatcher.utter_message(text="Here are the steps to update Python or Pip.")
#         return []

# class ActionUtterGoodbye(Action):
#     def name(self) -> Text:
#         return "utter_goodbye"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_goodbye")
#         return []

# Add more actions as needed for other parts of your domain
