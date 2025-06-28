from leafnode import LeafNode
from textnode import TextType


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            if not text_node.url:
                raise ValueError("URL is required for a LINK TextNode")
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            if not text_node.url:
                raise ValueError("URL is required for a IMAGE TextNode")
            return LeafNode(
                "img", "", props={"src": text_node.url, "alt": text_node.text}
            )
        case _:
            raise ValueError("Not a valid TextType to create a LeafNode")
