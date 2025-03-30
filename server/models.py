from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates, relationship
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    hero_powers = relationship("HeroPower", back_populates="hero", cascade="all, delete-orphan")

    serialize_rules = ("-hero_powers.hero",)

class Power(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    hero_powers = relationship("HeroPower", back_populates="power", cascade="all, delete-orphan")

    serialize_rules = ("-hero_powers.power",)

    @validates("description")
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return value

class HeroPower(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey("power.id"), nullable=False)

    hero = relationship("Hero", back_populates="hero_powers")
    power = relationship("Power", back_populates="hero_powers")

    serialize_rules = ("-hero.hero_powers", "-power.hero_powers")

    @validates("strength")
    def validate_strength(self, key, value):
        if value not in ["Strong", "Weak", "Average"]:
            raise ValueError("Strength must be 'Strong', 'Weak', or 'Average'")
        return value
