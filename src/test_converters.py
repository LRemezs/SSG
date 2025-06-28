import unittest

from converters import text_node_to_html_node
from textnode import TextNode, TextType


class TestConverter(unittest.TestCase):
    def test_plain_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic_text(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code_text(self):
        node = TextNode("This is a code text node", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link_text(self):
        node = TextNode("This is a link text node", TextType.LINK, "google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href": "google.com"})

    def test_image_text(self):
        node = TextNode("Alt Text", TextType.IMAGE, "test.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "test.jpg", "alt": "Alt Text"})

    def test_invalid_type(self):
        node = TextNode("Not a type", None)
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(node)
        self.assertEqual(
            str(context.exception), "Not a valid TextType to create a LeafNode"
        )

    def test_image_text_wo_url(self):
        node = TextNode("Alt Text", TextType.IMAGE)
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "URL is required for a IMAGE TextNode")

    def test_link_text_wo_url(self):
        node = TextNode(
            "This is a link text node",
            TextType.LINK,
        )
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "URL is required for a LINK TextNode")
