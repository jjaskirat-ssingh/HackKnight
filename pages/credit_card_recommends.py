import streamlit as st

# Create a list of credit cards
credit_cards = [
  {
    "name": "Chase Sapphire Preferred® Card",
    "annual_fee": 95,
    "rewards_program": "2x points on travel and dining",
    "credit_score_required": 700,
    "spending_habits": ["Travel", "Dining"],
  },
  {
    "name": "Citi® Double Cash Card",
    "annual_fee": 0,
    "rewards_program": "1% cash back on all purchases, 2% cash back on all eligible purchases when you pay your bill in full each month",
    "credit_score_required": 670,
    "spending_habits": ["Gas", "Groceries"],
  },
  {
    "name": "Capital One Venture Rewards® Credit Card",
    "annual_fee": 95,
    "rewards_program": "2x miles on every purchase",
    "credit_score_required": 720,
    "spending_habits": ["Travel", "Shopping"],
  },
  {
    "name": "Chase Freedom Unlimited®",
    "annual_fee": 0,
    "rewards_program": "5% cash back on travel purchased through Chase Ultimate Rewards®, 3% cash back on dining and drugstores, and 1% cash back on all other purchases",
    "credit_score_required": 670,
    "spending_habits": ["Travel", "Dining", "Drugstores"],
  },
  {
    "name": "American Express® Gold Card",
    "annual_fee": 250,
    "rewards_program": "4x points at restaurants worldwide, 4x points on flights booked directly with airlines or on Amex Travel, and 1x points on all other purchases",
    "credit_score_required": 740,
    "spending_habits": ["Travel", "Restaurants"],
  },
  {
    "name": "Discover it® Cash Back",
    "annual_fee": 0,
    "rewards_program": "5% cash back on rotating categories each quarter, 1% cash back on all other purchases",
    "credit_score_required": 670,
    "spending_habits": ["Gas", "Groceries", "Online Shopping"],
  },
]

# Set the title of the app
st.title("Credit Card Recommender")

# Ask the user for their annual income
annual_income = st.number_input("Annual income", min_value=0, max_value=1000000)

# Ask the user for their credit score
credit_score = st.number_input("Credit score", min_value=300, max_value=850)

# Ask the user about their spending habits
spending_habits = st.multiselect("Spending habits", options=["Travel", "Gas", "Groceries", "Shopping"])

# Get the credit card recommendations
recommendations = []
for credit_card in credit_cards:
  if credit_card["credit_score_required"] <= credit_score and set(credit_card["spending_habits"]) & set(spending_habits):
    recommendations.append(credit_card)

# Display the credit card recommendations
if recommendations:
  st.write("Here are the credit card recommendations for you:")
  for recommendation in recommendations:
    st.write(f"* {recommendation['name']}: {recommendation['rewards_program']}")
else:
  st.write("No credit card recommendations found.")
