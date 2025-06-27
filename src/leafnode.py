from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Call parent constructor
        super().__init__(tag, value, None, props)  # children=None

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes MUST have value")
        if self.tag is None:
            return self.value

        props_html = ""
        if self.props:
            props_html = self.props_to_html()  # using parent's method

        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
