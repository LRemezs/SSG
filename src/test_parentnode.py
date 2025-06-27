import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_tag_missing(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("", [child_node])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "All parent nodes MUST have a tag")

    def test_to_html_with_child_missing(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(
            str(context.exception),
            "How do you expect this to be a parent with no children??",
        )

    def test_to_html_with_props_on_levels(self):
        grandchild_node = LeafNode("b", "grandchild", {"class": "bold"})
        child_node = ParentNode(
            "span", [grandchild_node], {"class": "centered", "font-size": "12px"}
        )
        parent_node = ParentNode(
            "div", [child_node], {"class": "tester", "font": "Arial"}
        )
        self.assertEqual(
            parent_node.to_html(),
            '<div class="tester" font="Arial"><span class="centered" font-size="12px"><b class="bold">grandchild</b></span></div>',
        )

    def test_to_html_with_mixed_children_nodes(self):
        grand_child_1 = LeafNode("li", "item 1")
        grand_child_2 = LeafNode("li", "item 2")
        parent_node = ParentNode("ul", [grand_child_1, grand_child_2])
        childless_parent_node = LeafNode("span", "a span!")
        grandparent_node = ParentNode("div", [childless_parent_node, parent_node])

        self.assertEqual(
            grandparent_node.to_html(),
            "<div><span>a span!</span><ul><li>item 1</li><li>item 2</li></ul></div>",
        )

    def test_to_html_child_just_text(self):
        child_node_1 = LeafNode("b", "Bold text")
        child_node_2 = LeafNode(None, "just plain text")
        child_node_3 = LeafNode("i", "italic")
        parent_node = ParentNode("p", [child_node_1, child_node_2, child_node_3])

        self.assertEqual(
            parent_node.to_html(), "<p><b>Bold text</b>just plain text<i>italic</i></p>"
        )


if __name__ == "__main__":
    unittest.main()
