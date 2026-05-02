import os
from flask import Flask, render_template_string, flash

app = Flask(__name__)

# NOTRE RÉSERVOIR DE VÉRITÉ (Géré par GitHub)
# On utilise l'ID comme clé unique pour éviter les doublons
PRODUCTS = {
    "GGX-TECH-01": {
        "division": "TECH-LABS",
        "name": "DRILL LOUDNESS AUDITOR",
        "price": "44,99 $US",
        "url": "https://whop.com/checkout/plan_R9m4vKqW2B6x7/",
        "color": "#00ff41"
    },
    "GGX-STUDIO-01": {
        "division": "STUDIOS",
        "name": "JAM TRACK: BLUES Am",
        "price": "39,99 $US",
        "url": "https://whop.com/checkout/plan_JAM_OFFICIEL",
        "color": "#ff00ff"
    }
}

@app.route('/')
def index():
    return render_template_string("""
    <body style="background:#080a0c; color:#e8ecf0; font-family:sans-serif; padding:20px;">
        <h1 style="color:#c4984a; text-align:center; letter-spacing:10px;">🛡️ GGX EMPIRE CORE</h1>
        <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(300px, 1fr)); gap:20px;">
            {% for id, p in products.items() %}
            <div style="border:1px solid #333; border-top:5px solid {{p.color}}; padding:20px; background:rgba(14,17,20,0.9);">
                <small style="color:{{p.color}}; font-weight:bold;">{{p.division}} | {{id}}</small>
                <h3 style="text-transform:uppercase;">{{p.name}}</h3>
                <div style="font-size:1.8rem; font-weight:bold; margin:15px 0;">{{p.price}}</div>
                <a href="{{p.url}}" style="display:block; border:1px solid {{p.color}}; color:{{p.color}}; text-align:center; padding:12px; text-decoration:none; font-weight:bold;">ACQUISITION UNITÉ</a>
            </div>
            {% endfor %}
        </div>
    </body>
    """, products=PRODUCTS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
