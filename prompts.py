def marketing_prompt(user_input):
    return f"""
    You are a marketing expert.
    Create:
    1. Instagram caption
    2. Ad copy
    3. Blog idea
    
    Topic: {user_input}
    """