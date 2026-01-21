from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

# Import ALL models so SQLModel sees them
from models import (
    CompanyPrimary,
    CompanySecondary,
    CompetitiveIntelligence,
    ContactInformation,
    DigitalPresenceBrand,
    FinancialsFunding,
    IndygxAssessment,
    PartnershipsEcosystem,
)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not found in .env")

engine = create_engine(DATABASE_URL, echo=True)

print("Creating tables in Supabase...")
SQLModel.metadata.create_all(engine)
print("All tables created successfully.")
