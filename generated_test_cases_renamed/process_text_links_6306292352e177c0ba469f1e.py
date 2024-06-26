import re
from typing import Set, Tuple
from urllib.parse import urlparse

import bleach
from bleach import callbacks

ILLEGAL_TAG_CHARS = "!#$%^&*+.,@£/()=?`'\\{[]}~;:\"’”—\xa0"


def decode_if_bytes(text):
    try:
        return text.decode("utf-8")
    except AttributeError:
        return text


def encode_if_text(text):
    try:
        return bytes(text, encoding="utf-8")
    except TypeError:
        return text


def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    """Find tags in text.

    Tries to ignore tags inside code blocks.

    Optionally, if passed a "replacer", will also replace the tag word with the result
    of the replacer function called with the tag word.

    Returns a set of tags and the original or replaced text.
    """
    found_tags = set()
    # <br> and <p> tags cause issues in us finding words - add some spacing around them
    new_text = text.replace("<br>", " <br> ").replace("<p>", " <p> ").replace("</p>", " </p> ")
    lines = new_text.splitlines(keepends=True)
    final_lines = []
    code_block = False
    final_text = None
    # Check each line separately
    for line in lines:
        final_words = []
        if line[0:3] == "```":
            code_block = not code_block
        if line.find("#") == -1 or line[0:4] == "    " or code_block:
            # Just add the whole line
            final_lines.append(line)
            continue
        # Check each word separately
        words = line.split(" ")
        for word in words:
            if word.find('#') > -1:
                candidate = word.strip().strip("([]),.!?:*_%/")
                if candidate.find('<') > -1 or candidate.find('>') > -1:
                    # Strip html
                    candidate = bleach.clean(word, strip=True)
                # Now split with slashes
                candidates = candidate.split("/")
                to_replace = []
                for candidate in candidates:
                    if candidate.startswith("#"):
                        candidate = candidate.strip("#")
                        if test_tag(candidate.lower()):
                            found_tags.add(candidate.lower())
                            to_replace.append(candidate)
                if replacer:
                    tag_word = word
                    try:
                        for counter, replacee in enumerate(to_replace, 1):
                            tag_word = tag_word.replace("#%s" % replacee, replacer(replacee))
                    except Exception:
                        pass
                    final_words.append(tag_word)
                else:
                    final_words.append(word)
            else:
                final_words.append(word)
        final_lines.append(" ".join(final_words))
    if replacer:
        final_text = "".join(final_lines)
    if final_text:
        final_text = final_text.replace(" <br> ", "<br>").replace(" <p> ", "<p>").replace(" </p> ", "</p>")
    return found_tags, final_text or text


def get_path_from_url(url: str) -> str:
    """
    Return only the path part of an URL.
    """
    parsed = urlparse(url)
    return parsed.path


<insert generated code here>


def test_tag(tag: str) -> bool:
    """Test a word whether it could be accepted as a tag."""
    if not tag:
        return False
    for char in ILLEGAL_TAG_CHARS:
        if char in tag:
            return False
    return True


def validate_handle(handle):
    """
    Very basic handle validation as per
    https://diaspora.github.io/diaspora_federation/federation/types.html#diaspora-id
    """
    return re.match(r"[a-z0-9\-_.]+@[^@/]+\.[^@/]+", handle, flags=re.IGNORECASE) is not None


def with_slash(url):
    if url.endswith('/'):
        return url
    return f"{url}/"

if __name__ == "__main__":
    isT = True
    test_cases = dict()
    try:
        test_cases['test1'] = process_text_links('https://example.org example.org\nhttp://example.org') == \
               '<a href="https://example.org" rel="nofollow" target="_blank">https://example.org</a> ' \
               '<a href="http://example.org" rel="nofollow" target="_blank">example.org</a>\n' \
               '<a href="http://example.org" rel="nofollow" target="_blank">http://example.org</a>'
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    try:
        test_cases['test2'] = process_text_links('<a href="https://example.org">https://example.org</a>') == \
               '<a href="https://example.org" rel="nofollow" target="_blank">https://example.org</a>'
    except Exception as error:
        test_cases['test2'] = type(error).__name__
    try:




        test_cases['test3'] = process_text_links('<code>https://example.org</code><code>\nhttps://example.org\n</code>') == \
               '<code>https://example.org</code><code>\nhttps://example.org\n</code>'

    except Exception as error:
        test_cases['test3'] = type(error).__name__
    try:

        test_cases['test4'] = process_text_links('foo@example.org') == 'foo@example.org'

    except Exception as error:
        test_cases['test4'] = type(error).__name__
    try:

        test_cases['test5'] = process_text_links('<a href="/streams/tag/foobar">#foobar</a>') == \
               '<a href="/streams/tag/foobar">#foobar</a>'
    except Exception as error:
        test_cases['test5'] = type(error).__name__
    try:


        test_cases['test6'] = process_text_links(
            '<p><span class="h-card"><a class="u-url mention" href="https://dev.jasonrobinson.me/u/jaywink/">'
            '@<span>jaywink</span></a></span> boom</p>') == \
               '<p><span class="h-card"><a class="u-url mention" href="https://dev.jasonrobinson.me/u/jaywink/" ' \
               'rel="nofollow" target="_blank">@<span>jaywink</span></a></span> boom</p>'
    except Exception as error:
        test_cases['test6'] = type(error).__name__
    print(test_cases)





