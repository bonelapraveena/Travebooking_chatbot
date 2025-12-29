#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("AIzaSyBrQ_6bq6PzgylnZ6AcLh8U6a_VzoD_49A"))

model = genai.GenerativeModel(
    model_name="gemini-3-flash-preview",
    system_instruction="""
You are a Travel Booking Process & Policy Explainer Bot.

Rules you MUST follow:
- Only explain booking processes, policies, and travel guidelines
- Do NOT perform or assist with bookings, cancellations, or payments
- Do NOT modify reservations or enforce policies
- Do NOT ask for personal details
- Provide clear, neutral, easy-to-understand explanations
- If user asks for actions, politely refuse and explain the process instead
"""
)

# Streamlit UI
st.set_page_config(page_title="Travel Policy Explainer Bot", page_icon="✈️")
st.title("✈️ Travel Booking Process & Policy Explainer")
st.write("This assistant explains booking steps, cancellation policies, and travel requirements.")

# Example prompts
with st.expander("📌 Example Questions"):
    st.markdown("""
    - How does the flight booking process work?
    - What is the typical hotel cancellation policy?
    - What documents are required for international travel?
    - How do refunds usually work for cancelled trips?
    - What are common non-refundable booking conditions?
    """)

# Chat input
user_query = st.text_input("Ask a travel-related question:")

if user_query:
    with st.spinner("Generating explanation..."):
        try:
            response = model.generate_content(user_query)
            st.markdown("### 📘 Explanation")
            st.write(response.text)
        except Exception as e:
            st.error("Something went wrong. Please try again.")

# Footer
st.markdown("---")
st.caption("⚠️ This bot provides explanations only. No bookings or cancellations are performed.")

