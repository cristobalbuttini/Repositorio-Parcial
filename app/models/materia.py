from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Materia(db.Model):
    __tablename__ = 'materias'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    codigo: str = db.Column(db.String(50), nullable=False)
    observacion: str = db.Column(db.String(255), nullable=True)
    
    
    orientacion_id: int = db.Column(db.Integer, db.ForeignKey('orientaciones.id'))
    orientacion = db.relationship('Orientacion', back_populates='materias')    # El backref se usa cuando es bidireccional (muchos a muchos))
   
    autoridades = db.relationship('Autoridad', secondary='autoridades_materias', back_populates='materias')
    
    def asociar_autoridad(self, autoridad):
        if autoridad not in self.autoridades:
            self.autoridades.append(autoridad)
    
    def desasociar_autoridad(self, autoridad):
        if autoridad in self.autoridades:
            self.autoridades.remove(autoridad)
            