from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        # Call parent constructor
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes MUST have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("How do you expect this to be a parent with no children??")

        props_html = ""
        if self.props:
            props_html = self.props_to_html()  # using parent's method

        child_html = ""
        for child in self.children:
            child_html += child.to_html()

        return f"<{self.tag}{props_html}>{child_html}</{self.tag}>"
