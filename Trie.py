# -*- coding: utf-8 -*-

from collections import defaultdict


def here():
    print('PrimeMusic')


class TrieNode(object):
    """
        Trie树上的一个节点
    """
    def __init__(self, char = '', count = 0, depth = 0):
        """
        """
        self.char = char
        self.count = count
        self.depth = depth

        self.isLeaf = False
        self.suffix = None

        self.child = defaultdict(object)


    def insert_child(self, char = '', count = 0, depth = 0):
        """
        """
        self.child[char] = TrieNode(char, count, depth)



class Trie(object):
    """
        Trie树
    """
    def __init__(self):
        """
            初始化根节点
        """
        self.root = TrieNode('')


    def insert_string(self, string = ''):
        """
            向Trie树中增加一个字符串
        """
        node = self.root
        for char in string:
            if not node.child.has_key(char):
                node.insert_child(char, 0, node.depth+1)
            node = node.child[char]
            node.count += 1
        node.isLeaf = True


    def Match(self, N, text, start):
        node = self.root
        first, last = start+1, start+1
        while start<N:
            if node.child.has_key(text[start]):
                node = node.child[text[start]]
                start += 1
                if node.isLeaf: first,last = start-node.depth,start
            else: break
        return (first, last)


    def removeImpurity(self, text):
        pure_text = ''
        start, N = 0, len(text)
        while start<N:
            (first,last) = self.Match(N,text,start)
            pure_text += text[start:first]
            start = last
        return pure_text


    def find_common_prefix(self, node, count = 2, prefix = ''):
        """
            在Trie树上找到出现次数大于等于count的最长公共前缀
        """
        prefix_list = []
        prefix += node.char

        flag = False
        for (char, child_node) in node.child.items():
            if child_node.count >= count:
                flag = True
                child_prefix_list = self.find_common_prefix(child_node, count, prefix)
                prefix_list.extend(child_prefix_list)
        if not flag:
            prefix_list.append(prefix)

        return prefix_list



if __name__ == '__main__':

    trie = Trie()
    trie.insert_string(u'第一章 六安瓜片')
    trie.insert_string(u'一章 北灵院')
    trie.insert_string(u'第一章-1-六安瓜片')
    trie.insert_string(u'第一章 数学之美')
    trie.insert_string(u'第一章-1- 标题是浮云')
    trie.insert_string(u'第一章-1- 北灵院')

    for word in trie.find_common_prefix(trie.root,2,''):
        print word
    #print(trie.find_common_prefix(trie.root, 2, '').encode('utf8', 'ignore'))


    text = u'this is a test第一章 数学之美 !!!'
    print trie.removeImpurity(text)

    here()    
