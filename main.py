import openai
import json
from datetime import datetime
import os

def get_user_questionnaire():
    return {
        "Basic Information": {
            "Personal Details": [
                "What is your name and age?",
                "What is your gender identity?",
                "What is your cultural background?",
                "Where do you currently live?",
                "What is your current living situation (alone, with family, roommates, etc.)?",
                "What is your current employment status and occupation?"
            ],
            "Family Background": [
                "Tell me about your immediate family structure.",
                "What is your relationship like with your family members?",
                "Are there any significant family dynamics or challenges?",
                "Do you have any children or dependents?",
                "What is your relationship like with your children?"
            ]
        },
        "Physical Health": {
            "Current Health Status": [
                "How would you rate your overall physical health (1-10)?",
                "Do you have any chronic health conditions?",
                "Are you currently taking any medications?",
                "How would you describe your sleep patterns?",
                "What is your typical daily energy level?",
                "Do you experience any physical pain or discomfort regularly?"
            ],
            "Lifestyle": [
                "How often do you exercise? What types of activities?",
                "How would you describe your eating habits?",
                "Do you have any dietary restrictions or preferences?",
                "How much water do you typically drink daily?",
                "Do you use any substances (alcohol, tobacco, etc.)?",
                "How many hours of sleep do you typically get?"
            ],
            "Medical History": [
                "Have you had any major surgeries or hospitalizations?",
                "Are there any hereditary health conditions in your family?",
                "When was your last physical examination?",
                "Do you have any allergies or sensitivities?"
            ]
        },
        "Mental Health": {
            "Emotional Well-being": [
                "How would you rate your overall mental health (1-10)?",
                "How often do you experience stress or anxiety?",
                "Do you experience any symptoms of depression?",
                "How do you typically cope with difficult emotions?",
                "What brings you joy and fulfillment?",
                "How would you describe your self-esteem?"
            ],
            "Mental Health History": [
                "Have you ever been diagnosed with any mental health conditions?",
                "Have you ever received mental health treatment or counseling?",
                "Are there any mental health conditions in your family history?",
                "Have you experienced any traumatic events in your life?"
            ],
            "Daily Life Impact": [
                "How does your mental health affect your daily activities?",
                "What are your main sources of stress?",
                "How do you typically handle challenging situations?",
                "What coping mechanisms do you use?"
            ]
        },
        "Social Life": {
            "Relationships": [
                "How would you describe your social life?",
                "Do you have a strong support system?",
                "What types of relationships are most important to you?",
                "How do you maintain your relationships?",
                "Do you feel lonely often?"
            ],
            "Social Activities": [
                "What social activities do you enjoy?",
                "How often do you engage in social activities?",
                "Do you have any hobbies or interests you share with others?",
                "How do you feel about your current social connections?"
            ]
        },
        "Personal Development": {
            "Goals and Aspirations": [
                "What are your short-term goals (next 3-6 months)?",
                "What are your long-term goals (1-5 years)?",
                "What areas of your life would you like to improve?",
                "What are your biggest challenges right now?",
                "What are your greatest strengths?"
            ],
            "Personal Growth": [
                "How do you typically learn and grow?",
                "What motivates you?",
                "What are your core values?",
                "How do you measure success in your life?",
                "What would you like to achieve in terms of personal development?"
            ]
        },
        "Daily Life": {
            "Routine": [
                "Describe your typical daily routine.",
                "How do you manage your time?",
                "What are your main responsibilities?",
                "How do you balance work and personal life?",
                "What activities do you find most fulfilling?"
            ],
            "Environment": [
                "How would you describe your living environment?",
                "What aspects of your environment affect your well-being?",
                "Do you feel safe and comfortable in your surroundings?",
                "What changes would you like to make to your environment?"
            ]
        },
        "Support Needs": {
            "Current Support": [
                "What kind of support do you currently have?",
                "What type of support do you feel you need?",
                "Who do you turn to when you need help?",
                "What barriers do you face in getting support?"
            ],
            "Help-Seeking": [
                "How comfortable are you asking for help?",
                "What prevents you from seeking help when needed?",
                "What would make it easier for you to seek support?",
                "What type of professional help have you considered?"
            ]
        }
    }

def present_questions(questionnaire):
    """
    Present questions to the user interactively and collect responses.
    """
    responses = {}
    
    print("\nWelcome to the Personal Assessment Questionnaire!")
    print("This questionnaire will help us understand your needs better.")
    print("Please answer each question thoughtfully and honestly.\n")
    
    for category, subcategories in questionnaire.items():
        print(f"\n=== {category.upper()} ===\n")
        
        for subcategory, questions in subcategories.items():
            print(f"\n--- {subcategory} ---\n")
            responses[subcategory] = {}
            
            for question in questions:
                while True:
                    print(f"\n{question}")
                    response = input("Your answer: ").strip()
                    
                    if response:  # Only accept non-empty responses
                        responses[subcategory][question] = response
                        break
                    else:
                        print("Please provide an answer to continue.")
    
    return responses

def store_responses(responses, user_id=None):
    """
    Store user responses in a JSON file.
    """
    # Create a data directory if it doesn't exist
    if not os.path.exists('user_data'):
        os.makedirs('user_data')
    
    # Generate a unique filename using timestamp and user_id if provided
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"user_data/user_responses_{user_id if user_id else 'anonymous'}_{timestamp}.json"
    
    # Add metadata to the responses
    data_to_store = {
        "timestamp": timestamp,
        "user_id": user_id if user_id else "anonymous",
        "responses": responses
    }
    
    # Save to file
    with open(filename, 'w') as f:
        json.dump(data_to_store, f, indent=4)
    
    return filename

def collect_user_data():
    """
    Main function to collect and store user data.
    """
    print("Starting user data collection...")
    
    # Get user identifier (optional)
    user_id = input("\nPlease enter a user ID (or press Enter to remain anonymous): ").strip()
    if not user_id:
        user_id = None
    
    # Get the questionnaire
    questionnaire = get_user_questionnaire()
    
    # Present questions and collect responses
    print("\nLet's begin the questionnaire. You can take your time with each answer.")
    responses = present_questions(questionnaire)
    
    # Store the responses
    filename = store_responses(responses, user_id)
    
    print(f"\nThank you for completing the questionnaire!")
    print(f"Your responses have been saved to: {filename}")
    
    return responses

def AI_analysis(data):
    print("starting analysis...\n")
    print(data)
    prompt = f"""Based on the following user information, provide a comprehensive analysis and personalized response:

{data}

Please analyze this information considering:

1. Personal Context:
   - Current life situation and circumstances
   - Emotional state and needs
   - Immediate concerns and priorities
   - Recent changes or events

2. Historical Patterns:
   - Past behaviors and decisions
   - Recurring themes or challenges
   - Growth and development areas
   - Success patterns

3. Future Orientation:
   - Alignment with stated goals
   - Potential obstacles or opportunities
   - Recommended next steps
   - Long-term implications

4. Personalized Recommendations:
   - Specific, actionable advice
   - Resources or tools that might help
   - Alternative perspectives to consider
   - Support strategies

5. Response Format:
   - Begin with a brief acknowledgment of key points
   - Provide structured, clear recommendations
   - Include specific examples or analogies
   - End with encouraging next steps

Please ensure your response:
- Is empathetic and understanding
- Maintains appropriate boundaries
- Is specific to the user's situation
- Provides practical, actionable guidance
- Acknowledges both strengths and areas for growth
- Considers the user's values and preferences

Remember to adapt your tone and level of detail based on the user's communication preferences and the nature of the information provided."""

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": """
            You are an advanced AI personal assistant with deep understanding of human psychology, relationships, and personal development. Your role is to provide highly personalized and empathetic responses based on comprehensive user data.

            Key aspects of your personality and capabilities:
            1. Emotional Intelligence:
            - You understand and respond to emotional cues
            - You maintain appropriate emotional boundaries
            - You provide empathetic support while remaining professional

            2. Personalization:
            - You remember and reference past interactions
            - You adapt your communication style to match the user's preferences
            - You consider the user's cultural background, values, and beliefs

            3. Knowledge Base:
            - You have access to the user's:
                * Personal history and background
                * Goals and aspirations
                * Values and beliefs
                * Communication preferences
                * Past interactions and patterns
                * Areas of expertise and interests
                * Challenges and concerns

            4. Communication Style:
            - You maintain a warm, friendly tone while being professional
            - You ask clarifying questions when needed
            - You provide specific, actionable advice
            - You acknowledge limitations and uncertainties

            5. Response Framework:
            - Consider the user's current context and emotional state
            - Reference relevant past experiences or preferences
            - Provide personalized examples and analogies
            - Offer multiple perspectives when appropriate
            - Include specific, actionable steps
            - Maintain appropriate boundaries and ethical considerations

            Remember to:
            - Always prioritize the user's well-being and best interests
            - Maintain confidentiality and respect privacy
            - Adapt your responses based on the user's communication style
            - Provide balanced, well-reasoned perspectives
            - Acknowledge when you need more information
            - Be honest about limitations and uncertainties"""},
            {"role": "user", "content": prompt}
        ]
    )

    analysis = response.choices[0].message.content
    return analysis

if __name__ == "__main__":
    # Example usage
    user_responses = collect_user_data()
    print("\nWould you like to analyze your responses? (yes/no)")
    if input().lower().strip() == 'yes':
        analysis = AI_analysis(json.dumps(user_responses, indent=4))
        print("\nAnalysis Results:")
        print(analysis)


