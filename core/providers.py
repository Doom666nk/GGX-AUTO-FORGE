class GGX_Data_Engine:
    def __init__(self):
        # Configuration de tes 3 Divisions et de tes produits Tech-Labs
        self.payload = [
            {
                "id": "GGX-TECH-001",
                "name": "DRILL LOUDNESS AUDITOR | Pro licence",
                "price": "44,99 $US",
                "url": "https://whop.com/checkout/plan_R9m4vKqW2B6x7/",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "ITU-R BS.1770 Integrated LUFS Analyzer",
                "stock": "TOP VENTE"
            },
            {
                "id": "GGX-TECH-002",
                "name": "LOFI NOISE SCULPTOR | Standard Edition",
                "price": "14,99 $US",
                "url": "https://whop.com/checkout/plan_Y2n3uXpL1T5z8/",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "High-End Lofi DSP Engine & Saturation",
                "stock": "PROMO -20%"
            },
            {
                "id": "GGX-SOL-001",
                "name": "GGX SOLUTIONS | Consulting",
                "price": "SUR DEVIS",
                "url": "https://whop.com/ggx-solutions/",
                "img": "https://files.whop.com/logos/GGX_Solutions_Logo.png",
                "desc": "Management & Business Consulting",
                "stock": "DISPONIBLE"
            }
        ]

    def get_payload(self):
        return self.payload
