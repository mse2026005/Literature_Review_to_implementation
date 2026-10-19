import google.generativeai as genai
import os
import time

genai.configure(api_key=os.environ.get("AQ.Ab8RN6JPKLP2OJiOGaSYw6MQA"))
model = genai.GenerativeModel('gemini-1.5-pro')

def generate_response(prompt, system_instruction):
    try:
        response = model.generate_content(
            f"Role: {system_instruction}\n\nTask: {prompt}",
            generation_config={"temperature": 0.7}
        )
        time.sleep(4) # Respect free tier rate limits (15 RPM)
        return response.text
    except Exception as e:
        return str(e)

def run_debate(topic, agents, rounds=3):
    history = f"Topic: {topic}\n"
    for r in range(rounds):
        history += f"\n--- Round {r+1} ---\n"
        for agent_name, persona in agents.items():
            prompt = f"Previous discussion:\n{history}\nProvide your critique and updated hypothesis."
            reply = generate_response(prompt, persona)
            history += f"{agent_name}: {reply}\n"
    return history