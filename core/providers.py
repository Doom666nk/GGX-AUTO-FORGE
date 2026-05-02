class GGX_Data_Engine:
    def __init__(self):
        self.payload = [
            {
                "id": "GGX-TECH-001",
                "name": "DRILL LOUDNESS AUDITOR | Pro Licence",
                "price": "44.99 $US",
                "url": "https://whop.com/checkout/plan_R9m4vKqW2B6x7/",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "ITU-R BS.1770 Integrated LUFS Analyzer. Précision chirurgicale pour vos masters.",
                "stock": "PRODUIT ÉLITE"
            },
            {
                "id": "GGX-TECH-002",
                "name": "LOFI NOISE SCULPTOR | Standard Edition",
                "price": "14.99 $US",
                "url": "https://whop.com/checkout/plan_Y2n3uXpL1T5z8/",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "High-End Lofi DSP Engine & Saturation. Le son analogique dans votre DAW.",
                "stock": "-20% MAINTENANT"
            },
            {
                "id": "GGX-SOL-001",
                "name": "GGX SOLUTIONS | Consulting",
                "price": "SUR DEVIS",
                "url": "https://whop.com/ggx-solutions/",
                "img": "https://files.whop.com/logos/GGX_Solutions_Logo.png",
                "desc": "Expertise en déploiement IA et Micro-SaaS. Propulsez votre business.",
                "stock": "DISPONIBLE"
            }
        ]

    def get_payload(self):
        return self.payload
