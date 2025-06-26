import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_html_node(self):
        node = HTMLNode(
            "<p>", "Hello World", props={"font-size": "14", "color": "green"}
        )
        self.assertEqual(node.tag, "<p>")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"font-size": "14", "color": "green"})

    def test_props_to_html(self):
        node = HTMLNode(
            "<p>", "Hello World", props={"font-size": "14", "color": "green"}
        )
        self.assertEqual(node.props_to_html(), ' font-size="14" color="green"')

    def test_to_html(self):
        node = HTMLNode(
            "<p>", "Hello World", props={"font-size": "14", "color": "green"}
        )
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
