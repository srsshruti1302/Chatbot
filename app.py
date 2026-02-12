import streamlit as st

st.set_page_config(page_title="Insurance Assistant", page_icon="🏢")

st.title("🏢 Insurance Company Virtual Assistant")
st.caption("Helping you with policies, claims & support")

intents = {
    "policy recommendation": "To recommend the best policy, please tell me if you are looking for life, health, motor, or home insurance.",
    "buy policy": "You can purchase insurance online, via mobile app, or at the nearest branch. ID and address proof are required.",
    "file claim": "To file a claim, login to your account, select your policy, upload documents, and submit the claim.",
    "health claim documents": "Health insurance claims require policy number, hospital bills, discharge summary, and ID proof.",
    "claim settlement time": "Claims are generally settled within 7–14 working days after document verification.",
    "cashless hospitalization": "Cashless treatment is available at network hospitals where the insurer directly settles the bill.",
    "policy status": "You can check policy status online using your policy number or registered mobile number.",
    "missed premium": "You have a grace period of 15–30 days. Failure to pay may lead to policy lapse.",
    "renew policy": "You can renew your policy online using UPI, debit/credit card, or net banking.",
    "human support": "You can connect with a customer support executive via call, live chat, or branch visit."
}

user_input = st.text_input("Ask your question:")

if user_input:
    user_input = user_input.lower()
    response = "I’m sorry, I couldn’t find an exact answer. Please connect with our support team."

    for intent in intents:
        if intent in user_input:
            response = intents[intent]
            break

    st.chat_message("assistant").write(response)
