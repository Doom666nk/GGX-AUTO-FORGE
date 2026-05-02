import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# NOTRE BASE DE DONNÉES (AUTO-REMPLIE PAR ASPIRATION)
PRODUCTS = [
    {
        "id": "GGX-TECH-01",
        "division": "TECH-LABS",
        "name": "DRILL LOUDNESS AUDITOR",
        "price": "44,99 $US",
        "url": "https://whop.com/checkout/plan_R9m4vKqW2B6x7/",
        "color": "#00ff41"
    }
]

# FONCTION D'ASPIRATION (CRAWLER)
def aspirer_produit(url_source):
    try:
        # Ici on simule l'aspiration des données Whop ou de ta forge
        # Dans un cas réel, on va chercher les balises <title> et les prix
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url_source, headers=headers, timeout=5)
        if r.status_code == 200:
            return {"status": "SUCCESS", "url": url_source}
    except Exception as e:
        return {"status": "ERROR", "msg": str(e)}

@app.route('/admin/aspirer/<path:target_url>')
def api_aspirer(target_url):
    # Cette route te permet de dire au Cloud : "Aspire ce lien !"
    result = aspirer_produit(target_url)
    return jsonify(result)

@app.route('/')
def index():
    # Ton design V5.0 Empire reste inchangé
    return render_template_string("""
    <h1 style="color:#c4984a;">🛡️ GGX EMPIRE — ASPIRATION ACTIVE</h1>
    <div class="grid">
        {% for p in products %}
        <div class="card" style="border-top: 4px solid {{ p.color }};">
            <h3>{{ p.name }}</h3>
            <p>{{ p.price }}</p>
            <a href="{{ p.url }}" class="buy-btn" style="color:{{ p.color }};">ACQUISITION</a>
        </div>
        {% endfor %}
    </div>
    """, products=PRODUCTS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
