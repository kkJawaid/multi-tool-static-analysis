from app.database.connection import get_connection

def find_blog(blogId): 
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT blog_id, blog_status FROM blogs WHERE blog_id = %s;
    """
    values = (blogId,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result is None:
        return None 
    
    if result.get("blog_status") == "private":
        result = None
    return result

def find_bookmark(blogId, userId):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT * FROM bookmarks WHERE blog_id = %s AND user_id = %s;
    """
    values = (blogId, userId)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def create_bookmark_controller(blogId, userId):
    blog_result = find_blog(blogId)
    if blog_result is None:
        # for private blogs and blogs that don't exist
        return {
            "message": "Blog not found"
        }
    
    bookmark_result = find_bookmark(blogId, userId)
    if (bookmark_result is not None):
        return {
            "message": "Bookmark already exists!"
        }

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    INSERT INTO bookmarks
    (user_id, blog_id)
    VALUES
    (%s, %s);
    """
    values = (userId, blogId)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "message": "Bookmark successfully created;"
    }

def delete_bookmark_controller(blogId, userId):
    blog_result = find_blog(blogId)
    if blog_result is None:
        # for private blogs and blogs that don't exist
        return {
            "message": "Blog not found"
        }
    bookmark_result = find_bookmark(blogId, userId)
    if (bookmark_result is None):
        return {
            "message": "Bookmark does not exist."
        }
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    DELETE FROM bookmarks
    WHERE user_id = %s AND blog_id = %s;
    """
    values = (userId, blogId)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "message": "Bookmark succssfully deleted;"
    }