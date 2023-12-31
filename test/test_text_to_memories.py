from minichain.tools.text_to_memory import text_to_memory
from minichain.utils.markdown_browser import markdown_browser


def test_text_to_memory():
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    text = markdown_browser(url)
    memories = text_to_memory(text, source=url)
    print("titles", "\n".join([i.memory.title for i in memories]))
    print(memories)
