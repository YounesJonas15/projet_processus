from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from db_fournisseur import Base


class Demande(Base):
    __tablename__ = "demandes"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    nom = Column(String)
    prenom = Column(String)
    description = Column(String)
    statut = Column(String)
    devis = Column(String)

