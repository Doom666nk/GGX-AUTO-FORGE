class GGX_Data_Engine:
    def __init__(self):
        self.payload = [
            {
                "id": "GGX-TECH-01",
                "name": "NOM_DU_PRODUIT_ICI",
                "price": "44.99 $USD",
                "url": "LIEN_WHOP_ICI",
                "img": "https://files.whop.com/logos/GGX_TechLabs_Logo.png",
                "type": "SOFTWARE",
                "desc": "DESCRIPTION_COURTE"
            },
            {
                "id": "GGX-STEM-01",
                "name": "NOM_DE_LA_TRACK_ICI",
                "price": "4.99 $USD",
                "url": "LIEN_WHOP_ICI",
                "img": "https://files.whop.com/logos/GGX_StudiosMedia_Logo.png",
                "type": "STEM",
                "desc": "BASS / DRUMS / VOCAL"
            }
            # Tu peux rajouter autant de blocs { ... } que tu veux ici !
        ]

    def get_payload(self):
        return self.payload
