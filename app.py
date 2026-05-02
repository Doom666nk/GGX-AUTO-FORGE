import os
from flask import Flask, render_template_string

app = Flask(__name__)

# ICI ON STOCKE TOUT DANS GIT - C'EST TON INVENTAIRE INDESTRUCTIBLE
# Chaque ligne ici est sauvegardée pour l'éternité dans ton historique GitHub
PRODUCTS = [
    {
        "id": "GGX-TECH-01",
        "division": "TECH-LABS",
        "name": "DRILL LOUDNESS AUDITOR",
        "price": "44,99 $US",
        "url": "https://whop.com/checkout/plan_R9m4vKqW2B6x7/",
        "color": "#00ff41",
        "integrity": "SHA-256 VERIFIED",
        "tag": "TECH"
    },
    {
        "id": "GGX-STUDIO-01",
        "division": "STUDIOS",
        "name": "JAM TRACK: BLUES Am (FULL PACK)",
        "price": "39,99 $US",
        "url": "https://whop.com/checkout/plan_JAM_OFFICIEL", # Ton lien de la capture
        "color": "#ff00ff",
        "integrity": "32-BIT WAV / STEMS",
        "tag": "JAM"
    },
    {
        "id": "GGX-SOL-01",
        "division": "SOLUTIONS",
        "name": "BUSINESS ARCHITECT",
        "price": "99,99 $US",
        "url": "https://whop.com/checkout/plan_SOL_OFFICIEL",
        "color": "#00d1ff",
        "integrity": "VIP CONSULTING",
        "tag": "SOL"
    }
    # Les 74 slots suivants seront ajoutés ici et archivés dans Git
]

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>GGX EMPIRE - GIT-BACKED V5.0</title>
        <style>
            :root { --brass: #c4984a; --void: #080a0c; }
            body { 
                background: var(--void); 
                color: #e8ecf0; 
                font-family: 'Barlow Condensed', sans-serif; 
                margin: 0; padding: 20px;
            }
            .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
            .card { 
                border: 1px solid #333; background: #0e1114; 
                padding: 15px; border-top: 4px solid;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            }
            .buy-btn { 
                display: block; border: 1px solid; text-align: center; 
                padding: 12px; text-decoration: none; font-weight: bold; margin-top: 15px;
            }
        </style>
    </head>
    <body>
        <h1 style="color:var(--brass); text-align:center; letter-spacing:5px;">🛡️ GGX GIT-STORAGE CORE</h1>
        <div class="grid">
            {% for p in products %}
            <div class="card" style="border-top-color: {{ p.color }};">
                <div style="color: {{ p.color }}; font-size: 0.8rem; font-weight: bold;">{{ p.division }}</div>
                <h3 style="margin: 10px 0;">{{ p.name }}</h3>
                <div style="font-size: 1.8rem; font-weight: bold; margin: 15px 0;">{{ p.price }}</div>
                <div style="font-size: 0.7rem; opacity: 0.5;">STATUS: {{ p.integrity }}</div>
                <a href="{{ p.url }}" class="buy-btn" style="border-color: {{ p.color }}; color: {{ p.color }};">ACQUISITION</a>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """, products=PRODUCTS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
