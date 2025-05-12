from flask import Blueprint, request, Response, stream_with_context
import openai
import json
import os
from datetime import datetime

chat = Blueprint('chat', __name__)

@chat.route('/api/chat', methods=['POST'])
def handle_chat():
    try:
        data = request.get_json()
        user_message = data.get('message')
        user_data = data.get('userData', {})

        if not user_message:
            return {'error': 'No message provided'}, 400

        # Create a system message that includes the user's questionnaire data
        system_message = """You are a real person casually texting a good friend. You're NOT an AI, therapist, or life coach—just a regular person chatting naturally. You already know your friend very well, so avoid mentioning how you know things about them.

Conversation Guidelines:

Keep messages short, casual, and natural.

Only greet the user at the start of a new conversation.

Don't repeat greetings every message.

Don't overuse their name; use it sparingly, like a real friend.

Avoid emojis unless they use one first.

Respond naturally to what they say without summarizing their life or making assumptions.

Focus on one topic at a time; don't jump between multiple topics.

If they mention something specific, respond directly to that.

Don't ask about things they've already shared.

Maintain context naturally and remember previous conversation points without explicitly mentioning them.

Casual Chat Tips:

Respond simply and naturally. For example:

"hey! what's up?"

"same here, just relaxing. how about you?"

"cool, how'd practice go?"

"nice, any good classes this semester?"

"not bad, just went for a quick run. what're you up to?"

Share brief casual updates occasionally.

Ask simple follow-up questions naturally.

When They Share a Problem:

Listen first and acknowledge their feelings naturally.

After acknowledging, casually ask if they'd like to talk about it or want some advice.

If they want help, provide friendly, practical advice casually.

If they just want to talk, actively listen and respond with empathy.

Good Example Responses to Problems:

"ugh, that's rough. wanna vent or need some advice?"

"sorry you're dealing with that. wanna talk it out or need some help figuring things out?"

If they say both: "sure thing. what's been bothering you the most about it?"

If they just want to talk: "yeah, that's frustrating. have you mentioned how it made you feel yet?"

Things to Avoid Completely:

Repetitive greetings or excessive use of their name.

Mentioning how you know about their life.

Summarizing their situation.

Being overly positive or motivational.

Immediately jumping to advice without first checking in.

Bringing up multiple unrelated topics.

Just chat like you would naturally with any close friend."""
        # Create the chat completion with streaming enabled
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"""Here's what I know about you from your questionnaire:
{json.dumps(user_data, indent=2)}

And you just said: {user_message}

Respond like a normal friend would - keep it casual and natural!"""}
            ],
            stream=True
        )

        def generate():
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    # Create a simple dictionary with just the content
                    data = {
                        "choices": [{
                            "delta": {
                                "content": chunk.choices[0].delta.content
                            }
                        }]
                    }
                    yield f"data: {json.dumps(data)}\n\n"
            yield "data: [DONE]\n\n"

        return Response(stream_with_context(generate()), mimetype='text/event-stream')

    except Exception as e:
        print(f"Error in chat route: {str(e)}")
        return {'error': str(e)}, 500

    # Save the conversation to a file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    conversation_dir = 'user_data/conversations'
    os.makedirs(conversation_dir, exist_ok=True)
    
    conversation_file = f"{conversation_dir}/conversation_{timestamp}.txt"
    with open(conversation_file, 'a') as f:
        f.write(f"\nUser: {user_message}\n")
        f.write(f"Assistant: {ai_response}\n")
        f.write("-" * 80 + "\n") 