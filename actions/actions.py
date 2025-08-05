from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, ActiveLoop

class ActionShowMainMenu(Action):
    def name(self) -> Text:
        return "action_show_main_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_input = tracker.latest_message.get('text').lower()
        print(f"user chose: {user_input}")

        if any(keyword in user_input for keyword in ["/show_menu", "menu"]):
            text = (
                "How may I help you?\n"
				"📲 Type the Option number to proceed\n"
				"📲 Type Exit anytime to leave the chat\n"
				"1. CARD SERVICES 💸\n"
				"2. EFTS 💰\n"
				"3. CREDIT 💰\n"
				"4. BILL MUSTER 💰\n"
				"5. INTERNET BANKING 💰\n"
				"6. GENERAL BANKING 💰\n"
				"7. MOBILE BANKING 💸\n"
				"8. ZANACO XPRESS 💰\n"
				"9. EXIT 💰\n"
            )
        else:
            text = (
				"How may I help you?\n"
				"📲 Type the Option number to proceed\n"
				"📲 Type Exit anytime to leave the chat\n"
				"1. CARD SERVICES 💸\n"
				"2. EFTS 💰\n"
				"3. CREDIT 💰\n"
				"4. BILL MUSTER 💰\n"
				"5. INTERNET BANKING 💰\n"
				"6. GENERAL BANKING 💰\n"
				"7. MOBILE BANKING 💸\n"
				"8. ZANACO XPRESS 💰\n"
				"9. EXIT 💰\n"
            )
        dispatcher.utter_message(text=text)

        return [SlotSet("menu_level", "faqs")]
    
class ActionHandleOption(Action):
    def name(self) -> Text:
        return "action_handle_option"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        menu_level = tracker.get_slot('menu_level')
        user_input = tracker.latest_message.get('text').strip()
        
        print(f"Option number : {user_input}")
        print(f"Menu level : {menu_level}")

        # ✅ FAQ Categories: Set slot & show submenu
        if menu_level == "faqs":
            menu_map = {
                "1": ("utter_card_services_menu", "cards"),
                "2": ("utter_efts_menu", "efts"),
                "3": ("utter_credit_menu", "credit"),
                "4": ("utter_bill_muster_menu", "bill_muster"),
                "5": ("utter_internet_banking_menu", "internet_banking"),
                "6": ("utter_general_banking_menu", "general"),
                "7": ("utter_mobile_banking_menu", "mobile_banking"),
                "8": ("utter_zanaco_xpress_menu", "zanaco_xpress"),
                "9": ("utter_exit", "exit")
            }

            if user_input in menu_map:
                utterance, slot_value = menu_map[user_input]
                dispatcher.utter_message(response=utterance)
                return [SlotSet("menu_level", slot_value)]
            else:
                dispatcher.utter_message(response="utter_invalid_option")
                return []

        # ✅ CARD Submenu (menu_level = "cards")
        elif menu_level == "cards":
            if user_input.isdigit():
                question_number = int(user_input)
                
                if question_number in (9, 12, 15):
                    # Activate the new form
                    utter_name = f"utter_card_q{question_number}"
                    print(f"Utterenace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    return [ActiveLoop("customer_info_form")]
                
                if 1 <= question_number <= 20:
                    utter_name = f"utter_card_q{question_number}"
                    print(f"Utterenace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    # print(f"Response : {dispatcher.utter_message(response=utter_name)}")
                    # [SlotSet("menu_level", "faqs")]
                    print(f"menu_level : {menu_level}")
                    dispatcher.utter_message(
                            text="Did I answer your queries?",
                            buttons=[
                                        {"title": "Yes", "payload": "/affirm"},
                                        {"title": "No", "payload": "/deny"}
                                    ]
                                )
                    return [SlotSet("menu_level", "None")]
                else:
                    dispatcher.utter_message(response="utter_invalid_option")
            else:
                dispatcher.utter_message(response="utter_invalid_option")
            return []

        # ✅ efts Faq Menu
        elif menu_level == "efts":
            if user_input.isdigit():
                question_number = int(user_input)
                
                if question_number == 8:
                    # Activate the new form
                    utter_name = f"utter_efts_q{question_number}"
                    print(f"Utterenace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    return [ActiveLoop("customer_info_form")]
                
                if 1 <= question_number <= 14:
                    utter_name = f"utter_efts_q{question_number}"
                    print(f"Utterance number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    # print(f"Response : {dispatcher.utter_message(response=utter_name)}")
                    dispatcher.utter_message(
                            text="Did I answer your queries?",
                            buttons=[
                                        {"title": "Yes", "payload": "/affirm"},
                                        {"title": "No", "payload": "/deny"}
                                    ]
                                )
                else:
                    dispatcher.utter_message(response="utter_invalid_option")
            else:
                dispatcher.utter_message(response="utter_invalid_option")
            return []

        # ✅ National ID Menu
        elif menu_level == "credit":
            if user_input.isdigit():
                question_number = int(user_input)
                
                if question_number in (15, 16, 21):
                    # Activate the new form
                    utter_name = f"utter_credit_q{question_number}"
                    print(f"Utterenace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    return [ActiveLoop("customer_info_form")]
                
                if 1 <= question_number <= 29:
                    utter_name = f"utter_credit_q{question_number}"
                    print(f"Utternace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    # print(f"Response : {dispatcher.utter_message(response=utter_name)}")
                    dispatcher.utter_message(
                            text="Did I answer your queries?",
                            buttons=[
                                        {"title": "Yes", "payload": "/affirm"},
                                        {"title": "No", "payload": "/deny"}
                                    ]
                                )
                else:   
                    dispatcher.utter_message(response="utter_invalid_option")
            else:
                dispatcher.utter_message(response="utter_invalid_option")
            return []

        # ✅ Kiosk Menu
        elif menu_level == "bill_muster":
            if user_input.isdigit():
                question_number = int(user_input)
                if question_number in (1, 2, 3, 4, 5, 6, 7):
                    # Activate the new form
                    utter_name = f"utter_bill_muster_q{question_number}"
                    print(f"Utterenace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    return [ActiveLoop("customer_info_form")]
                else:   
                    dispatcher.utter_message(response="utter_invalid_option")
            else:
                dispatcher.utter_message(response="utter_invalid_option")
            return []

        elif menu_level == "internet_banking":
            if user_input.isdigit():
                question_number = int(user_input)
                
                if question_number in (6, 7, 8, 9, 11):
                    # Activate the new form
                    utter_name = f"utter_internet_banking_q{question_number}"
                    print(f"Utterenace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    return [ActiveLoop("customer_info_form")]
                
                if 1 <= question_number <= 11:
                    utter_name = f"utter_internet_banking_q{question_number}"
                    print(f"Utternace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    # print(f"Response : {dispatcher.utter_message(response=utter_name)}")
                    dispatcher.utter_message(
                            text="Did I answer your queries?",
                            buttons=[
                                        {"title": "Yes", "payload": "/affirm"},
                                        {"title": "No", "payload": "/deny"}
                                    ]
                                )
                else:   
                    dispatcher.utter_message(response="utter_invalid_option")
            else:
                dispatcher.utter_message(response="utter_invalid_option")
            return []
        
        elif menu_level == "general":
            if user_input.isdigit():
                question_number = int(user_input)
                
                if question_number in (33, 34, 36):
                    # Activate the new form
                    utter_name = f"utter_general_q{question_number}"
                    print(f"Utterenace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    return [ActiveLoop("customer_info_form")]
                
                if 1 <= question_number <= 36:
                    utter_name = f"utter_general_q{question_number}"
                    print(f"Utternace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    # print(f"Response : {dispatcher.utter_message(response=utter_name)}")
                    dispatcher.utter_message(
                            text="Did I answer your queries?",
                            buttons=[
                                        {"title": "Yes", "payload": "/affirm"},
                                        {"title": "No", "payload": "/deny"}
                                    ]
                                )
                else:   
                    dispatcher.utter_message(response="utter_invalid_option")
            else:
                dispatcher.utter_message(response="utter_invalid_option")
            return []
        
        elif menu_level == "mobile_banking":
            if user_input.isdigit():
                question_number = int(user_input)
                
                if question_number in (3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16, 17, 18):
                    # Activate the new form
                    utter_name = f"utter_mobile_banking_q{question_number}"
                    print(f"Utterenace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    return [ActiveLoop("customer_info_form")]
                
                if 1 <= question_number <= 19:
                    utter_name = f"utter_mobile_banking_q{question_number}"
                    print(f"Utternace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    # print(f"Response : {dispatcher.utter_message(response=utter_name)}")
                    dispatcher.utter_message(
                            text="Did I answer your queries?",
                            buttons=[
                                        {"title": "Yes", "payload": "/affirm"},
                                        {"title": "No", "payload": "/deny"}
                                    ]
                                )
                else:   
                    dispatcher.utter_message(response="utter_invalid_option")
            else:
                dispatcher.utter_message(response="utter_invalid_option")
            return []
        
        elif menu_level == "zanaco_xpress":
            if user_input.isdigit():
                question_number = int(user_input)
                
                if 1 <= question_number <= 14 or 15 <= question_number <= 17:
                    # Activate the new form
                    utter_name = f"utter_zanaco_xpress_{question_number}"
                    print(f"Utterenace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    return [ActiveLoop("customer_info_form")]
                
                if 1 <= question_number <= 19:
                    utter_name = f"utter_zanaco_xpress_{question_number}"
                    print(f"Utternace Number : {utter_name}")
                    dispatcher.utter_message(response=utter_name)
                    # print(f"Response : {dispatcher.utter_message(response=utter_name)}")
                    dispatcher.utter_message(
                            text="Did I answer your queries?",
                            buttons=[
                                        {"title": "Yes", "payload": "/affirm"},
                                        {"title": "No", "payload": "/deny"}
                                    ]
                                )
                else:   
                    dispatcher.utter_message(response="utter_invalid_option")
            else:
                dispatcher.utter_message(response="utter_invalid_option")
            return []
        # 🔴 Unknown menu_level
        else:
            dispatcher.utter_message(text="Menu state unknown. Please type 'hi' to start over.")
            return []


class ActionHandleAffirm(Action):
    def name(self) -> Text:
        return "action_handle_affirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Thank you very much for contacting us! If you need further assistance, please get in touch. We are always happy to help.")

        dispatcher.utter_message(
            text="If you have time, can you rate me as a customer associate to you?",
            buttons=[
                {"title": "1 - Unhappy", "payload": "/give_rating{\"rating\": 1}"},
                {"title": "2 - Not Very Happy", "payload": "/give_rating{\"rating\": 2}"},
                {"title": "3 - Neutral", "payload": "/give_rating{\"rating\": 3}"},
                {"title": "4 - Happy", "payload": "/give_rating{\"rating\": 4}"},
                {"title": "5 - Very Happy", "payload": "/give_rating{\"rating\": 5}"},
            ]
        )
        return []
    
    
# class ActionHandleRating(Action):
#     def name(self) -> Text:
#         return "action_handle_rating"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         rating = tracker.get_slot("rating")
#         if not rating:
#             dispatcher.utter_message(text="Sorry, I didn't catch your rating.")
#             return []

#         if int(rating) >= 4:
#             dispatcher.utter_message(text="Delighted to hear your feedback. Take care and have a wonderful day!")
#             dispatcher.utter_message(text="Thank you for stopping by at Zanaco, we appreciate you, and hope you have a wonderful day.")
#             return []
#         else:
#             dispatcher.utter_message(text="Please tell us the places we can improve upon so that we can serve you better next time.")
#             return [SlotSet("request_feedback", True)]  # optional: to handle a form
        
class ActionHandleRating(Action):
    def name(self) -> Text:
        return "action_handle_rating"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        rating = tracker.get_slot("rating")

        if not rating:
            dispatcher.utter_message(text="Sorry, I didn't catch your rating.")
            return []

        if int(rating) >= 4:
            dispatcher.utter_message(text="Delighted to hear your feedback. Take care and have a wonderful day!")
            dispatcher.utter_message(text="Thank you for stopping by at Zanaco, we appreciate you, and hope you have a wonderful day.")
            return []
        else:
            dispatcher.utter_message(text="Please tell us the places we can improve upon so that we can serve you better next time.")
            return [
                SlotSet("request_feedback", True),
                ActiveLoop("feedback_form")
            ]
        
class SubmitFeedbackForm(Action):
    def name(self) -> Text:
        return "submit_feedback_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        feedback = tracker.get_slot("user_feedback")

        dispatcher.utter_message(text="We are extremely sorry to hear that, and we take these issues very seriously. We assure you that we will improve your experience.")
        dispatcher.utter_message(text="We will keep this in mind, thank you for your feedback!")
        
        dispatcher.utter_message(
            text="Select Main Menu",
            buttons=[
                {"title": "Main Menu", "payload": "/FAQs"}
            ]
        )

        return [SlotSet("request_feedback", None)]
    
class SubmitCustomerInfoForm(Action):
    def name(self) -> str:
        return "submit_customer_info_form"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
    ) -> List[Dict[str, Any]]:

        # You could extract info like this if needed
        # user_input = tracker.get_slot("cust_info")

        # Respond with confirmation and ticket ID
        dispatcher.utter_message(
            text="Ok. Your information has been submitted successfully. Your service request number is 1753962591"
        )

        # Follow-up prompt
        dispatcher.utter_message(
            text="Did I answer your queries?",
            buttons=[
                {"title": "Yes", "payload": "/affirm"},
                {"title": "No", "payload": "/deny"}
            ]
        )

        return []


class ActionAskName(Action):
    def name(self) -> Text:
        return "action_ask_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(template="utter_ask_name")
        return []

# class ActionSaveName(Action):
#     def name(self) -> str:
#         return "action_save_name"

#     def run(self, dispatcher, tracker, domain):
#         # Get the user's latest input
#         user_name = tracker.latest_message.get("text")

#         # Validate if the input is empty or invalid (optional)
#         if not user_name or user_name.lower() in ["hi", "hello", "hey"]:
#             dispatcher.utter_message(text="That doesn't seem like a name. Could you please tell me your name?")
#             return []

#         # Acknowledge the name and save it in the slot
#         dispatcher.utter_message(text=f"{user_name}, Please Choose a Category")
#         return [SlotSet("name", user_name)]
    
class ActionDeactivateForm(Action):
    def name(self) -> str:
        return "action_deactivate_form"

    def run(self,
            dispatcher,
            tracker,
            domain) -> List[Dict[str, Any]]:

        return [
            ActionDeactivateForm(),
            SlotSet("name", None)
        ]
        
# class ActionDefaultFallback(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(text="Sorry, I didn’t understand that. Please choose an option from the menu.")
#         return []
    
class ActionSetMenuLevelFaqs(Action):
    def name(self) -> Text:
        return "action_set_menu_level_faqs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Menu level set to FAQs.")
        return [SlotSet("menu_level", "faqs")]
    
class ActionEnterName(Action):
    def name(self) -> str:
        return "action_enter_name"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        # dispatcher.utter_message(response="utter_ask_name")
        return [ActiveLoop("name_form")]
    
class ActionResetCustInfo(Action):
    def name(self) -> str:
        return "action_reset_cust_info"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        # dispatcher.utter_message(text="Customer info has been cleared.")
        return [SlotSet("cust_info", None)]
