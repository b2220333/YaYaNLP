from yaya.collection.dict import DoubleArrayTrie
from yaya import config
from yaya.utility.singleton import singleton

__author__ = 'tony'


class ChinseTraditionalBaseDict:
    def convert_key_to_value(self, text):
        search = self.trie.search(text)
        wordnet = [None] * search.array_length
        lennet = [0] * search.array_length
        for i, k, v in search.search_all_words():
            if len(v[1]) > lennet[i]:
                wordnet[i] = v[1]
                lennet[i] = len(k)
        offset = 0
        valuetext = []
        while offset < search.array_length:
            if wordnet[offset] is None:
                valuetext.append(search.char_array[offset])
                offset += 1
            else:
                valuetext.append(wordnet[offset])
                offset += lennet[offset]
        return "".join(valuetext)


@singleton
class SimplifiedChineseDict(ChinseTraditionalBaseDict):
    def __init__(self):
        self.trie = DoubleArrayTrie.load(config.TRADITIONAL_CHINESE_DICT_NAME,
                                         lambda i: i[i.find(u'=') + 1:],
                                         lambda i: i.split('=')[::-1],
                                         dict_bin_ext=config.DICT_BIN_REVERSE_EXT)
        self.trie.get_attr = lambda v: v

    def convert_simplified_to_traditional(self, text):
        return self.convert_key_to_value(text)


@singleton
class TraditionalChineseDict(ChinseTraditionalBaseDict):
    def __init__(self):
        self.trie = DoubleArrayTrie.load(config.TRADITIONAL_CHINESE_DICT_NAME,
                                         lambda i: i[:i.find(u'=')],
                                         lambda i: i.split('='))
        self.trie.get_attr = lambda v: v

    def convert_traditional_to_simplified(self, text):
        return self.convert_key_to_value(text)
