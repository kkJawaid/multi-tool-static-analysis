from app.database.connection import get_connection

def profile_details(user):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
            SELECT user_name, user_email
            FROM users
            WHERE user_id = %s
        """
    
    values = (user,)
    cursor.execute(query, values)
    profile_details = cursor.fetchone()
    cursor.close()
    conn.close()

    return profile_details

def get_user_blogs_controller(userId):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
            SELECT b.blog_id, b.blog_title, b.blog_text, b.published_date, b.edited_date, b.blog_status, u.user_name
            FROM blogs b 
            INNER JOIN 
            users u 
            ON b.user_id = u.user_id 
            WHERE b.user_id = %s
        """
    values = (userId,)
    cursor.execute(query, values)
    user_blogs = cursor.fetchall()
    cursor.close()
    conn.close()
    return user_blogs 

def get_user_comments_controller(userId):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
            SELECT  u.user_name, b.blog_title, c.comment_text, c.published_time, c.edited_time
            FROM comments c 
            INNER JOIN 
            users u
            on c.user_id = u.user_id 
            INNER JOIN 
            blogs b 
            ON b.blog_id = c.blog_id 
            WHERE c.user_id = %s
        """
    values = (userId,)
    cursor.execute(query, values)
    user_comments = cursor.fetchall()
    cursor.close()
    conn.close()
    return user_comments 

def get_user_bookmarks_controller(userId):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
            SELECT  u.user_name, b.blog_title 
            FROM bookmarks bm 
            INNER JOIN 
            users u
            on u.user_id = bm.user_id 
            INNER JOIN 
            blogs b 
            ON bm.blog_id = b.blog_id 
            WHERE bm.user_id = %s
        """
    values = (userId,)
    cursor.execute(query, values)
    user_bookmarks = cursor.fetchall()
    cursor.close()
    conn.close()
    return user_bookmarks 

def update_user_profile_controller(user,userId):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    update_fields = []
    values = []

    # if "username" in user:
    #     update_fields.append("user_name = %s")
    #     values.append(user["username"])

    # if "email" in user:
    #     update_fields.append("user_email = %s")
    #     values.append(user["email"])

    # # plain text vulnerability
    # if "password" in user:
    #     update_fields.append("user_password = %s")
    #     values.append(user["password"])

    # intentional vulnerability: 
    # column name taken directly from user input, not validated against a whitelist of real column names
    for field_name, field_value in user.items():
        update_fields.append(f"{field_name} = %s")
        values.append(field_value)

    query = f"""
        UPDATE users
        SET {", ".join(update_fields)}
        WHERE user_id = %s
    """

    values.extend([userId])

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

    return {
        "message": "Profile updated successfully."
    }

def delete_user_profile_controller(userId):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
            DELETE FROM users 
            WHERE user_id = %s
        """
    values = (userId,)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "message": "Deleted profile successfully."
    } 