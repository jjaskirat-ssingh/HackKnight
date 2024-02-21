# import requests
# from bs4 import BeautifulSoup
# import streamlit as st

# def scrape_news(location):
#   """Scrape financial news from CNBC's finance section based on the user's location."""

#   # Get the URL for the news website
# #   url = "https://www.cnbc.com/worldwide/" + location + "/finance"
#   url = "https://finance.yahoo.com/news/" + location + "/finance"
#   # Make a request to the website
#   response = requests.get(url)

#   # Parse the HTML response
#   soup = BeautifulSoup(response.content, "html.parser")

#   # Find all the news articles
#   articles = soup.find_all("article")

#   # Create a list of news articles
#   news_list = []
#   for article in articles:
#     title = article.find("h2").text
#     link = article.find("a").get("href")

#     # Only include articles that are from the finance section
#     if "finance" in link:
#       news_list.append({"title": title, "link": link})

#   return news_list


# def main():
#   # Get the user's location
#   location = st.text_input("What is your location? ")

#   # Scrape the news articles
#   news_list = scrape_news(location)

#   # Display the news articles
#   st.title("Financial News")
#   for news in news_list:
#     st.write(news["title"])
#     st.write(news["link"])


# if __name__ == "__main__":
#   main()


import streamlit as st
import requests
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK data (run this only once)
# import nltk
# nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Streamlit UI
st.title("Advanced Financial News Analysis")

st.write("Enter a keyword to search for financial news:")

# Input field
keyword = st.text_input("Enter a keyword", "")

if st.button("Search"):
    if keyword:
        # API key from newsapi.org
        api_key = "50af0a3ae65f414a92581c2dcb41d37f"
        
        # API endpoint and parameters
        url = f"https://newsapi.org/v2/everything?q={keyword}&sortBy=publishedAt&apiKey={api_key}"
        
        response = requests.get(url)
        data = response.json()
        
        if data.get('status') == 'ok':
            articles = data.get('articles', [])
            if articles:
                st.write(f"Found {len(articles)} articles related to '{keyword}':")
                for article in articles:
                    st.write("Title:", article.get('title'))
                    st.write("Source:", article.get('source').get('name'))
                    st.write("Published At:", article.get('publishedAt'))
                    st.write("Description:", article.get('description'))
                    st.write("URL:", article.get('url'))

                    # Perform sentiment analysis
                    sentiment = sia.polarity_scores(article.get('title'))['compound']
                    st.write("Sentiment Score:", sentiment)

                    st.write("---")
            else:
                st.write("No articles found.")
        else:
            st.write("Error fetching news data.")
    else:
        st.write("Please enter a keyword to search.")
