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