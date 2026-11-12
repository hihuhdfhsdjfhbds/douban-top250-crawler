"""解析层单测：用本地 HTML 样本，不依赖网络。"""

from scraper.parser import parse_books

SAMPLE_HTML = """
<table>
  <tr class="item">
    <td><div class="pic"><em>1</em></div></td>
    <td>
      <div class="pl2"><a href="#">活着</a></div>
      <p class="pl">余华 / 作家出版社 / 2012-8 / 20.00元</p>
      <span class="rating_nums">9.4</span>
      <span class="inq">活着本身就是意义。</span>
    </td>
  </tr>
</table>
"""


def test_parse_single_book():
    items = parse_books(SAMPLE_HTML)
    assert len(items) == 1
    assert items[0]["rank"] == "1"
    assert items[0]["title"] == "活着"
    assert items[0]["rating"] == "9.4"
    assert items[0]["quote"] == "活着本身就是意义。"


def test_parse_empty_html():
    assert parse_books("<table></table>") == []