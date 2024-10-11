def create_task(topic):
    return f'''
    Write a blog post about "{topic['title']}". 
    Focus specifically on the following: {topic['description']}.
    Make sure the post is concise, engaging, and stays within 100 words.
    '''

def save_blog_post(blog_post, filename):
    with open(filename, "w") as file:
        file.write(blog_post)

