import os
from flask import Flask, render_template_string

app = Flask(__name__)

# INVENTAIRE SÉCURISÉ - SOURCE UNIQUE
PRODUCTS = {
    "GGX-TECH-01": {
        "division": "TECH-LABS",
        "name": "DRILL LOUDNESS AUDITOR",
        "price": "44,99 $US",
        "url": "https://whop.com/checkout/plan_R9m4vKqW2B6x7/",
        "color": "#00ff41",
        "integrity": "SHA-256 VERIFIED"
    },
    "GGX-STUDIO-01": {
        "division": "STUDIOS",
        "name": "JAM TRACK: BLUES Am",
        "price": "39,99 $US",
        "url": "https://whop.com/checkout/plan_JAM_OFFICIEL",
        "color": "#ff00ff",
        "integrity": "32-BIT WAV / STEMS"
    },
    "GGX-STUDIO-02": {
        "division": "STUDIOS",
        "name": "THE MOON (WAV STEMS)",
        "price": "14,99 $US",
        "url": "https://whop.com/checkout/plan_MOON_OFFICIEL",
        "color": "#ff00ff",
        "integrity": "32-BIT / 48KHZ"
    },
    "GGX-SOL-01": {
        "division": "SOLUTIONS",
        "name": "BUSINESS ARCHITECT",
        "price": "99,99 $US",
        "url": "https://whop.com/checkout/plan_SOL_OFFICIEL",
        "color": "#00d1ff",
        "integrity": "VIP CONSULTING"
    }
}

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>GGX EMPIRE - V5.0 ACTIVE</title>
        <style>
            :root { --brass: #c4984a; --void: #080a0c; }
            body { background: var(--void); color: #e8ecf0; font-family: sans-serif; padding: 20px; }
            .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
            .card { border: 1px solid #333; background: #0e1114; padding: 15px; border-top: 4px solid; }
            .buy-btn { display: block; border: 1px solid; text-align: center; padding: 10px; text-decoration: none; margin-top: 15px; }
        </style>
    </head>
    <body>
        <h1 style="color:var(--brass); text-align:center;">🛡️ GGX EMPIRE CORE</h1>
        <div class="grid">
            {% for id, p in products.items() %}
            <div class="card" style="border-top-color: {{ p.color }};">
                <small style="color: {{ p.color }}; font-weight: bold;">{{ p.division }} | {{ id }}</small>
                <h3>{{ p.name }}</h3>
                <div style="font-size: 1.5rem; margin: 10px 0;">{{ p.price }}</div>
                <a href="{{ p.url }}" class="buy-btn" style="border-color: {{ p.color }}; color: {{ p.color }};">ACQUISITION UNITÉ</a>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """, products=PRODUCTS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
