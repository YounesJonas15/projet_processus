from pydantic import BaseModel

class DemandeBase(BaseModel):
    nom: str
    prenom: str
    societe : str  
    email: str  
    description: str

class DemandeCreate(DemandeBase):
    pass

class Verification(BaseModel):
    id: str
    response: bool
    devis : str

class devis (BaseModel):
      montant: int