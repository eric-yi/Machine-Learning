import urllib2
import unittest
import sys, os

_debug = True
#_debug = False

tieba_dir = './baidu_tieba/'
not_found_size = 9 * 1024

def debug(*values):
  if _debug:
    log('debug', *values)

def info(*values):
  log('info', *values)

def log(level, *values):
  message = '[%s]' % level
  for value in values:
    message += '\t%s' % str(value)
  print message

def head(suffix):
    debug('===============' + suffix + ' start===============')

def tail(suffix):
    debug('===============' + suffix + ' end===============')

def run():
    start = 4000000000
    size = 10000000
    end = start + size
    ids = gen_ids(start, end, size)
    for id in ids:
        fetch_baidu_tieba(id)

def gen_id(start, end):
    import random
    return random.randrange(start, end)

def gen_ids(start, end, size):
    ids = []
    while len(ids) < size:
        id = gen_id(start, end)
        if id not in ids:
            ids.append(id)

    return ids

def fetch_page(url):
    import urllib
    head('fetch_page')
    rep = urllib.urlopen(url)
    html = rep.read()
    #debug(html)
    tail('fetch_page')
    return html

def fetch_baidu_tieba(id):
    head('fetch_page')
    url_suffix = 'http://tieba.baidu.com/p/'
    url = url_suffix + str(id)
    html = fetch_page(url)
    save_badidu_tieba(id, html)
    #debug('fetch ' + str(id) + ':' + html)
    tail('fetch_page')
    return html

def save_badidu_tieba(id, html):
    head('save_badidu_tieba')
    if not os.path.exists(tieba_dir):
        os.mkdir(tieba_dir)
    filename = tieba_dir+str(id) + '.html'
    f = open(filename, 'w')
    f.write(html)
    f.close()
    b = os.path.getsize(filename)
    debug('fetch ' + str(id) + ' size: ' + str(b))
    if b < not_found_size:
        debug(str(id) + ' has been removed')
        os.remove(filename)
    tail('save_badidu_tieba')

from lxml import html
from lxml import etree

def parse_html_with_lxml(content):
    tree = html.fromstring(content)
    return tree

# feature map, key: recurse name
# fetch all attributes and texts
def make_feature_list(html_tree):
    feature_map = {}
    feature_map['key'] = 'value'
    # TODO: codes in here

    return feature_map

def test():
    NoArgsTestProgram()

class TestCase(unittest.TestCase):
    @unittest.skip('1')
    def test_fetch_baidu_tieba_4482638959(self):
        html = fetch_baidu_tieba(4482638959)
        self.assertTrue(html is not None)

    @unittest.skip('1')
    def test_fetch_baidu_tieba_100_pages(self):
        start = 4482638959
        end = start + 1000
        size = 100
        ids = gen_ids(start, end, size)
        for id in ids:
            html = fetch_baidu_tieba(id)

    @unittest.skip('1')
    def test_gen_ids_start400000000_size100(self):
        start = 4482638959
        end = start + 1000
        size = 100
        ids = gen_ids(start, end, size)
        self.assertEqual(len(ids), 100)

    @unittest.skip('1')
    def test_parse_baidu_tieba_4482638959(self):
        content = fetch_baidu_tieba(4482639885)
        tree = parse_html_with_lxml(content)
        e = tree.xpath('/html')
        body = tree.xpath('/html/body')
        charset = tree.xpath('//html/head/meta[@charset]')
        for ch in charset:
            debug(etree.tostring(ch))
        title = tree.xpath('/html/head/title')
        #debug('title: ' + title.text)
        if title:
            debug('title: ' + title[0].text.encode('utf-8'))
        self.assertTrue(body)
        self.assertTrue(head)
        self.assertEqual(e[0].tag, 'html')
        div = tree.xpath('//div[@id=\'post_content_87668484593\']')
        self.assertTrue(len(div) == 1)
      #  for d in div:
      #      debug(etree.tostring(d))
      #      debug(d.text_content().encode('utf-8'))

    @unittest.skip('1')
    def test_baidu_tieba_4482638959_notfound(self):
        b = os.path.getsize(tieba_dir+str(4482638959) + '.html')
        debug('file size:' + str(b) + ' and not found size: ' + str(not_found_size))
        self.assertTrue(b < not_found_size)

    @unittest.skip('1')
    def test_baidu_tieba_4482638980_notfound(self):
        b = os.path.getsize(tieba_dir+str(4482638980) + '.html')
        debug('file size:' + str(b) + ' and not found size: ' + str(not_found_size))
        self.assertTrue(b > not_found_size)

    @unittest.skip('1')
    def test_baidu_tieba_dir_available_html(self):
        for f in os.listdir(tieba_dir):
            debug('tieba avaailable f: ' + f)
            b = os.path.getsize(tieba_dir + f)
            self.assertTrue(b > not_found_size)

    #@unittest.skip('1')
    def test_make_feature_list(self):
        content = fetch_baidu_tieba(4482639885)
        tree = parse_html_with_lxml(content)
        feature_map = make_feature_list(tree)
        self.assertTrue(feature_map)

class NoArgsTestProgram(unittest.TestProgram):
    def parseArgs(self, argv):
        self.testNames = None
        self.createTests()

def main():
    option = 'run'
    if len(sys.argv) > 1:
        option = sys.argv[1]

    if 'test' in option:
        test()
    else:
        run()


if __name__ == '__main__':
    info('web spider')
    main()

