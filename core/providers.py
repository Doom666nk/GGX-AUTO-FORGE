class GGX_Data_Engine:
    def __init__(self):
        # ICI TU METS TES VRAIS LIENS DE CHECKOUT WHOP
        self.payload = [
            {"id": "001", "name": "GHOST PROTOCOL V6", "price": "49.99", "img": "assets/images/unit1.jpg", "url": "https://whop.com/checkout/TON_LIEN_1", "zip": "assets/files/pack1.zip"},
            {"id": "002", "name": "VORTEX SYSTEM PRO", "price": "29.99", "img": "assets/images/unit2.jpg", "url": "https://whop.com/checkout/TON_LIEN_2", "zip": "assets/files/pack2.zip"},
            # Tu peux continuer jusqu'à 200...
        ]

    def get_payload(self):
        return self.payload
