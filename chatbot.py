
import pandas as pd
import os

# Analyzed dataset load karein
data_path = 'data/analyzed_audio_wearables.csv'

if not os.path.exists(data_path):
    print("Error: Analyzed dataset nahi mila! Pehle 'main.py' run karein.")
    exit()

df = pd.read_csv(data_path)

def audio_sentiment_chatbot(query):
    query = query.lower()
    
    # 1. Total Reviews Query
    if 'total' in query or 'kitne comments' in query or 'how many reviews' in query:
        return f"📊 Total dataset mein {len(df)} reviews hain (Audionic aur Zero Lifestyle ke mil kar)."
    
    # 2. Audionic Stats
    elif 'audionic' in query:
        aud_df = df[df['brand'] == 'Audionic']
        pos = len(aud_df[aud_df['sentiment'] == 'Positive'])
        neg = len(aud_df[aud_df['sentiment'] == 'Negative'])
        neu = len(aud_df[aud_df['sentiment'] == 'Neutral'])
        return f"🎧 Audionic Stats:\n  - Positive Reviews: {pos}\n  - Negative Reviews: {neg}\n  - Neutral Reviews: {neu}"
    
    # 3. Zero Lifestyle Stats
    elif 'zero lifestyle' in query or 'zero' in query:
        zero_df = df[df['brand'] == 'Zero Lifestyle']
        pos = len(zero_df[zero_df['sentiment'] == 'Positive'])
        neg = len(zero_df[zero_df['sentiment'] == 'Negative'])
        neu = len(zero_df[zero_df['sentiment'] == 'Neutral'])
        return f"⌚ Zero Lifestyle Stats:\n  - Positive Reviews: {pos}\n  - Negative Reviews: {neg}\n  - Neutral Reviews: {neu}"
    
    # 4. Most Popular / Likes Query
    elif 'popular' in query or 'likes' in query or 'sab se zyada' in query:
        top_review = df.loc[df['likes'].idxmax()]
        return f"🔥 Sab se zyada likes wala review ({top_review['likes']} likes):\n  Brand: {top_review['brand']} ({top_review['product']})\n  Review: '{top_review['review_text']}'\n  [Sentiment: {top_review['sentiment']}]"
    
    else:
        return "🤖 Maaf kijiye, main yeh samajh nahi saka. Aap in cheezon ke baray mein pooch sakte hain:\n  - 'Audionic ke baray mein batao'\n  - 'Zero Lifestyle stats'\n  - 'Sab se zyada likes kis review par hain?'\n  - 'Total reviews kitne hain?'"

if __name__ == "__main__":
    print("=" * 60)
    print("🤖 Audio & Wearables Interactive Sentiment Chatbot Active!")
    print("Aap apne sawal pooch sakte hain. (Band karne ke liye 'exit' ya 'quit' likhein)")
    print("=" * 60 + "\n")
    
    while True:
        user_input = input("Aapka Sawal: ").strip()
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot closed. Allah Hafiz!")
            break
        if not user_input:
            continue
        
        response = audio_sentiment_chatbot(user_input)
        print(f"\n{response}\n" + "-" * 50)