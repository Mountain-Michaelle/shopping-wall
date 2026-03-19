import uuid 

def generate_uuid() -> str:
    return str(uuid.uuid4)

def uuid_length() -> int:
    return 40