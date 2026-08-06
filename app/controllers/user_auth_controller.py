from app.database.connection import get_connection 
from app.security.password import ( hash_password, verify_password )
from app.security.jwt import ( create_access_token )

def check_uniqueness(user):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = f"""
    SELECT user_name, user_email FROM users
    WHERE user_name='{user.username}' and user_email='{user.email}'
    """
    #values = (user.username, user.email)
    #cursor.execute(query, values)
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    cursor.close()
    if (result):
        return 1 # user arleady exists
    else:
        return 0 # user does not exist
    

def register_user(user):
    unique_check = check_uniqueness(user)
    if (unique_check == 1):
        return {
            "message": "User already exists"
        }

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    hashed = hash_password(user.password)
    query = f"""
        INSERT INTO users
        (user_name, user_email, user_password)
        VALUES('{user.username}','{user.email}','{hashed}')
    """
    #values = (user.username, user.email, hashed)
    #cursor.execute(query, values)
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return {
        "message": "User registered successfully"
    }

def login_user(user):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = f"""
    SELECT user_id, user_name, user_email, user_password
    FROM users
    WHERE user_email = '{user.email}'
    """
    #values = (user.email,)
    #cursor.execute(query, values)
    cursor.execute(query)
    result = cursor.fetchone()
    if result == None:
            return {
                "message": "User does not exist"
            }
    
    verify_password(user.password, result["user_password"])
    cursor.close() 
    conn.close()
    
    if result and verify_password(user.password, result["user_password"]):
        token = create_access_token({"user_id": result["user_id"]})

        return {
            "access_token": token,
            "token_type": "bearer",
            "message": "Login successful",
            "user": {result["user_email"], result["user_id"]}
        }
    
    return {
        "message": "Invalid credentials"
    }      