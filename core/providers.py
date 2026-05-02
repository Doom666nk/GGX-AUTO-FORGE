class GGX_Data_Engine:
    def __init__(self):
        # REMPLACE 'TON_LIEN_ICI' par tes vrais checkout Whop
        self.payload = [
            {"id": "001", "name": "VORTEX BYPASS ELITE", "price": "49.99", "url": "https://whop.com/checkout/TON_LIEN_1", "stock": "12"},
            {"id": "002", "name": "GHOST PROTOCOL V6", "price": "29.99", "url": "https://whop.com/checkout/TON_LIEN_2", "stock": "5"},
            {"id": "003", "name": "ARSENAL FULL BUNDLE", "price": "99.99", "url": "https://whop.com/checkout/TON_LIEN_3", "stock": "8"},
            # Ajoute tes autres produits ici...
        ]

    def get_payload(self):
        return self.payload
