from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    email = Column(Text, nullable=True)
    username = Column(String(30), unique=True, nullable=True)
    password = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return self.username


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    image = Column(String(255))
    name = Column(String(30), nullable=True)
    description = Column(Text, nullable=False)
    price = Column(Integer)
    price_type = Column(String(4))
    slug = Column(String(100), unique=True, nullable=True)
    count = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return self.name


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    image = Column(String(255))
    name = Column(String(30), nullable=True)
    slug = Column(String(100), unique=True, nullable=True)
    comment = Column(Text)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return self.name


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    image = Column(String(255))
    name = Column(String(150), nullable=True)
    slug = Column(String(100), unique=True, nullable=True)
    who = Column(String(150))
    date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return self.name


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    image = Column(String(255))
    name = Column(String(30), nullable=True)
    slug = Column(String(100), unique=True, nullable=True)
    staff_type = Column(String(150))
    title = Column(String(80))
    date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return self.name