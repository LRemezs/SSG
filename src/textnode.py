from enum import Enum


class TextType(Enum):
    PLAIN_TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE_TEXT = "code_text"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        # check if 'other' is a TextNode
        if not isinstance(other, TextNode):
            return False

        # compare attributes
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
