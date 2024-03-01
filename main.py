from urllib.request import urlopen


def generate_page_html(url: str, encoding: str = "utf-8"):
    page_obj = urlopen(url)
    page_html_bytes = page_obj.read()
    decoded_page = page_html_bytes.decode(encoding)
    return decoded_page


def main():
    url = ("https://catalog.ua.edu/undergraduate/human-environmental-sciences/clothing-textiles-interior-design"
           "/interior-design-bs/#requirementstextcontainer")
    page = generate_page_html(url, "utf-8")
    print(page)


if __name__ == "__main__":
    main()
