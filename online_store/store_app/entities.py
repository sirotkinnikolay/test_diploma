class Category:
    def __init__(self, id, title, href, image, subcategories):
        self.id = id
        self.title = title
        self.image = image
        self.href = href
        self.subcategories = subcategories

    def to_dict(self):
        return {'id': self.id,
                'title': self.title,
                'image': self.image,
                'href': self.href,
                'subcategories': self.subcategories
                }
