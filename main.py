import os
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs('reports', exist_ok=True)
os.makedirs('data', exist_ok=True)

print("--- Step 1: Loading Dataset ---")
df = pd.read_csv('data/audio_wearables_2000_comments.csv')

print("--- Step 2: Cleaning Text ---")
def clean_review(text):
    text = str(text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['cleaned_text'] = df['review_text'].apply(clean_review)

print("--- Step 3: Running Pure Python Sentiment Analysis ---")

# Custom Tech Slang Dictionary (Zero NLTK)
custom_lexicon = {
    'killer': 2.0, 'zabardast': 2.5, 'top notch': 2.5, 'op': 2.0,
    'sleek': 1.8, 'value': 1.5, 'accurate': 1.5, 'good': 1.5, 'great': 2.0,
    'bakwas': -2.5, 'delay': -1.8, 'latency': -1.5, 'drain': -2.0,
    'cheap': -1.8, 'kharab': -2.0, 'waste': -2.5, 'bad': -2.0, 'slow': -1.5
}

def get_custom_sentiment(text):
    text_lower = text.lower()
    score = 0.0
    for word, weight in custom_lexicon.items():
        if word in text_lower:
            score += weight
            
    if score > 0:
        return 'Positive', min(score / 3.0, 1.0)
    elif score < 0:
        return 'Negative', max(score / 3.0, -1.0)
    else:
        return 'Neutral', 0.0

results = df['cleaned_text'].apply(get_custom_sentiment)
df['sentiment'] = [r[0] for r in results]
df['sentiment_score'] = [r[1] for r in results]

# Save analyzed file
df.to_csv('data/analyzed_audio_wearables.csv', index=False)
print("Analyzed data saved in 'data/' folder.")

print("\n--- Brand-wise Sentiment Summary ---")
summary = pd.crosstab(df['brand'], df['sentiment'], normalize='index') * 100
print(summary.round(2))

print("\n--- Step 4: Generating Professional Charts ---")
# Chart 1: Brand Comparison
plt.figure(figsize=(9, 5))
sns.countplot(data=df, x='brand', hue='sentiment', palette='Set2')
plt.title('Audionic vs Zero Lifestyle - Sentiment Comparison', fontsize=13, fontweight='bold')
plt.xlabel('Brand')
plt.ylabel('Review Count')
plt.legend(title='Sentiment')
plt.tight_layout()
plt.savefig('reports/sentiment_comparison.png', dpi=300)
plt.close()

# Chart 2: Product-wise Sentiment
plt.figure(figsize=(11, 6))
sns.countplot(data=df, y='product', hue='sentiment', palette='coolwarm')
plt.title('Product-Wise Sentiment Breakdown', fontsize=13, fontweight='bold')
plt.xlabel('Review Count')
plt.ylabel('Product Model')
plt.legend(title='Sentiment')
plt.tight_layout()
plt.savefig('reports/product_wise_sentiment.png', dpi=300)
plt.close()

print("\nCharts successfully saved inside 'reports/' folder!")
print("Pipeline Execution Completed Successfully!")