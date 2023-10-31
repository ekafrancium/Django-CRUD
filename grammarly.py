import re

def grammarly(text):
    # Regular expressions for common grammar mistakes (simplified for demonstration)
    mistakes = {
        r'\b(its)\b': 'it\'s',
        r'\b(theyre)\b': 'they\'re',
        r'\b(wont)\b': 'won\'t',
        # Add more rules as needed
    }

    for pattern, correction in mistakes.items():
        text = re.sub(pattern, correction, text, flags=re.IGNORECASE)

    return text

# Example usage
input_text = "Its a common mistake that theyre making. Wont you help?"
corrected_text = grammarly(input_text)
print("Corrected Text:")
print(corrected_text)
