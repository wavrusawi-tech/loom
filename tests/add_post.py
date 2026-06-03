import loom

post_config = loom.classes.blog.PostConfig(False)
post_text_config = loom.classes.blog.PostConfig.PostTextConfig(26, 20, 14, 12, 11)

post = loom.classes.blog.Post(post_text_config, post_config)