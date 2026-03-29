import pytest
from solution import extract_links
def test_1_basic():
    assert extract_links("[Google](https://google.com)") == [{"text": "Google", "url": "https://google.com"}]
def test_2_multiple():
    assert len(extract_links("[A](u1) [B](u2)")) == 2
def test_3_ignore_code():
    assert extract_links("`[Hidden](url)` [Visible](url2)") == [{"text": "Visible", "url": "url2"}]
def test_4_no_links():
    assert extract_links("Plain text") == []
def test_5_malformed():
    assert extract_links("[Broken](url") == []
def test_6_spaces():
    assert extract_links("[Link Text](url)") == [{"text": "Link Text", "url": "url"}]
def test_7_nested():
    text = "Link with [extra] [brackets](https://test.com)"
    result = extract_links(text)
    assert result[0]["text"] == "brackets"
    assert result[0]["url"] == "https://test.com"
def test_8_wiki():
    assert extract_links("[Wiki](https://en.wikipedia.org/wiki/Python)") == [{"text": "Wiki", "url": "https://en.wikipedia.org/wiki/Python"}]
def test_9_image_ignore():
    assert extract_links("![Img](url1) [Link](url2)") == [{"text": "Link", "url": "url2"}]
def test_10_empty_brackets():
    assert extract_links("[](url)") == [] 