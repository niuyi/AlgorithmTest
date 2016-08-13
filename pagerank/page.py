import random


class Page:
    def __init__(self, name):
        self.name = name
        self.pv = 0
        self.pages = []

    def add_pages(self, pages):
        self.pages = pages

    def visit(self):
        self.pv += 1

    def next_page(self):
        random.shuffle(self.pages)
        return self.pages[0]
