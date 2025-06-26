class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        if children is None:
            children = []
        if props is None:
            props = {}
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        strings = []
        for prop, value in self.props.items():
            strings.append(f'{prop}="{value}"')
        return " " + " ".join(strings)

    def __repr__(self):
        return f"HTMLNode({repr(self.tag)}, {repr(self.value)}, {repr(self.children)}, {repr(self.props)})"
