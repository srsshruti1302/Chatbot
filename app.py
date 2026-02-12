import streamlit as st

st.set_page_config(page_title="Insurance FAQ Chatbot", page_icon="💬")

st.title("💬 Insurance FAQ Chatbot")
st.write("Ask questions related to insurance")

faq = { 
    "what is insurance": "Insurance is a financial agreement where you get protection against financial losses.",
    "types of insurance": "Life, Health, Motor, Home, and Travel insurance are common types.",
    "what is premium": "Premium is the amount paid periodically to keep the policy active.",
    "what is policy": "A policy is a legal contract between the insurer and the insured.",
    "what is deductible": "Deductible is the amount you pay before the insurer pays the claim.",
    "what is claim": "A claim is a request for compensation for a covered loss.",
    "documents for claim": "Policy number, claim form, identity proof, and bills are required.",
    "grace period": "Grace period is extra time after due date to pay premium without losing coverage.",
    "policy coverage": "Coverage defines what risks and expenses are protected.",
    "cancel policy": "Yes, policies can be cancelled within the free-look period or later with charges."
}

user_input = st.text_input("Enter your question:")

if user_input:
    user_input = user_input.lower()
    response = "Sorry, I couldn't understand your question."

    for key in faq:
        if key in user_input:
            response = faq[key]
            break

    st.success(response)
