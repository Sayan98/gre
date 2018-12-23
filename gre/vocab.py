#!/usr/bin/env python3

from tinydb import TinyDB, Query

class Vocab:
    def __init__(self, debug=False):
        self.debug = debug
        self.db = TinyDB("gre_vocab.json")

    def add(self, words):
        for word in words:
            self.add_word(word)

    def remove(self, words):
        for word in words:
            self.remove_word(word)

    def show(self):
        for doc in self.db.all():
            print(doc["word"])

    def add_word(self, word):
        definition = self.__get_definition(word)
        data = {
        "word": word,
        "definition": definition
        }

        assert isinstance(word, str)
        assert isinstance(definition, str)

        self.db.insert(data)

    def __get_definition(self, word):
        return "<placeholder>"

    def remove_word(self, word):
        assert isinstance(word, str)

        query = Query()
        result = self.db.get(query.word == word)

        try:
            doc_id = result.doc_id
            self.db.remove(doc_ids=[doc_id])
        except AttributeError as e:
            print(f"Error removing {word}")

    def get(self, word):
        assert isinstance(word, str)

        query = Query()
        results = self.db.search(query.word == word)

        if len(results) != 0:
            for doc in results:
                print(doc["word"])
