import os
from flask import Flask, render_template_string

app = Flask(__name__)

# LES 3 BOUTIQUES (DIVISIONS) - STOCKAGE PERMANENT
PRODUCTS = [
    {
        "id": "GGX-TECH-01",
        "division": "TECH-LABS",
        "name": "DRILL LOUDNESS AUDITOR",
        "price": "44,99 $US",
        "url": "https://whop.com/checkout/plan_R9m4vKqW2B6x7/",
        "color": "#00ff41", # VERT IMPACT
        "integrity": "SHA-256 VERIFIED",
        "mission": "Analyse de Loudness ITU-R BS.1770"
    },
    {
        "id": "GGX-STUDIO-01",
        "division": "STUDIOS",
        "name": "JAM TRACK: BLUES Am (FULL PACK)",
        "price": "39,99 $US",
        "url": "https://whop.com/checkout/plan_JAM_OFFICIEL",
        "color": "#ff00ff", # MAGENTA IMPACT
        "integrity": "32-BIT WAV / STEMS",
        "mission": "Pack complet de Stems Multitrack"
    },
    {
        "id": "GGX-SOL-01",
        "division": "SOLUTIONS",
        "name": "BUSINESS ARCHITECT",
        "price": "99,99 $US",
        "url": "https://whop.com/checkout/plan_SOL_OFFICIEL",
        "color": "#00d1ff", # BLEU IMPACT
        "integrity": "VIP ACCESS",
        "mission": "Structure d'entreprise et Consulting"
    }
]

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>GGX EMPIRE - BOUTIQUES OFFICIELLES</title>
        <style>
            :root { --brass: #c4984a; --void: #080a0c; }
            body { 
                background: var(--void); color: #e8ecf0; 
                font-family: 'Barlow Condensed', sans-serif; padding: 20px;
                background-image: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('https://files.whop.com/logos/GGX_TechLabs_Logo.png');
                background-attachment: fixed; background-size: 300px;
            }
            .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 25px; max-width: 1200px; margin: auto; }
            .card { 
                border: 1px solid #333; background: rgba(14, 17, 20, 0.9); 
                padding: 20px; border-top: 5px solid; position: relative;
                box-shadow: 0 15px 35px rgba(0,0,0,0.8);
            }
            .division-name { font-weight: 900; font-size: 0.8rem; letter-spacing: 2px; margin-bottom: 15px; }
            .product-title { font-size: 1.6rem; margin: 10px 0; font-weight: 800; text-transform: uppercase; }
            .price-tag { font-size: 2rem; font-weight: 900; margin: 20px 0; text-align: center; color: #fff; }
            .buy-btn { 
                display: block; border: 1px solid; text-align: center; 
                padding: 15px; text-decoration: none; font-weight: 900; 
                letter-spacing: 2px; transition: 0.4s;
            }
        </style>
    </head>
    <body>
        <div style="text-align:center; margin-bottom: 60px;">
            <h1 style="color:var(--brass); letter-spacing:15px; text-transform:uppercase;">🛡️ GGX EMPIRE CORE</h1>
            <p style="color:var(--brass); opacity:0.7;">V5.0 — BOUTIQUES ENREGISTRÉES</p>
        </div>
        <div class="grid">
            {% for p in products %}
            <div class="card" style="border-top-color: {{ p.color }};">
                <div class="division-name" style="color: {{ p.color }};">{{ p.division }}</div>
                <div style="font-size: 0.7rem; opacity: 0.4;">UNIT_ID: {{ p.id }}</div>
                <h3 class="product-title">{{ p.name }}</h3>
                <p style="font-size: 0.8rem; opacity: 0.6; min-height: 40px;">MISSION: {{ p.mission }}</p>
                <div class="price-tag">{{ p.price }}</div>
                <a href="{{ p.url }}" class="buy-btn" style="border-color: {{ p.color }}; color: {{ p.color }};">ACQUISITION UNITÉ</a>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """, products=PRODUCTS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
