def get_response(user_input):
    user_input = user_input.lower()

    if "fever" in user_input:
        return "You may have a fever. Stay hydrated and rest. If it persists, consult a doctor."
    
    elif "headache" in user_input:
        return "Headaches can be caused by stress or dehydration. Try resting and drinking water."
    
    elif "cold" in user_input:
        return "For cold, take rest, drink warm fluids, and consider consulting a doctor if severe."
    
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you with your health today?"
    
    else:
        return "I'm not sure about that. Please consult a healthcare professional."
