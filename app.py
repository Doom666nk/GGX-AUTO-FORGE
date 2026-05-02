import os
from flask import Flask, render_template_string

app = Flask(__name__)

# TON INVENTAIRE - PROPRIÉTÉ DE GGX
# On a nos 3 piliers, et on laisse la porte ouverte pour les 74 suivants
PRODUCTS = [
    {
        "id": "GGX-TECH-01",
        "division": "TECH-LABS",
        "name": "DRILL LOUDNESS AUDITOR",
        "price": "44,99 $US",
        "url": "https://whop.com/checkout/plan_R9m4vKqW2B6x7/",
        "color": "#00ff41"
    },
    {
        "id": "GGX-STUDIO-01",
        "division": "STUDIOS",
        "name": "JAM TRACK: BLUES Am",
        "price": "39,99 $US",
        "url": "https://whop.com/checkout/plan_JAM_OFFICIEL",
        "color": "#ff00ff"
    },
    {
        "id": "GGX-SOL-01",
        "division": "SOLUTIONS",
        "name": "BUSINESS ARCHITECT",
        "price": "99,99 $US",
        "url": "https://whop.com/checkout/plan_SOL_OFFICIEL",
        "color": "#00d1ff"
    }
    # 📥 LES PROCHAINES ASPIRATIONS ARRIVERONT ICI
]

@app.route('/')
def index():
    return render_template_string("""
    <body style="background:#080a0c; color:#e8ecf0; font-family:sans-serif;">
        <h1 style="color:#c4984a; text-align:center;">🛡️ EMPIRE CORE V5.0</h1>
        <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(300px, 1fr)); gap:20px;">
            {% for p in products %}
            <div style="border:1px solid #333; border-top:5px solid {{p.color}}; padding:20px; background:#0e1114;">
                <small style="color:{{p.color}}">{{p.division}}</small>
                <h3>{{p.name}}</h3>
                <div style="font-size:1.5rem; margin:10px 0;">{{p.price}}</div>
                <a href="{{p.url}}" style="display:block; border:1px solid {{p.color}}; color:{{p.color}}; text-align:center; padding:10px; text-decoration:none;">ACQUISITION</a>
            </div>
            {% endfor %}
        </div>
    </body>
    """, products=PRODUCTS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
