from pydantic import BaseModel

class DemandeBase(BaseModel):
    nom: str
    prenom: str
    ville: str  
    email: str  
    description: str

class DemandeCreate(DemandeBase):
    pass
