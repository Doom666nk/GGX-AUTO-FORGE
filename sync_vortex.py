import re, os

def forge():
    # On reste sur 200 produits max pour garder le fichier léger
    products = [
        {"id": f"{i:03d}", "name": f"Produit {i}", "price": "49.99", "img": f"assets/images/p{i}.jpg", "url": "#", "zip": "#"}
        for i in range(1, 201)
    ]

    catalog_html = ""
    for p in products:
        catalog_html += f'''
        <div class="card">
            <h3>{p['name']}</h3>
            <p>{p['price']} USD</p>
            <a href="{p['url']}" class="btn">ACHAT</a>
        </div>'''

    template = f'''<!DOCTYPE html><html><head><style>body{{background:#000;color:#fff;font-family:sans-serif;}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;}}</style></head><body><div class="grid">{catalog_html}</div></body></html>'''
    
    with open("index.html", "w") as f:
        f.write(template)
    print(f"✅ FORGE RÉPARÉE : index.html créé (Taille normale).")

if __name__ == "__main__":
    forge()
