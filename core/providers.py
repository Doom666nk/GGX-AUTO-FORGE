class GGX_Data_Engine:
    def __init__(self):
        # STRUCTURE PRÊTE POUR TES 200 PRODUITS
        # Remplace simplement les '#' par tes vrais liens Whop
        self.payload = [
            {"id": f"UNIT-{i:03d}", 
             "name": f"GGX ARSENAL PRODUCT {i}", 
             "price": "49.99", 
             "img": f"assets/images/product_{i}.jpg", 
             "url": "https://whop.com/checkout/direct_plan_XXX", # TON LIEN ICI
             "zip": f"assets/files/bundle_{i}.zip"} 
            for i in range(1, 201) # Génère automatiquement 200 entrées
        ]

    def get_payload(self):
        return self.payload
