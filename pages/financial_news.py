import streamlit as st
import nltk
import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from newspaper import Article
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('punkt')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# List of financial-related keywords
financial_keywords = ['finance', 'economy', 'market', 'stock', 'investment', 'bank', 'trading']

# List of reputable financial news sources
financial_sources = ['Bloomberg', 'Reuters', 'Financial Times', 'CNBC', 'Wall Street Journal']

# Streamlit UI
st.title("Filtered Financial News Analysis")

st.write("Enter a keyword to search for relevant financial news:")

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
            filtered_articles = []
            for article in data.get('articles', []):
                # Check if the article contains financial keywords or is from financial sources
                title = article.get('title', '').lower()
                source = article.get('source', {}).get('name', '')
                
                if any(keyword in title for keyword in financial_keywords) or source in financial_sources:
                    filtered_articles.append(article)
            
            if filtered_articles:
                st.write(f"Found {len(filtered_articles)} relevant articles related to '{keyword}':")
                for article in filtered_articles:
                    st.write("Title:", article.get('title'))
                    st.write("Source:", article.get('source').get('name'))
                    st.write("Published At:", article.get('publishedAt'))
                    st.write("Description:", article.get('description'))
                    st.write("URL:", article.get('url'))

                    # Fetch article content
                    url = article.get('url')
                    news_article = Article(url)
                    news_article.download()
                    news_article.parse()

                    # Summarize article content
                    news_article.nlp()  # Run NLP tasks
                    summary = news_article.summary
                    article['summary'] = summary
                    st.write("Summary:", summary)

                    # Perform sentiment analysis on summary
                    sentiment = sia.polarity_scores(summary)['compound']
                    st.write("Sentiment Score (Summary):", sentiment)

                    st.write("---")
                
                # Generate word cloud from summaries
                all_summaries = " ".join([article['summary'] for article in filtered_articles])
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_summaries)

                # Display the word cloud
                st.write("Word Cloud of Summaries")
                plt.figure(figsize=(10, 5))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis("off")
                st.pyplot(plt)

            else:
                st.write("No relevant articles found.")
        else:
            st.write("Error fetching news data.")
    else:
        st.write("Please enter a keyword to search.")
