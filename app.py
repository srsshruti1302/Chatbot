import streamlit as st

st.set_page_config(page_title="Insurance Chatbot", page_icon="🏢")

st.title("🏢 SecureLife Insurance – Virtual Assistant")
st.caption("Helping you with policies, claims & support")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello 👋 Welcome to SecureLife Insurance. How may I help you today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

def get_bot_response(text):
    text = text.lower()

    if "hi" in text or "hello" in text:
        return "Hello 👋 How can I assist you today?"

    elif "buy" in text or "purchase" in text:
        return "Sure. Are you looking for health, life, motor, or home insurance?"

    elif "health" in text:
        return "Great choice 👍 Are you looking for individual coverage or family coverage?"

    elif "family" in text:
        return "Our family health plans cover spouse, children, and parents. Would you like cashless hospitalization?"

    elif "cashless" in text or "yes" in text:
        return "We offer cashless treatment at 10,000+ network hospitals. Do you have any existing medical conditions?"

    elif "no" in text:
        return "That’s good to hear. I recommend our Family Health Plus Plan with coverage up to ₹10 lakhs."

    elif "premium" in text or "cost" in text:
        return "The annual premium starts from ₹18,000 depending on age and family size."

    elif "claim" in text:
        return "To file a claim: Login → Select policy → File claim → Upload documents → Submit."

    elif "documents" in text:
        return "Required documents include policy number, hospital bills, discharge summary, prescription, and ID proof."

    elif "settlement" in text or "time" in text:
        return "Claim settlement usually takes 7–14 working days after verification."

    elif "miss" in text or "grace" in text:
        return "You get a grace period of 15–30 days if you miss a premium payment."

    elif "renew" in text:
        return "You can renew your policy online using UPI, debit/credit card, or net banking."

    elif "human" in text or "agent" in text:
        return "I can connect you with a customer support executive via call or live chat. Would you like a call back?"

    elif "yes" in text:
        return "✅ Request noted. A customer support executive will contact you shortly."

    else:
        return "I’m sorry, I couldn’t understand that. Could you please rephrase your question?"

# Process user input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    bot_reply = get_bot_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.write(bot_reply)
