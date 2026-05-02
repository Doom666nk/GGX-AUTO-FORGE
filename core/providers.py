class GGX_Data_Engine:
    def __init__(self):
        self.payload = [
            {
                "id": "PACK-001",
                "name": "MEGA PACK: AM Jam Blues Deluxe",
                "price": "39.99 $USD",
                "url": "https://whop.com/checkout/TON_LIEN_ZIP_BLUES",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "Full Zip: Bass, Drum, Guitar, Vocal & Stems. Qualité Studio.",
                "stock": "ZIP COMPLET"
            },
            {
                "id": "STEM-001",
                "name": "STEM: Blues Bass Line (Am)",
                "price": "4.99 $USD",
                "url": "https://whop.com/checkout/TON_LIEN_BASS",
                "img": "https://files.whop.com/logos/GGX_StudiosMedia_Logo.png",
                "desc": "Piste séparée (WAV). Idéal pour pratique solo.",
                "stock": "SINGLE TRACK"
            },
            {
                "id": "STEM-002",
                "name": "STEM: Blues Drum Kit (Am)",
                "price": "4.99 $USD",
                "url": "https://whop.com/checkout/TON_LIEN_DRUM",
                "img": "https://files.whop.com/logos/GGX_StudiosMedia_Logo.png",
                "desc": "Piste batterie brute. 120 BPM.",
                "stock": "SINGLE TRACK"
            },
            {
                "id": "PACK-002",
                "name": "MEGA PACK: Rock Fusion Jam",
                "price": "39.99 $USD",
                "url": "https://whop.com/checkout/TON_LIEN_ZIP_ROCK",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "desc": "Full Zip: Multi-tracks for mixing & practice.",
                "stock": "ZIP COMPLET"
            }
        ]

    def get_payload(self):
        return self.payload
