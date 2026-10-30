
from supabook_cl import supabase

try:
    result = (
        supabase
        .table("user")
        .select("id")
        .limit(1)
        .execute()
    )

    print("Supabase database request succeeded!")
    print("Returned data:", result.data)

except Exception as error:
    print("Database request failed:")
    print(error)
