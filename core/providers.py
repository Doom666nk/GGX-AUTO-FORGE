class GGX_Data_Engine:
    def __init__(self):
        self.payload = [
            {
                "id": "GGX-TECH-01",
                "name": "DRILL LOUDNESS AUDITOR",
                "price": "44,99 $US",
                "url": "https://whop.com/checkout/plan_R9m4vKqW2B6x7/",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "ITU-R BS.1770 Integrated LUFS Analyzer",
                "type": "Software/DSP",
                "version": "1.0.0",
                "integrity": "SHA-256 Verified",
                "commission": "40%"
            },
            {
                "id": "GGX-TECH-02",
                "name": "LOFI NOISE SCULPTOR",
                "price": "14,99 $US",
                "url": "https://whop.com/checkout/plan_Y2n3uXpL1T5z8/",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "High-End Lofi DSP Engine & Saturation",
                "type": "Software/DSP",
                "version": "1.0.0",
                "integrity": "SHA-256 Verified",
                "commission": "40%"
            }
        ]
    def get_payload(self):
        return self.payload
