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