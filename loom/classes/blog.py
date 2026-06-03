import datetime

## Post metadata setup
class PostConfig:
    comments_allowed = False
    def __init__(self, comments_allow: bool):
        self.comments_allowed = comments_allow
    class PostTextConfig:
        title_size = 26
        heading_one_size = 20
        heading_two_size = 14
        heading_three_size = 12
        body_size = 11

        def __init__(self, title, h1, h2, h3, body):
            self.title_size = title
            self.heading_one_size = h1
            self.heading_two_size = h2
            self.heading_three_size = h3
            self.body_size = body
## Post setup
class Post:
    created_at = None
    def __init__(self, text_config: PostConfig.PostTextConfig, config: PostConfig):
        created_at = datetime.datetime.now()
        txt_conf = text_config
        
