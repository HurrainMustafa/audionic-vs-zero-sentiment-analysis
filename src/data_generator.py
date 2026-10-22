import pandas as pd
import random
import os

os.makedirs('data', exist_ok=True)

brands = ['Audionic', 'Zero Lifestyle']
audionic_products = ['Airbud 550', 'Max 4', 'Airbud 425', 'Airbud 335', 'Vision 5', 'Classic Pods']
zero_products = ['Z-Ring Smartwatch', 'Pulse Smartwatch', 'Blade Earbuds', 'Quantum Watch', 'Bolt Smartwatch', 'Helix Pods']

positive_templates = [
    "Yeh {product} ka bass killer hai! Battery timing bhi zabardast hai.",
    "Boht hi sasta aur value for money product hai {brand} ka.",
    "Sound quality top notch hai, {product} is an op choice!",
    "Sleek design aur battery backup kamaal ka hai. Highly recommended!",
    "Connectivity fast hai aur mic ki clarity bhi achi hai.",
    "Zabardast experience raha {brand} ke sath, build quality amazing hai."
]

negative_templates = [
    "{product} ki battery drain problem boht zyada hai, waste of money.",
    "Mic quality boht bakwas hai, call par awaz hi nahi jati.",
    "Disconnectivity issue aur high latency aati hai gaming mein.",
    "Material cheap lag raha hai, {brand} ne quality compromise ki hai.",
    "Kharab product hai, kuch din baad hi kharab ho gaya.",
    "Overpriced hai aur performance bilkul slow hai."
]

neutral_templates = [
    "Average product hai, price ke hisab se theek thak hai.",
    "{product} theek chal raha hai, na zyada acha na bura.",
    "Normal battery timing hai, everyday use ke liye theek hai.",
    "Design theek hai lekin sound thora aur behtar ho sakta tha."
]

data = []
for i in range(2200):
    brand = random.choice(brands)
    product = random.choice(audionic_products) if brand == 'Audionic' else random.choice(zero_products)
    category = random.choices(['Positive', 'Negative', 'Neutral'], weights=[0.55, 0.30, 0.15])[0]
    
    if category == 'Positive':
        template = random.choice(positive_templates)
    elif category == 'Negative':
        template = random.choice(negative_templates)
    else:
        template = random.choice(neutral_templates)
        
    review_text = template.format(product=product, brand=brand)
    likes = random.randint(0, 350)
    
    data.append({
        'brand': brand,
        'product': product,
        'review_text': review_text,
        'likes': likes
    })

df = pd.DataFrame(data)
df.to_csv('data/audio_wearables_2000_comments.csv', index=False)
print("Dataset generated successfully inside 'data/' folder!")