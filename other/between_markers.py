def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    beg_count = text.count(begin)
    end_count = text.count(end)

    begin_index = text.index(begin)+len(begin) if beg_count > 0 else 0
    end_index = text.index(end) if end_count > 0 else 0
    if not begin_index and not end_index:
        return text
    if begin_index and not end_index:
        return text[begin_index:]
    if not begin_index and end_index:
        return text[:text.index(end)]
    if begin_index and end_index:
        if begin_index < end_index:
            return text[begin_index:end_index]

    return ''


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')