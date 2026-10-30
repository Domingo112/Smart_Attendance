
import os
from dotenv import load_dotenv
from supabase import create_client

# Load the .env file
load_dotenv()

# Get the URL and key
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY")

# Check the values
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "Supabase URL or key is missing. Check your .env file."
    )

# Connect to Supabase
supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

print("Supabase client created successfully!")
