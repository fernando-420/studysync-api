from dotenv import load_dotenv
load_dotenv()

from src.database.connection import engine, Base
from src.models.db_models import Usuario, Sesion

print("Creando tablas en Supabase...")
Base.metadata.create_all(bind=engine)
print("¡Tablas creadas exitosamente!")