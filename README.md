# Fake News Detector
I built this app to tackle one of the biggest problems on the internet: misinformation. Using Natural Language Processing, it analyzes the writing style of an article to see if it’s trustworthy or just clickbait.

# How it Works:
--> The Model: I used a PassiveAggressive Classifier. It's great for news because it’s designed to learn quickly from mistakes as new types of "fake news" evolve.

--> The Secret Sauce: I wrote custom logic to strip out "source identifiers" (like Reuters tags). This forces the AI to look at the content of the story rather than just recognizing a brand name.

--> The Math: It uses TF-IDF Vectorization to ignore common words (like "the" or "and") and focus on the unique words that define a story's credibility.

# Built With:
1. Python (The backbone)

2. Scikit-Learn (The AI "brain")

3. Streamlit (The web interface)

4. Pandas & NLTK (Data cleaning)
   

# *Try it Yourself*
Paste a news article into the app: 

Check the Credibility Score.

High scores mean the text follows professional journalistic patterns; low scores suggest sensationalism.
