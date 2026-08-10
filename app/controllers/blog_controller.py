from app.database.connection import get_connection 

def fetch_all_blogs():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT * FROM blogs
    WHERE blog_status = 'public';
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return {
        "blogs": result
    } 

def fetch_specific_blog(blogId):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    # query = """
    # SELECT * FROM blogs
    # WHERE blog_id = %s;
    # """
    # values = (blogId,)
    # cursor.execute(query, values)

    # intentionally vulnerable
    query = f"""
    SELECT * FROM blogs
    WHERE blog_id = {blogId};
    """
    cursor.execute(query)

    result = cursor.fetchall()
    cursor.close()
    conn.close()

    if ( len(result) == 0 ): 
        return {
            "message": "Blog not found"
        }
    
    if( result[0].get('blog_status') == "private"):
        return {
            "message" : "Unauthorized access"
        }
    
    return {
        "blogs": result
    } 

def search_blog(search: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    # query = """
    # SELECT b.blog_title, b.blog_text, b.published_date, b.edited_date, b.blog_status, u.user_name
    # FROM blogs b
    # INNER JOIN users u
    # ON b.user_id = u.user_id
    # WHERE b.blog_title REGEXP %s OR b.blog_text REGEXP %s
    # ;
    # """
    # values = (search, search)
    # cursor.execute(query, values)

    # intentionally vulnerable
    query = f"""
    SELECT b.blog_title, b.blog_text, b.published_date, b.edited_date, b.blog_status, u.user_name
    FROM blogs b
    INNER JOIN users u
    ON b.user_id = u.user_id
    WHERE b.blog_title REGEXP '{search}' OR b.blog_text REGEXP '{search}'
    ;
    """
    cursor.execute(query)
    
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    if ( len(result) == 0 ): 
            return {
                "message": "Blog not found"
            }
        
    if( result[0].get('blog_status') == "private"):
        return {
            "message" : "Unauthorized access"
        }
    
    return {
        "blogs": result
    } 

def fetch_comments(blogId):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT b.blog_title, u.user_name, c.comment_text
    FROM blogs b
    INNER JOIN users u
    ON b.user_id = u.user_id
    INNER JOIN comments c 
    ON u.user_id = c.user_id
    WHERE b.blog_id = %s
    ;
    """
    values = (blogId,)
    cursor.execute(query, values)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    if ( len(result) == 0 ): 
            return {
                "message": "No comments"
            }
        
    if( result[0].get('blog_status') == "private"):
        return {
            "message" : "Unauthorized access"
        }
    
    return {
        "comments": result
    } 


def create_blog_function(userId, blog):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    INSERT INTO blogs
    (blog_title, blog_text, published_date, blog_status, user_id)
    VALUES
    (%s, %s, CURRENT_TIME(), %s, %s)
    ;
    """
    values = (blog.title, blog.text, blog.status, userId)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "message": "Blog created successfully"
    } 

def edit_blog_function(userId, blogId,blog):
    blog_found = fetch_specific_blog(blogId)
    if (blog_found['message'] == 'Blog not found'):
            return {
                "message": "Blog not found"
            }

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    update_fields = []
    values = []

    if "title" in blog:
        update_fields.append("blog_title = %s")
        values.append(blog["title"])

    if "text" in blog:
        update_fields.append("blog_text = %s")
        values.append(blog["text"])

    if "status" in blog:
        update_fields.append("blog_status = %s")
        values.append(blog["status"])

    update_fields.append("edited_date = CURRENT_TIMESTAMP")

    query = f"""
        UPDATE blogs
        SET {", ".join(update_fields)}
        WHERE blog_id = %s
        AND user_id = %s
    """

    values.extend([blogId, userId])

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

    return {
        "message": "Blog updated successfully"
    }

def delete_blog_function(userId, blogId):
    blog_found = fetch_specific_blog(blogId)
    if (blog_found['message'] == 'Blog not found'):
        return {
            "message": "Blog not found"
        }
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    DELETE FROM blogs
    WHERE user_id = %s AND blog_id = %s
    """
    values = (userId, blogId)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "message": "Blog deleted successfully"
    }
