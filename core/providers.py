class GGX_Data_Engine:
    def __init__(self):
        # Ici, chaque URL est liée directement à ton processeur de paiement Whop
        self.payload = [
            {
                "id": "GGX-TECH-001",
                "name": "DRILL LOUDNESS AUDITOR | Pro licence",
                "price": "44,99 $US",
                "url": "https://whop.com/checkout/plan_R9m4vKqW2B6x7/",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "ITU-R BS.1770 Integrated LUFS Analyzer.",
                "api_link": "active"
            },
            {
                "id": "GGX-TECH-002",
                "name": "LOFI NOISE SCULPTOR | Standard Edition",
                "price": "14,99 $US",
                "url": "https://whop.com/checkout/plan_Y2n3uXpL1T5z8/",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "High-End Lofi DSP Engine & Saturation.",
                "api_link": "active"
            }
        ]
    def get_payload(self):
        return self.payload
