from textnode import TextNode, TextType


def main():
    # Create test TextNode
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")

    print(node)


# Call the main function:
if __name__ == "__main__":
    main()
