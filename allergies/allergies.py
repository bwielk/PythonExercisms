class Allergy(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value

class Allergies(object):

    def __init__(self, score):
        self.score = score
        self.allergens = [  Allergy('eggs', 1),
                            Allergy('peanuts', 2),
                            Allergy('shellfish', 4),
                            Allergy('strawberries', 8),
                            Allergy('tomatoes', 16),
                            Allergy('chocolate', 32),
                            Allergy('pollen', 64),
                            Allergy('cats', 128)
                        ]
        self.allergies = []

    def calculate_allergens(self):
        assigned_score = self.score
        for allergen in reversed(self.allergens):
            if assigned_score >= allergen.value:
                assigned_score -= allergen.value
                self.allergies.append(allergen.name)

    def is_allergic_to(self, item):
        self.calculate_allergens()
        return item in self.allergies

    @property
    def lst(self):
        self.calculate_allergens()
        print(self.allergies)
        return self.allergies
