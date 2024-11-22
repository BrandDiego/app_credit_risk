import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_snowflake():
    """
    Crea una conexión segura a Snowflake usando credenciales validadas del archivo .env.
    """
    try:
        connection = snowflake.connector.connect(
            user=os.getenv("urcuqui"),
            password=os.getenv("LZJGinRcN6TiNudsJIllOcgp"),
            account=os.getenv("ctb59899.us-east-1"),
            warehouse=os.getenv("WH_ICESI")
        )
        print("Conexión a Snowflake establecida correctamente.")
        return connection
    except Exception as e:
        print(f"Error al conectar con Snowflake: {e}")
        raise
