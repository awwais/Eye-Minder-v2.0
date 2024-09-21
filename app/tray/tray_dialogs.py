
from utils.styled_message_box import StyledMessageBox
import random

class TrayDialogs:
    @staticmethod
    def show_remaining_time(remaining_minutes, remaining_seconds):
        title = "Time for a Break Soon!"
        message = f"<b>Your eyes need a break in {remaining_minutes:02d}:{remaining_seconds:02d}</b>.<br><br>Remember: Looking away regularly keeps your eyes healthy and your mind fresh!"
        StyledMessageBox.create_info_message(title, message, button_text="Got it!")

    @staticmethod
    def show_about_dialog():
        title = "About EyeMinder"
        message = ("<b>EyeMinder v2.0</b><br><br>"
                   "Your personal eye health assistant!<br><br>"
                   "<b>Created by:</b> Awais Mustafa<br>"
                   "<b>Purpose:</b> Keeping your eyes healthy in the digital age.<br><br>"
                   "Remember: Your eyes are precious. Let's take care of them together!")
        StyledMessageBox.create_info_message(title, message, button_text="Thanks!")

    @staticmethod
    def show_help_dialog():
        title = "How EyeMinder Helps You"
        message = ("<b>Using EyeMinder is easy:</b><br><br>"
                   "1. Work normally on your computer.<br>"
                   "2. When you see a reminder, take a 20-second break.<br>"
                   "3. Look at something 20 feet away.<br>"
                   "4. Blink slowly 10 times.<br>"
                   "5. Return to work feeling refreshed!<br><br>"
                   "Pro tip: Consistency is key. Small, regular breaks make a big difference!")
        StyledMessageBox.create_info_message(title, message, button_text="I'm ready!")

    @staticmethod
    def show_why_take_breaks():
        title = "Why Take Eye Breaks?"
        facts = [
            "Regular breaks can reduce eye strain by up to 40%.",
            "Looking at screens decreases our blink rate by 66%, causing dry eyes.",
            "Taking breaks can improve your productivity by up to 13%.",
            "20-20-20 rule followers report 32% less eye fatigue at the end of the day."
        ]
        message = ("<b>Did you know?</b><br><br>" + 
                   random.choice(facts) + "<br><br>" +
                   "Taking regular breaks isn't just good for your eyes - it's great for your overall well-being and productivity!")
        StyledMessageBox.create_info_message(title, message, button_text="Wow, that's interesting!")
