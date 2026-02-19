# VerityAI: Fake News Detector
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

# Current Limitations (What to Improve)
While the app works well for general news, there are a few things to keep in mind:
1. "Strict" Judging: The model is very suspicious. It often flags real news as "Fake" just because the writing style is new or technical. I designed it this way because it’s better to be safe than to let actual fake news pass.
   
2. Knowledge Gap: The model was trained on news from a couple of years ago. Since it doesn't have a "live" connection to the 2026 internet, it doesn't recognize brand-new topics or laws yet.
   
# *Try it Yourself*
Paste a news article into the app: [VerityAI](https://verity-ai.streamlit.app/)

Check the Credibility Score.

High scores mean the text follows professional journalistic patterns; low scores suggest sensationalism.
