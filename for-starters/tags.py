def _normalize(words):
    """Make words lowercase and replace characters"""
    pass


def _read_rss():
    """Reads the RSS feed in"""
    pass


def count_tags():
    """Count the number of tags in our RSS feed"""
    pass


if __name__ == "__main__":
    MSG = '{}, {} not in test set'

    # print and test solution
    from test import parse_tags_html
    tests = list(parse_tags_html())

    counts = count_tags()
    for tag, count in counts:
        assert (tag, count) in tests, MSG.format(tag, count)
        print('{:<20} {}'.format(tag,count))
