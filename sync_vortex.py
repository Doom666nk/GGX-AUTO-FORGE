import sys
import os

sys.path.append(os.getcwd())
from core.providers import GGX_Data_Engine

engine = GGX_Data_Engine()
products = engine.get_payload()

catalog_html = ""
for p in products:
    # Attribution de la couleur selon la division
    color = "#00ff41" # Vert par défaut (Tech)
    if "SOL" in p['id']: color = "#00d1ff" # Bleu (Solutions)
    if "STUDIO" in p['id'] or "STEM" in p['id']: color = "#ff00ff" # Violet (Studios)
    
    catalog_html += f'''
    <div class="card" style="border-color: {color}; box-shadow: 0 0 10px {color}33;">
        <div class="division-badge" style="background: {color}; color: #000;">{p['id'].split('-')[1]}</div>
        <img src="{p['img']}" class="product-img">
        <h3 style="color: {color};">{p['name']}</h3>
        <p class="description">{p['desc']}</p>
        <div class="price" style="color: {color};">{p['price']}</div>
        <a href="{p['url']}" class="buy-btn" style="background: {color};">ACHETER MAINTENANT</a>
    </div>
    '''

with open("index.html", "r") as f:
    content = f.read()

start_tag = ""
end_tag = ""

if start_tag in content and end_tag in content:
    new_content = content.split(start_tag)[0] + start_tag + catalog_html + end_tag + content.split(end_tag)[1]
    with open("index.html", "w") as f:
        f.write(new_content)
    print("✅ TUNING TERMINÉ : Couleurs et divisions synchronisées.")
