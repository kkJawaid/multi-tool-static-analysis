from app.database.connection import get_connection

def check_privacy_status(blogId):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT blog_status FROM blogs WHERE blog_id = %s
    """
    values =  (blogId, )
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result is None:
        return "Blog does not exist."
    if result[0] == "private":
        return 0
    else:
        return 1 

def create_comment_controller(userId, blogId, comment):
    blog_status = check_privacy_status(blogId)
    if blog_status != 1:
        return {
            "message": "Unauthorized access."
        }
    
    conn = get_connection()
    cursor = conn.cursor()
    # leaving this as intentionally parameterized since this is where malicious data would get stored
    query = """
    INSERT INTO comments
    (comment_text, published_time, user_id, blog_id)
    VALUES
    (%s, CURRENT_TIMESTAMP, %s, %s)
    """
    values = (comment.commentText, userId, blogId )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "message": "Comment successfully created."
    }

def update_comment_controller(blogId, comment, commentId):
    blog_status = check_privacy_status(blogId)
    if blog_status != 1:
        return {
            "message": "Unauthorized access."
        }
    
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    UPDATE comments
    SET comment_text = %s, edited_time = CURRENT_TIMESTAMP
    WHERE 
    comment_id = %s;
    """
    values = (comment.commentText, commentId )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "message": "Comment successfully updated."
    }

def delete_comment_controller(blogId, commentId):
    blog_status = check_privacy_status(blogId)
    if blog_status != 1:
        return {
            "message": "Unauthorized access."
        }
    
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    DELETE FROM comments WHERE comment_id = %s;
    """
    values = (commentId, )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "message": "Comment successfully deleted."
    }

# intentional vulnerability 
# separating injection point and execution point to demonstrate inter-procedural vulnerability
def find_related_comments_controller(commentId):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT comment_text FROM comments WHERE comment_id = %s", (commentId,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row is None:
        return {"message": "Comment not found"}
    stored_text = row[0]
    return search_comments_admin(stored_text)

def search_comments_admin(keyword_from_stored_comment):
    conn = get_connection()
    cursor = conn.cursor()
    # intentional second-order SQLi: 
    # keyword_from_stored_comment originates from a previously stored, unsanitized comment_text value
    query = f"""
    SELECT comment_id, comment_text, user_id
    FROM comments
    WHERE comment_text LIKE '%{keyword_from_stored_comment}%'
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result