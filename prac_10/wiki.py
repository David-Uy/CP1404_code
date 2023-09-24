import wikipedia


def main():
    import wikipedia

    search_query = input("Enter a page title or search phrase (or press Enter to quit): ")

    while search_query != "":
        try:
            page = wikipedia.page(search_query, auto_suggest=False)
            if page.exists():
                print("Title: '{}'".format(page.title))
                print("Summary: {}".format(page.summary))
                print("URL: {}".format(page.url))
            else:
                print("Page '{}' does not exist.".format(search_query))
        except wikipedia.exceptions.DisambiguationError as e:
            print("Disambiguation error: {}".format(e.options))
        except wikipedia.exceptions.PageError as e:
            print("Page error: {}".format(e))
        except Exception as e:
            print("An error occurred: {}".format(e))

        search_query = input("Enter a page title or search phrase (or press Enter to quit): ")


main()
