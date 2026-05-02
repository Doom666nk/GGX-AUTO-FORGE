class GGX_Data_Engine:
    def __init__(self):
        # Chaque produit est lié à un ID Whop qui surveille le Webhook
        self.payload = [
            {
                "id": "GGX-DRIL-01",
                "name": "DRILL LOUDNESS AUDITOR",
                "price": "44,99 $US",
                "url": "https://whop.com/checkout/plan_R9m4vKqW2B6x7/",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "Analyseur LUFS - Webhook Auto-Delivery Active.",
                "webhook": "enabled"
            },
            {
                "id": "GGX-LOFI-02",
                "name": "LOFI NOISE SCULPTOR",
                "price": "14,99 $US",
                "url": "https://whop.com/checkout/plan_Y2n3uXpL1T5z8/",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "DSP Engine - V2 API Connector Active.",
                "webhook": "enabled"
            }
        ]
    def get_payload(self):
        return self.payload
