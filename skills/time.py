import datetime

def get_current_time() -> str:
    """Returns the current time in a conversational format."""
    now = datetime.datetime.now()
    return f"The time is {now.strftime('%I:%M %p')}."

def get_current_date() -> str:
    """Returns today's date."""
    now = datetime.datetime.now()
    return f"Today is {now.strftime('%A, %B %d, %Y')}."
