class Person:

    def __init__(self, name, gender, birth_year, father=None, mother=None):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.__children = []
        self.father = father
        if father:
            self.father.add_child(self)
        self.mother = mother
        if mother:
            self.mother.add_child(self)

    def add_child(self, child):
            self.__children.append(child)

    def children(self, gender=None):
        return [child for child in self.__children
                if (child.gender == gender) or (gender is None)]

    def get_siblings(self, gender):
        if self.father:
            siblings_father = set(self.father.children(gender))
        else:
            siblings_father = set()
        if self.mother:
            siblings_mother = set(self.mother.children(gender))
        else:
            siblings_mother = set()

        siblings = siblings_father.union(siblings_mother)
        return list(siblings - {self})

    def get_brothers(self):
        return self.get_siblings('M')

    def get_sisters(self):
        return self.get_siblings('F')

    def is_direct_successor(self, successor):
        return successor in self.__children
