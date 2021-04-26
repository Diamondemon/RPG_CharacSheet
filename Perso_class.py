from typing import Union


class Competence(object):
    """ Competence of a character """

    def __init__(self, categ="", subcateg="", name="", effect=""):
        object.__init__(self)
        self.categ = categ
        self.subcateg = subcateg
        self.name = name
        self.effect = effect

    def copy(self):
        """
        Method called to create a duplicate of the instance

        :return: the duplicate instance
        """
        new_comp = Competence()
        new_comp.__dict__ = self.__dict__.copy()
        return new_comp

    def get_attr(self, key=""):
        """
        Getter for all attributes

        :param key: string reprensenting the name of the attribute to get
        :return: the value of the attributes
        """
        if key in self.__dict__.keys():
            return self.__dict__[key]

    def modify(self, name="", effect=""):
        """
        Method called to modify the whole description and name of the competence

        :param name: new name to set
        :param effect: new effect to set
        :return: None
        """
        self.name = name
        self.effect = effect

    def __str__(self):
        """
        Method called when printing an instance

        :return: string representing the instance
        """
        return "Compétence (catégorie {}) {} : {}".format(self.categ, self.name, self.effect)


class Player(object):
    """ Class for the player's character """

    def __init__(self, name="Joueur", basexp=0, mage=False):
        self.name = name
        self.xp = basexp
        self.totalxp = basexp
        self.mage = mage
        self.playerstats = {}
        self.basestats = {}
        self.secondstats = {}
        self.thirdstats = {}
        self.passivestats = {}
        self.competences = []
        self.percentages = {}
        self.GMstats = {}
        self.inventory = {}
        self.spells = {}

        self.basestats["hands"] = [0, 200]  # playerstats["stat"]=[actuel,max]
        self.basestats["light"] = [0, 200]
        self.basestats["medium"] = [0, 200]
        self.basestats["heavy"] = [0, 200]
        self.basestats["throw"] = [0, 200]
        self.basestats["shield"] = [0, 200]

        self.basestats["armor"] = [0, 200]

        self.basestats["training"] = [0, 200]
        self.basestats["dexterity"] = [0, 200]  # dextérité et habileté
        self.basestats["mobility"] = [0, 200]

        self.basestats["perception"] = [0, 200]  # perception et analyse
        self.basestats["stealth"] = [0, 200]
        self.basestats["reflex"] = [0, 200]
        self.basestats["wit"] = [0, 200]  # intelligence et connaissances
        self.basestats["mental-res"] = [0, 200]

        self.basestats["charisma"] = [0, 200]
        self.basestats["trading"] = [0, 200]
        self.basestats["luck"] = [0, 200]

        self.basestats["power"] = [0, 200]
        self.basestats["mastery"] = [0, 200]
        self.basestats["sensitivity"] = [0, 200]

        self.secondstats["symb-mastery"] = {"hands": 0, "light": 0, "medium": 0, "heavy": 0, "throw": 0}
        self.secondstats["symb-parry"] = 0

        self.secondstats["symb-armor"] = 0
        self.secondstats["armor-level"] = 0

        self.secondstats["symb-strength"] = [0, 5, 0]  # force [actuel,max,suppléments]
        self.secondstats["symb-ability"] = [0, 0]
        self.secondstats["symb-mobility"] = 0

        self.secondstats["symb-perception"] = 0
        self.secondstats["symb-stealth"] = [0, 0, 0]  # ps-T furtif, T furtif,
        self.secondstats["symb-init"] = 0
        self.secondstats["symb-T"] = 0
        self.secondstats["symb-ps_T"] = [0, 0, 0]  # ps-T reflex, T reflex, ps-T habileté
        self.secondstats["symb-S"] = 0

        self.secondstats["symb-light"] = 0
        self.secondstats["symb-mental"] = 0

        self.secondstats["symb-luck"] = 0
        self.secondstats["symb-charisma"] = 0
        self.secondstats["symb-trading"] = 0

        self.secondstats["symb-lightning"] = 0
        self.secondstats["symb-sensi"] = 0
        self.secondstats["symb-aura"] = 0
        self.secondstats["aura"] = [0, 200]

        self.thirdstats["phys-res"] = [0, 200]
        self.thirdstats["sight"] = 0
        self.thirdstats["hearing"] = 0
        self.thirdstats["smelling"] = 0
        self.thirdstats["silence"] = {"ground": 0, "moving": 0, "assassination": 0}
        self.thirdstats["hiding"] = {"shadow": 0, "not-moving": 0, "identity": 0}
        self.thirdstats["camo"] = {"smell": 0, "disguise": 0, "nature-field": 0}
        self.thirdstats["clue"] = {"intention": 0, "thing-info": 0, "bestiary": 0}
        self.thirdstats["field"] = {"trap": 0, "find": 0, "tracking": 0}
        self.thirdstats["ambush"] = {"ennemies": 0, "threat": 0, "curse": 0}
        self.thirdstats["hidden_action"] = {"thievery": 0, "ambush": 0, "escape": 0}
        self.thirdstats["invested_armor"] = {"Heaume": 0, "Spallières": 0, "Brassards": 0, "Avant-bras": 0,
                                             "Plastron": 0, "Jointures": 0, "Tassette": 0, "Cuissots": 0, "Grèves": 0,
                                             "Solerets": 0}

        self.playerstats["first_expertise"] = [0, 200]
        self.playerstats["RandD_expertise"] = [0, 200]
        self.playerstats["lux_expertise"] = [0, 200]
        self.playerstats["manufactured_expertise"] = [0, 200]

        self.passivestats["legal"] = [0, -50, 50]  # [actuel,min,max]
        self.passivestats["hope"] = [0, 0, 100]  # [actuel,min,max]
        self.passivestats["confidence"] = [0, -20, 20]  # [actuel,min,max]
        self.passivestats["anger"] = [0, -20, 20]  # [actuel,min,max]
        self.passivestats["stress"] = [0, -10, 5]  # [actuel,min,max]
        self.passivestats["fear"] = [0, 0, 25]  # [actuel,min,max]

        self.percentages["hands"] = 0
        self.percentages["light"] = 0
        self.percentages["medium"] = 0
        self.percentages["heavy"] = 0
        self.percentages["throw"] = 0
        self.percentages["shield"] = 0
        self.percentages["phys-res"] = 0
        self.percentages["dexterity"] = 0
        self.percentages["mobility"] = 0
        self.percentages["perception"] = 0
        self.percentages["stealth"] = 0
        self.percentages["mental-res"] = 0
        self.percentages["charisma"] = 0
        self.percentages["trading"] = 0
        self.percentages["spell"] = 0
        self.percentages["magical-perception"] = 0

        self.playerequipment: dict[str, Union[ArmorEquip, MeleeEquip, ThrowEquip]] = {
            "Heaume": None,
            "Spallières": None, "Brassards": None, "Avant-bras": None,
            "Plastron": None, "Jointures": None, "Tassette": None, "Cuissots": None, "Grèves": None,
            "Solerets": None, "left_melee": None, "right_melee": None, "left_throw": None,
            "right_throw": None}

        for key in self.secondstats.keys():
            if type(self.secondstats[key]) != dict and key != "aura" and key != "armor-level" and key != "symb-ps_T":
                self.GMstats[key] = 0
            elif type(self.secondstats[key]) == dict:
                for kkey in self.secondstats[key].keys():
                    self.GMstats[kkey] = 0

        for key in self.thirdstats.keys():
            if type(self.thirdstats[key]) != dict:
                self.GMstats[key] = 0
            elif key != "invested_armor":
                for kkey in self.thirdstats[key].keys():
                    self.GMstats[kkey] = 0

    def calculate(self, stat):
        """
        Method called to recalculate the values of tier 2 stats after modifying tier 1 stats

        :param stat: tier 1 stat that has been modified
        :return: None
        """

        if stat in ["hands", "light", "medium", "heavy", "throw", "shield", "training"]:
            possible_strength = self.basestats["hands"][0] // 5 + self.basestats["light"][0] // 10 + \
                                self.basestats["medium"][0] // 10 + self.basestats["heavy"][0] // 10 + \
                                self.basestats["throw"][0] // 10 + self.basestats["shield"][0] // 10
            possible_strength += min(10, self.basestats["training"][0] // 2) + min(10, max(0, self.basestats[
                "training"][0] - 40) // 2) + min(10, max(0, self.basestats["training"][0] - 80) // 2) + \
                min(10, max(0, self.basestats["training"][0] - 120) // 2) + min(10, max(0, self.basestats[
                    "training"][0] - 160) // 2)
            possible_strength += 5 * (
                        (self.basestats["training"][0] >= 30) + (self.basestats["training"][0] >= 70) + 2 * (
                            self.basestats["training"][0] >= 110) + 2 * (self.basestats["training"][0] >= 150))
            possible_strength -= self.thirdstats["phys-res"][0]
            self.secondstats["symb-strength"][0] = min(possible_strength, self.secondstats["symb-strength"][1])
            self.secondstats["symb-strength"][2] = max(0, possible_strength - self.secondstats["symb-strength"][1])

            if stat not in ["shield", "training"]:
                self.secondstats["symb-mastery"][stat] = 5 * (
                            (self.basestats[stat][0] >= 90) + (self.basestats[stat][0] >= 110) + (
                                self.basestats[stat][0] >= 160) + (self.basestats[stat][0] >= 170))
                self.secondstats["symb-mastery"][stat] += self.GMstats[stat]

            elif stat == "shield":
                self.secondstats["symb-parry"] = 5 * (
                            (self.basestats[stat][0] >= 60) + (self.basestats[stat][0] >= 90) + (
                                self.basestats[stat][0] >= 110) + (self.basestats[stat][0] >= 160) + (
                                        self.basestats[stat][0] >= 170))
                self.secondstats["symb-parry"] += self.GMstats["symb-parry"]

        elif stat == "phys-res":
            self.secondstats["symb-strength"][1] = 5 + 5 * min(4, self.thirdstats[stat][0] // 20) + 5 * \
                                                   min(4, max(0, self.thirdstats[stat][0] - 90) // 20)

            possible_strength = self.secondstats["symb-strength"][0] + self.secondstats["symb-strength"][2] + \
                self.GMstats["symb-strength"]
            self.secondstats["symb-strength"][0] = min(possible_strength, self.secondstats["symb-strength"][1])
            self.secondstats["symb-strength"][2] = max(0, possible_strength - self.secondstats["symb-strength"][1])

        elif stat == "armor":
            # symbole d'armure
            self.secondstats["symb-armor"] = 5 * ((self.basestats[stat][0] >= 40) + (self.basestats[stat][0] >= 60) + (
                        self.basestats[stat][0] >= 70) + (self.basestats[stat][0] >= 110) + (
                                                              self.basestats[stat][0] >= 120) + (
                                                              self.basestats[stat][0] >= 130) + (
                                                              self.basestats[stat][0] >= 170))
            self.secondstats["symb-armor"] += self.GMstats["symb-armor"]
            for i in self.thirdstats["invested_armor"].values():
                self.secondstats["symb-armor"] -= i
            # niveau d'armure
            self.secondstats["armor-level"] = ((self.basestats[stat][0] >= 10) + (self.basestats[stat][0] >= 20) + (
                        self.basestats[stat][0] >= 30) + (self.basestats[stat][0] >= 50) + (
                                                           self.basestats[stat][0] >= 80) + (
                                                           self.basestats[stat][0] >= 100) + (
                                                           self.basestats[stat][0] >= 150) + (
                                                           self.basestats[stat][0] >= 180))

        elif stat == "dexterity":
            # symbole
            self.secondstats["symb-ability"][0] = min(30, self.basestats[stat][0] // 2) + min(10, max(0, self.basestats[
                stat][0] - 60) // 4) + min(8, max(0, self.basestats[stat][0] - 100) // 5) + \
                                                  min(10, max(0, self.basestats[stat][0] - 140) // 4)
            self.secondstats["symb-ability"][0] += (
                        (self.basestats[stat][0] >= 90) + (self.basestats[stat][0] >= 110) + (
                            self.basestats[stat][0] >= 120) + (self.basestats[stat][0] >= 140) + (
                                    self.basestats[stat][0] >= 150) + (self.basestats[stat][0] >= 160) + (
                                    self.basestats[stat][0] >= 170))
            self.secondstats["symb-ability"][0] += self.secondstats["symb-ability"][1]
            self.secondstats["symb-ability"][0] += self.GMstats["symb-ability"]
            self.secondstats["symb-ability"][0] -= self.secondstats["symb-ps_T"][2]

        elif stat == "mobility":
            # symbole
            self.secondstats["symb-mobility"] = min(4, self.basestats[stat][0] // 5) + min(10, max(0, self.basestats[
                stat][0] - 30) // 5) + min(5, max(0, self.basestats[stat][0] - 80) // 4) + min(7, max(0, self.basestats[
                    stat][0] - 105) // 5) + min(5, max(0, self.basestats[stat][0] - 160) // 4)

            self.secondstats["symb-mobility"] += 5 * (
                        (self.basestats[stat][0] >= 30) + (self.basestats[stat][0] >= 90) + (
                            self.basestats[stat][0] >= 105) + (self.basestats[stat][0] >= 120) + (
                                    self.basestats[stat][0] >= 145) + (self.basestats[stat][0] >= 150))
            self.secondstats["symb-mobility"] += self.GMstats["symb-mobility"]

        elif stat == "perception":
            # symbole
            self.secondstats["symb-perception"] = 5 * (
                        (self.basestats[stat][0] >= 30) + (self.basestats[stat][0] >= 40) + (
                            self.basestats[stat][0] >= 60) + (self.basestats[stat][0] >= 70) + (
                                    self.basestats[stat][0] >= 80) + (self.basestats[stat][0] >= 115) + (
                                    self.basestats[stat][0] >= 125) + 2 * (self.basestats[stat][0] >= 180) + 3 * (
                                    self.basestats[stat][0] >= 190))
            for key in ["clue", "field", "ambush"]:
                for stats in self.thirdstats[key].keys():
                    self.secondstats["symb-perception"] -= self.thirdstats[key][stats]

            # symbole S
            self.secondstats["symb-S"] = 5 * ((self.basestats[stat][0] >= 25) + (self.basestats[stat][0] >= 65) + (
                        self.basestats[stat][0] >= 75) + (self.basestats[stat][0] >= 85) + (
                                                          self.basestats[stat][0] >= 90) + (
                                                          self.basestats[stat][0] >= 105) + (
                                                          self.basestats[stat][0] >= 160) + (
                                                          self.basestats[stat][0] >= 170))
            self.secondstats["symb-S"] += self.basestats[stat][0] // 5
            self.secondstats["symb-S"] += 5 * (
                        (self.basestats["sensitivity"][0] >= 90) + (self.basestats["sensitivity"][0] >= 110) + (
                            self.basestats["sensitivity"][0] >= 160) + (self.basestats["sensitivity"][0] >= 170))
            self.secondstats["symb-S"] += self.GMstats["symb-S"]
            self.secondstats["symb-S"] -= (
                        self.thirdstats["sight"] + self.thirdstats["hearing"] + self.thirdstats["smelling"])

        elif stat in ["reflex", "stealth"]:
            # symbole T
            # on retire ce qui a été consommé (T et S), + la magie, +les autres carac
            self.secondstats["symb-T"] = 5 * (
                        (self.basestats["reflex"][0] >= 90) + (self.basestats["reflex"][0] >= 110) + (
                            self.basestats["reflex"][0] >= 160) + (self.basestats["reflex"][0] >= 170))
            self.secondstats["symb-T"] += (5 * (
                        (self.basestats["stealth"][0] >= 25) + (self.basestats["stealth"][0] >= 65) + (
                            self.basestats["stealth"][0] >= 75) + (self.basestats["stealth"][0] >= 85) + (
                                    self.basestats["stealth"][0] >= 90) + (self.basestats["stealth"][0] >= 105) + (
                                    self.basestats["stealth"][0] >= 160) + (self.basestats["stealth"][0] >= 170)))
            self.secondstats["symb-T"] += self.GMstats["symb-T"]
            self.secondstats["symb-T"] -= (self.secondstats["symb-ps_T"][1] + self.secondstats["symb-stealth"][2])

            if stat == "stealth":
                self.secondstats["symb-stealth"][0] = 5 * (
                            (self.basestats[stat][0] >= 30) + (self.basestats[stat][0] >= 40) + (
                                self.basestats[stat][0] >= 60) + (self.basestats[stat][0] >= 70) + (
                                        self.basestats[stat][0] >= 80) + (self.basestats[stat][0] >= 115) + (
                                        self.basestats[stat][0] >= 125) + 2 * (self.basestats[stat][0] >= 180) + 3 * (
                                        self.basestats[stat][0] >= 190))
                self.secondstats["symb-stealth"][0] += self.GMstats["symb-stealth"]
                self.secondstats["symb-stealth"][1] = self.basestats[stat][0] // 10
                self.secondstats["symb-stealth"][1] += self.secondstats["symb-stealth"][2]
                totalstat = 0
                for key in ["hiding", "silence", "camo"]:
                    for stats in self.thirdstats[key].keys():
                        totalstat += self.thirdstats[key][stats]

                self.secondstats["symb-stealth"][0] += min(0, self.secondstats["symb-stealth"][1] - totalstat)
                self.secondstats["symb-stealth"][1] = max(0, self.secondstats["symb-stealth"][1] - totalstat)

            if stat == "reflex":
                self.secondstats["symb-init"] = 5 * (
                            (self.basestats[stat][0] >= 30) + (self.basestats[stat][0] >= 40) + (
                                self.basestats[stat][0] >= 60) + (self.basestats[stat][0] >= 70) + (
                                        self.basestats[stat][0] >= 80) + (self.basestats[stat][0] >= 120) + 2 * (
                                        self.basestats[stat][0] >= 180) + 3 * (self.basestats[stat][0] >= 190))
                self.secondstats["symb-init"] += (min(5, self.basestats[stat][0] // 4) + min(5, max(0, self.basestats[
                    stat][0] - 40) // 4) + min(5, max(0, self.basestats[stat][0] - 130) // 4))
                self.secondstats["symb-init"] += self.GMstats["symb-init"]
                self.secondstats["symb-init"] -= self.secondstats["symb-ability"][1]
                self.secondstats["symb-ps_T"][0] = self.basestats[stat][0] // 5
                self.secondstats["symb-ps_T"][0] += (
                            self.secondstats["symb-ps_T"][1] + self.secondstats["symb-ps_T"][2])

                for stats in self.thirdstats["hidden_action"].keys():
                    self.secondstats["symb-ps_T"][0] -= self.thirdstats["hidden_action"][stats]

        elif stat == "wit":
            # symbole
            self.secondstats["symb-light"] = min(15, max(0, self.basestats[stat][0] - 10) // 2) + \
                                             min(25, max(0, self.basestats[stat][0] - 50) // 2) + \
                                             min(20, max(0, self.basestats[stat][0] - 110) // 2) + \
                                             min(15, max(0, self.basestats[stat][0] - 160) // 2)
            self.secondstats["symb-light"] += self.GMstats["symb-light"]

        elif stat == "mental-res":
            # symbole
            self.secondstats["symb-mental"] = min(20, max(0, self.basestats[stat][0] - 10) // 2) + \
                                              min(10, max(0, self.basestats[stat][0] - 60) // 4) + \
                                              min(10, max(0, self.basestats[stat][0] - 110) // 4) + \
                                              min(8, max(0, self.basestats[stat][0] - 158) // 4)
            self.secondstats["symb-mental"] += self.GMstats["symb-mental"]

        elif stat == "trading":
            # symbole 3 cubes empilés
            self.secondstats["symb-trading"] = min(40, max(0, self.basestats[stat][0] - 10) // 2) + \
                                               min(40, max(10, self.basestats[stat][0] - 100) // 2) + \
                                               min(40, max(15, self.basestats[stat][0] - 130) // 2) + \
                                               min(40, max(10, self.basestats[stat][0] - 160) // 3)
            self.secondstats["symb-trading"] += 10 * (
                        (self.basestats[stat][0] >= 170) + (self.basestats[stat][0] >= 190))
            self.secondstats["symb-trading"] += self.GMstats["symb-trading"]

        elif stat in ["power", "mastery"]:
            # symbole
            self.secondstats["symb-lightning"] = min(10, self.basestats["power"][0] // 2) + \
                                                 min(10, max(0, self.basestats["power"][0] - 20) // 3) + \
                                                 min(25, max(0, self.basestats["power"][0] - 60) // 4)
            self.secondstats["symb-lightning"] += (min(20, self.basestats["mastery"][0]) +
                                                   min(15, max(0, self.basestats["mastery"][0] - 20) // 2) +
                                                   min(40, max(0, self.basestats["power"][0] - 60) // 2) +
                                                   min(10, max(0, self.basestats["power"][0] - 150) // 4))
            self.secondstats["symb-lightning"] += 10 * (
                        (self.basestats["power"][0] >= 170) + 2 * (self.basestats["power"][0] >= 190) + (
                            self.basestats["mastery"][0] >= 90))
            self.secondstats["symb-lightning"] += self.GMstats["symb-lightning"]
            for key in self.spells.keys():
                self.secondstats["symb-lightning"] -= self.spells[key]
            self.upstats("aura")

        elif stat == "sensitivity":
            # symbole
            self.secondstats["symb-sensi"] = 10 * ((self.basestats[stat][0] >= 30) + (self.basestats[stat][0] >= 40) + (
                        self.basestats[stat][0] >= 60) + (self.basestats[stat][0] >= 70) + (
                                                               self.basestats[stat][0] >= 80) + (
                                                               self.basestats[stat][0] >= 100) + (
                                                               self.basestats[stat][0] >= 120) + (
                                                               self.basestats[stat][0] >= 150) + 2 * (
                                                               self.basestats[stat][0] >= 180) + 2 * (
                                                               self.basestats[stat][0] >= 190))
            self.secondstats["symb-sensi"] += self.GMstats["symb-sensi"]

            # symbole S
            self.secondstats["symb-S"] = 5 * ((self.basestats[stat][0] >= 90) + (self.basestats[stat][0] >= 110) + (
                        self.basestats[stat][0] >= 160) + (self.basestats[stat][0] >= 170))
            self.secondstats["symb-S"] += 5 * (
                        (self.basestats["perception"][0] >= 25) + (self.basestats["perception"][0] >= 65) + (
                            self.basestats["perception"][0] >= 75) + (self.basestats["perception"][0] >= 85) + (
                                    self.basestats["perception"][0] >= 90) + (
                                    self.basestats["perception"][0] >= 105) + (
                                    self.basestats["perception"][0] >= 160) + (self.basestats["perception"][0] >= 170))
            self.secondstats["symb-S"] += self.basestats["perception"][0] // 5
            self.secondstats["symb-S"] += self.GMstats["symb-S"]
            self.secondstats["symb-S"] -= (
                        self.thirdstats["sight"] + self.thirdstats["hearing"] + self.thirdstats["smelling"])

        elif stat == "aura":
            # symbole
            self.secondstats["symb-aura"] = min(20, self.secondstats[stat][0]) + min(20, max(0, self.secondstats[stat][
                0] - 20) // 2) + min(20, max(0, self.secondstats[stat][0] - 60) // 4) + min(50, max(0, self.secondstats[
                                                                                                stat][0] - 140))
            self.secondstats["symb-aura"] += 20 * (self.basestats["mastery"][0] >= 90)
            self.secondstats["symb-aura"] += self.GMstats["symb-aura"]

    def calc_perc(self, stat):
        """
        Method called to recalculate the percentages of the character for the dice rolls after modifying a stat

        :param stat: name of the stat that has been modified
        :return: None
        """

        if stat in ["hands", "light", "medium", "heavy", "throw", "shield", "charisma", "trading", "power"]:

            if stat == "power":
                self.percentages["spell"] = min(20, self.basestats[stat][0]) + 5 * (
                            self.basestats[stat][0] >= 50) + min(4, max(0, self.basestats[stat][0] - 130) // 5)
            else:
                self.percentages[stat] = min(20, self.basestats[stat][0]) + 5 * (self.basestats[stat][0] >= 50) + \
                                         min(4, max(0, self.basestats[stat][0] - 130) // 5)

        elif stat in ["mobility", "perception", "stealth", "sensitivity"]:
            self.percentages[stat] = min(20, self.basestats[stat][0]) + min(10, max(0, self.basestats[stat][
                0] - 40) // 2) + min(4, max(0, self.basestats[stat][0] - 130) // 5)

        elif stat == "dexterity":
            self.percentages[stat] = min(10, self.basestats[stat][0] // 2) + min(5, max(0, self.basestats[stat][
                0] - 20) // 4)
            self.percentages[stat] += 5 * ((self.basestats[stat][0] >= 50) + (self.basestats[stat][0] >= 70))

        elif stat == "phys-res":
            self.percentages[stat] = min(20, self.thirdstats[stat][0]) + min(10, max(0, self.thirdstats[stat][
                0] - 30) // 2) + min(5, max(0, self.thirdstats[stat][0] - 80) // 4) + \
                                     min(5, max(0, self.thirdstats[stat][0] - 110) // 4) + \
                                     min(5, max(0, self.thirdstats[stat][0] - 140) // 4)
            self.percentages[stat] += 5 * (self.thirdstats[stat][0] >= 70)

        elif stat == "mental-res":
            self.percentages[stat] = min(20, self.basestats[stat][0]) + \
                                     min(10, max(0, self.basestats[stat][0] - 30) // 2) + \
                                     min(4, max(0, self.basestats[stat][0] - 70) // 5) + \
                                     min(8, max(0, self.basestats[stat][0] - 110) // 5)

    def change_invent_number(self, obj, number):
        """
        Method called to modify the number of a specified item the character possesses

        :param obj: item to modify the quantity of
        :param number: value to modify the quantity
        :return: None
        """
        if self.inventory[obj] + number >= 0:
            self.inventory[obj] += number

    def change_passive(self, stat, number):
        """
        Method to modify the passive statis of the character

        :param stat: stat to modify
        :param number: number to add
        :return: None
        """
        if self.passivestats[stat][1] <= number <= self.passivestats[stat][2]:
            self.passivestats[stat][0] = number

    def clearstats(self):
        """
        Method called to restat the character

        :return: None
        """
        self.secondstats["symb-ability"][1] = 0
        self.secondstats["symb-stealth"][1] = 0
        self.secondstats["symb-stealth"][2] = 0
        self.secondstats["symb-ps_T"][1] = 0
        self.secondstats["symb-ps_T"][2] = 0

        for key in self.thirdstats.keys():
            if type(self.thirdstats[key]) == list:
                self.thirdstats[key][0] = 0

            elif type(self.thirdstats[key]) == dict:
                for kkey in self.thirdstats[key].keys():
                    self.thirdstats[key][kkey] = 0
            else:
                self.thirdstats[key] = 0

        self.calculate("phys-res")

        poplist = []
        for spell in self.spells.keys():
            self.spells[spell] = 0
            poplist.append(spell)

        for spell in poplist:
            self.spells.pop(spell)

        for key in self.basestats:
            self.basestats[key][0] = 0
            self.calculate(key)
            self.calc_perc(key)

        self.xp = self.totalxp

    def compet_add(self, competence):
        """
        Method called to give a new competence to the character

        :param competence: Competence object to add
        :return: None
        """
        self.competences.append(competence)

    def compet_suppr(self, index):
        """
        Method called to remove a competence of the character

        :param index: index of the competence to remove
        :return: None
        """
        self.competences.pop(index)

    def convert_init(self, number):
        """
        Method to convert initiative points into ability points

        :param number: value to convert
        :return: None
        """
        if self.secondstats["symb-init"] - number >= self.secondstats["symb-ability"][1] + number:
            self.secondstats["symb-init"] -= number
            self.secondstats["symb-ability"][1] += number
            self.secondstats["symb-ability"][0] += number

    def equip_obj(self, obj, where=""):
        """
        Method called to equip an item from the inventory
        :param obj: item to equip
        :param where: side of the object if it is a weapon
        :return: None
        """
        if self.inventory[obj]:
            if type(obj) == ArmorEquip:
                self.playerequipment[obj.location] = obj

            elif type(obj) == ThrowEquip:
                if obj.carac["hand"] == 1:
                    if self.playerequipment[where + "_throw"]:
                        if self.playerequipment[where + "_throw"].carac["hand"] == 2:
                            self.playerequipment["left_throw"] = self.playerequipment["right_throw"] = None

                        if self.playerequipment[
                            "right" * (where == "left") + "left" * (where == "right") + "_throw"] == obj and \
                                self.inventory[obj] <= 1:
                            self.playerequipment[
                                "right" * (where == "left") + "left" * (where == "right") + "_throw"] = None

                    else:
                        if self.playerequipment[
                            "right" * (where == "left") + "left" * (where == "right") + "_throw"] == obj and \
                                self.inventory[obj] <= 1:
                            self.playerequipment[
                                "right" * (where == "left") + "left" * (where == "right") + "_throw"] = None

                    self.playerequipment[where + "_throw"] = obj

                else:
                    self.playerequipment["left_throw"] = self.playerequipment["right_throw"] = obj
            else:
                if obj.carac["hand"] == 1:
                    if self.playerequipment[where + "_melee"]:
                        if self.playerequipment[where + "_melee"].carac["hand"] == 2:
                            self.playerequipment["left_melee"] = self.playerequipment["right_melee"] = None

                        if self.playerequipment[
                            "right" * (where == "left") + "left" * (where == "right") + "_melee"] == obj and \
                                self.inventory[obj] <= 1:
                            self.playerequipment["right" * (where == "left") + "left" *
                                                 (where == "right") + "_melee"] = self.playerequipment[where + "_melee"]

                    else:
                        if self.playerequipment[
                            "right" * (where == "left") + "left" * (where == "right") + "_melee"] == obj and \
                                self.inventory[obj] <= 1:
                            self.playerequipment[
                                "right" * (where == "left") + "left" * (where == "right") + "_melee"] = None

                    self.playerequipment[where + "_melee"] = obj
                else:
                    self.playerequipment["left_melee"] = self.playerequipment["right_melee"] = obj

    def get_armor_level(self):
        """
        Method called to get the level of armor threshold

        :return: the level of armor threshold
        """
        return self.secondstats["armor-level"]

    def get_basestats(self):
        """
        Method called to get the tier 1 stats of the character

        :return: dictionnary of the tier 1 stats
        """
        return self.basestats

    def get_competences(self) -> list[Competence]:
        """
        Method called to get the competences of the character

        :return: list of competences
        """
        return self.competences

    def get_current_armor(self, location):
        """
        Method called to get one of the equipped armor pieces

        :param location: where the object is located
        :return: armor piece
        """
        return self.playerequipment[location]

    def get_equipment(self):
        """
        Method called to get the items equipped on the character

        :return: list of equipped items
        """
        return self.playerequipment

    def get_gmstats(self):
        """
        Method called to get the stats given to the character by the GM

        :return: dictionnary of the stats
        """
        return self.GMstats

    def get_inventory(self):
        """
        Method called to get the inventory of the character

        :return: inventory
        """
        return self.inventory

    def get_invested_armor(self, location):
        """
        Method called to get the invested points of armor

        :param location: armor piece location
        :return: corresponding points of armor invested in the requested armor piece location
        """
        return self.thirdstats["invested_armor"][location]

    def get_lightnings(self, spell):
        """
        Method to get the lightnings invested in the specified spell

        :return: number of lightnings invested
        """
        return self.spells[spell]

    def get_name(self):
        """
        Method to get the name of the character

        :return: name of the character
        """
        return self.name

    def get_passivestats(self):
        """
        Method to get the passive stats of the character

        :return: passive stats
        """
        return self.passivestats

    def get_percentages(self):
        """
        Method to get the percentages of the character

        :return: dictionnary of the percentages
        """
        return self.percentages

    def get_secondstats(self):
        """
        Method to get the tier 2 stats

        :return: tier 2 stats
        """
        return self.secondstats

    def get_spelllist(self):
        """
        Method to get the spells of the character

        :return: list of the spells
        """
        return self.spells.keys()

    def get_thirdstats(self):
        """
        Method to get the tier 3 stats

        :return: tier 3 stats
        """
        return self.thirdstats

    def get_weapon(self, side: str, weapontype: str):
        """
        Getter for weapons

        :param weapontype: "melee" or "throw" weapon
        :param side: "left" or "right" hand weapon
        :return: corresponding weapon
        """
        return self.playerequipment[side+"_"+weapontype]

    def GM_gain(self, stat, number):
        """
        Method called to handle the stat points given by the GM

        :param stat: stat to give points into
        :param number: value to give the player
        :return: None
        """
        if number > 0:
            self.GMstats[stat] += number

            if stat in self.secondstats["symb-mastery"].keys():
                self.secondstats["symb-mastery"][stat] += number
            elif stat in self.secondstats.keys() and stat != "symb-strength":
                if type(self.secondstats[stat]) == list:
                    self.secondstats[stat][0] += number
                else:
                    self.secondstats[stat] += number
            elif stat == "symb-strength":
                possible_strength = self.secondstats[stat][0] + self.secondstats[stat][2] + number
                self.secondstats[stat][0] = min(self.secondstats[stat][1], possible_strength)
                self.secondstats[stat][2] = possible_strength - self.secondstats[stat][0]

            elif stat in self.thirdstats.keys():
                if type(self.thirdstats[stat]) == list:
                    self.thirdstats[stat][0] += number
                else:
                    self.thirdstats[stat] += number
            else:
                for key in self.thirdstats.keys():
                    if stat in self.thirdstats[key].keys():
                        self.thirdstats[key][stat] += number

    def GM_clearstats(self):
        """
        Method called to clear the stats given by the GM

        :return: None
        """
        for stat in self.GMstats.keys():

            if stat in self.secondstats["symb-mastery"].keys():
                self.secondstats["symb-mastery"][stat] -= self.GMstats[stat]
            elif stat in self.secondstats.keys() and stat != "symb-strength":
                if type(self.secondstats[stat]) == list:
                    self.secondstats[stat][0] -= self.GMstats[stat]
                else:
                    self.secondstats[stat] -= self.GMstats[stat]
            elif stat == "symb-strength":
                possible_strength = self.secondstats[stat][0] + self.secondstats[stat][2] - self.GMstats[stat]
                self.secondstats[stat][0] = min(self.secondstats[stat][1], possible_strength)
                self.secondstats[stat][2] = possible_strength - self.secondstats[stat][0]

            elif stat in self.thirdstats.keys():
                if type(self.thirdstats[stat]) == list:
                    self.thirdstats[stat][0] -= self.GMstats[stat]
                else:
                    self.thirdstats[stat] -= self.GMstats[stat]
            else:
                for key in self.thirdstats.keys():
                    if stat in self.thirdstats[key].keys():
                        self.thirdstats[key][stat] -= self.GMstats[stat]

            self.GMstats[stat] = 0

    def invent_add(self, obj):
        """
        Method called to add an item to the character's inventory

        :param obj: item to add
        :return: None
        """
        self.inventory[obj] = 1

    def invent_suppr(self, obj):
        """
        Method called to delete the specified item from the inventory

        :param obj: item to remove
        :return: None
        """
        self.inventory.pop(obj)

    def ismage(self):
        """
        Method called to know if the character is a mage

        :return: boolean indicating if it is a mage
        """
        return self.mage

    def spell_add(self, spell):
        """
        Method called to give a spell to the character

        :param spell: name of the spell to add
        :return: None
        """
        self.spells[spell] = 0

    def spell_pop(self, spell):
        """
        Method called to remove a spell of the character

        :param spell: name of the spell to remove from the player's set
        :return: None
        """
        if self.spells[spell] > 0:
            self.use_lightning(spell, -self.spells[spell])

        self.spells.pop(spell)

    def unequip_obj(self, obj):
        """
        Method called to unequip an item of the character

        :param obj: object to unequip
        :return: None
        """
        if type(obj) == ArmorEquip:
            self.playerequipment[obj.get_stat("location")] = None
        elif type(obj) == ThrowEquip:
            if obj.carac["hand"] == 2:
                self.playerequipment["left_throw"] = self.playerequipment["right_throw"] = None
            elif self.playerequipment["left_throw"] == obj:
                self.playerequipment["left_throw"] = None
            elif self.playerequipment["right_throw"] == obj:
                self.playerequipment["right_throw"] = None
        else:
            if obj.carac["hand"] == 2:
                self.playerequipment["left_melee"] = self.playerequipment["right_melee"] = None
            elif self.playerequipment["left_melee"] == obj:
                self.playerequipment["left_melee"] = None
            elif self.playerequipment["right_melee"] == obj:
                self.playerequipment["right_melee"] = None

    def upstats(self, stat: str, number: int = 0, location: str = None):
        """
        Method called to consume experience points and increase a tier 1 stat, or consume a tier 2 stat to increase tier
        a 3 stat

        :param stat: name of the stat to increase
        :param number: value to increase the stat by
        :param location: to invest armor symbols
        :return: None
        """

        if stat in self.basestats.keys() and number <= self.xp:
            if (self.basestats[stat][0] + number <= self.basestats[stat][1]) and (
                    self.basestats[stat][0] + number >= 0):
                self.basestats[stat][0] += number
                self.xp -= number

        elif stat == "phys-res" and number <= (
                self.secondstats["symb-strength"][2] + self.secondstats["symb-strength"][0]):
            if (self.thirdstats[stat][0] + number <= self.thirdstats[stat][1]) and (
                    self.thirdstats[stat][0] + number >= 0):
                self.thirdstats[stat][0] += number
                self.secondstats["symb-strength"][2] -= number
                if self.secondstats["symb-strength"][2] < 0:
                    self.secondstats["symb-strength"][0] += self.secondstats["symb-strength"][2]
                    self.secondstats["symb-strength"][2] = 0

        elif stat == "aura":
            self.secondstats["aura"][0] = self.basestats["power"][0] // 2 + self.basestats["mastery"][0] // 2

        elif stat == "invested_armor":
            if number <= self.secondstats["symb-armor"]:
                self.secondstats["symb-armor"] -= number
                self.thirdstats[stat][location] += number

        elif stat in ["sight", "hearing", "smelling"]:
            if number <= self.secondstats["symb-S"]:
                self.thirdstats[stat] += number
                self.secondstats["symb-S"] -= number

        # Pour ce tier 3, "number" sera probablement égal à 1
        elif stat in self.thirdstats["silence"].keys():
            if self.secondstats["symb-stealth"][0] + self.secondstats["symb-stealth"][1] + self.secondstats[
                    "symb-T"] >= number:
                if self.secondstats["symb-stealth"][1] > 0:
                    self.secondstats["symb-stealth"][1] -= number
                    self.thirdstats["silence"][stat] += number

                elif self.secondstats["symb-stealth"][0] > 0:
                    self.secondstats["symb-stealth"][0] -= number
                    self.thirdstats["silence"][stat] += number

                else:
                    self.secondstats["symb-stealth"][2] += number
                    self.secondstats["symb-T"] -= number
                    self.thirdstats["silence"][stat] += number

        elif stat in self.thirdstats["hiding"].keys():
            if self.secondstats["symb-stealth"][0] + self.secondstats["symb-stealth"][1] + self.secondstats[
                    "symb-T"] >= number:
                if self.secondstats["symb-stealth"][1] > 0:
                    self.secondstats["symb-stealth"][1] -= number
                    self.thirdstats["hiding"][stat] += number

                elif self.secondstats["symb-stealth"][0] > 0:
                    self.secondstats["symb-stealth"][0] -= number
                    self.thirdstats["hiding"][stat] += number

                else:
                    self.secondstats["symb-stealth"][2] += number
                    self.secondstats["symb-T"] -= number
                    self.thirdstats["hiding"][stat] += number

        elif stat in self.thirdstats["camo"].keys():
            if self.secondstats["symb-stealth"][0] + self.secondstats["symb-stealth"][1] + self.secondstats[
                    "symb-T"] >= number:
                if self.secondstats["symb-stealth"][1] > 0:
                    self.secondstats["symb-stealth"][1] -= number
                    self.thirdstats["camo"][stat] += number

                elif self.secondstats["symb-stealth"][0] > 0:
                    self.secondstats["symb-stealth"][0] -= number
                    self.thirdstats["camo"][stat] += number

                else:
                    self.secondstats["symb-stealth"][2] += number
                    self.secondstats["symb-T"] -= number
                    self.thirdstats["camo"][stat] += number

        elif stat in self.thirdstats["clue"].keys():
            if self.secondstats["symb-perception"] >= number:
                self.secondstats["symb-perception"] -= number
                self.thirdstats["clue"][stat] += number

        elif stat in self.thirdstats["field"].keys():
            if self.secondstats["symb-perception"] >= number:
                self.secondstats["symb-perception"] -= number
                self.thirdstats["field"][stat] += number

        elif stat in self.thirdstats["ambush"].keys():
            if self.secondstats["symb-perception"] >= number:
                self.secondstats["symb-perception"] -= number
                self.thirdstats["ambush"][stat] += number

        elif stat in self.thirdstats["hidden_action"].keys():
            if self.secondstats["symb-ability"][0] + self.secondstats["symb-ps_T"][0] + self.secondstats[
                    "symb-T"] >= number:
                if self.secondstats["symb-ps_T"][0] > 0:
                    self.secondstats["symb-ps_T"][0] -= number
                    self.thirdstats["hidden_action"][stat] += number

                elif self.secondstats["symb-T"] > 0:
                    self.secondstats["symb-T"] -= number
                    self.secondstats["symb-ps_T"][1] += number
                    self.thirdstats["hidden_action"][stat] += number

                else:
                    self.secondstats["symb-ps_T"][2] += number
                    self.secondstats["symb-ability"][0] -= number
                    self.thirdstats["hidden_action"][stat] += number

        self.calculate(stat)
        self.calc_perc(stat)

    def upxp(self, number):
        """
        Method to give experience points to the character

        :param number: value to add
        :return: None
        """
        if self.xp + number >= 0:
            self.xp = self.xp + number
            self.totalxp = self.totalxp + number

    def use_lightning(self, spell, number):
        """
        Method called to attribute lightnings to the specified spell

        :param spell: spell to inest lightnings into
        :param number: value to invest
        :return: None
        """
        if self.spells[spell] + number >= 0 and self.secondstats["symb-lightning"] >= number:
            self.spells[spell] += number
            self.secondstats["symb-lightning"] -= number

    def __setstate__(self, dict_attr):
        """
        Method called when unserializing a character from a file

        :param dict_attr: dictionnary of attributes
        :return: None
        """
        test_char = Player()
        for key in test_char.__dict__.keys():
            if (not (key in dict_attr.keys())) or not isinstance(dict_attr[key], type(test_char.__dict__[key])):
                dict_attr[key] = test_char.__dict__[key]

        poplist = []

        for key in dict_attr.keys():
            if not (key in test_char.__dict__.keys()):
                poplist.append(key)

        for key in poplist:
            dict_attr.pop(key)

        self.__dict__ = dict_attr

    def __str__(self):
        """
        Method called when printing an instance

        :return: string representing the instance
        """
        return "Personnage {}, a accumulé au total {} points d'xp, il lui en reste {} à répartir.".format(
            self.name, self.totalxp, self.xp)


# inventaire


class Obj(object):
    """ Basic Item """

    def __init__(self, name="", description="", stackable=False):
        self.name = name
        self.description = description
        self.is_stackable = stackable

    def copy(self):
        """
        Method called to create a duplicate of the instance

        :return: the duplicate instance
        """
        new_obj = Obj(self.name, self.description, self.is_stackable)

        return new_obj

    def get_stat(self, key):
        """
        Getter for any attribute or stat

        :param key: string representing the attribute or stat to get
        :return: None
        """
        if key in self.__dict__.keys():
            return self.__dict__[key]

    def get_stats_aslist(self, keylist):
        """
        Getter for any list of attributes or stats

        :param keylist: list of strings representing an attribute or stat to get
        :return: None
        """
        valuelist = []

        for key in keylist:
            valuelist.append(self.get_stat(key))

        return valuelist


class Cord(Obj):
    """ String for shooting weapons"""

    def __init__(self, name="", description="", stackable="False", pourcentage=0):
        Obj.__init__(self, name, description, stackable)
        self.perc = pourcentage  # chance de ne pas casser en cas d'échec

    def copy(self):
        """
        Method called to create a duplicate of the instance

        :return: the duplicate instance
        """
        new_cord = Cord(self.name, self.description, self.is_stackable, self.perc)

        return new_cord

    def set_perc(self, newval):
        """
        Setter for the percentage of resistance of the cord to breaking

        :param newval: value of percentage to set
        :return: None
        """
        self.perc = newval


class Equip(Obj):
    """ Abstract class for any equipment """

    def __init__(self, name="", description="", stackable=False):
        Obj.__init__(self, name, description, stackable)
        self.carac = {}

    def get_stat(self, key):
        """
        Getter for any attribute or stat

        :param key: string representing the attribute or stat to get
        :return: None
        """

        if key in self.carac.keys():
            return self.carac[key]

        else:
            return Obj.get_stat(self, key)

    def get_stats_aslist(self, keylist):
        """
        Getter for any list of attributes or stats

        :param keylist: list of strings representing an attribute or stat to get
        :return: None
        """
        valuelist = []
        for key in keylist:
            valuelist.append(self.get_stat(key))
        return valuelist

    def upsolid(self, solid):
        """
        Method called to update the item's usury

        :param solid: number to change the usury by
        :return: None
        """
        if self.carac["solid"] + solid >= 0:
            self.carac["solid"] += solid


class ArmorEquip(Equip):
    """ Class for armor equipment items """

    def __init__(self, name="", description="", stackable=False, location=""):
        Equip.__init__(self, name, description, stackable)
        self.location = location
        self.carac["prot"] = 0  # protection, pour les dégats du tranchant
        self.carac["amort"] = 0  # amortissement, pour les dégâts d'armes contondantes
        self.carac["mobi"] = 0  # mobilité offerte par l'armure (influence le jet de dés)
        self.carac["vit"] = 0  # ralentissement créé par l'armure
        self.carac["solid"] = 0  # solidité restante de l'objet

    def copy(self):
        """
        Method called to create a duplicate of the instance

        :return: the duplicate instance
        """
        new_obj = ArmorEquip(self.name, self.description, self.is_stackable, self.location)
        new_obj.upstats(self.carac["prot"], self.carac["amort"], self.carac["mobi"], self.carac["vit"])
        new_obj.upsolid(self.carac["solid"])

        return new_obj

    def upstats(self, prot, amort, mobi, vit):
        """
        Method called to set the statistics of the weapon

        :param prot: protection given against cutting
        :param amort: protection given against blunt attacks
        :param mobi: effect of the piece of armor on mobility
        :param vit: effect of the piece of armor on the turn speed
        :return: None
        """
        self.carac["prot"] = prot
        self.carac["amort"] = amort
        self.carac["mobi"] = mobi
        self.carac["vit"] = vit


class MeleeEquip(Equip):
    """ Class for melee weapons"""

    def __init__(self, name="", description="", stackable=False, weight="", hast=False):
        """ Whether or not the weapon is a hast weapon, it gives specific bonuses """
        Equip.__init__(self, name, description, stackable)
        self.carac["weight"] = weight  # type d'arme (lourde, légère)
        self.carac["hand"] = 0  # nombre de mains nécessaires à l'utilisation
        self.carac["dgt_tr"] = 0  # dégâts du tranchant
        self.carac["dgt_ctd"] = 0  # dégâts du plat
        self.carac["estoc"] = 0  # dégats en estoc
        self.carac["mastery"] = 0  # maitrise du personnage sur cet objet
        self.carac["quality"] = ""  # qualité de l'équipement (influence la perte de solidité)
        self.carac["solid"] = 0  # solidité restante de l'objet
        self.carac["hast"] = hast  # indique si l'objet bénéficie des règles des armes de hast
        if self.carac["hast"]:
            self.carac["hast_bonus"] = 0
        else:
            self.carac["vit"] = 0

    def copy(self):
        """
        Method called to create a duplicate of the instance

        :return: the duplicate instance
        """
        new_obj = MeleeEquip(self.name, self.description, self.is_stackable, self.carac["weight"], self.carac["hast"])
        if self.is_hast():
            vit = self.carac["hast_bonus"]
        else:
            vit = self.carac["vit"]
        new_obj.upstats(self.carac["hand"], self.carac["dgt_tr"], self.carac["dgt_ctd"], self.carac["estoc"], vit)
        new_obj.upsolid(self.carac["solid"])
        new_obj.newquali(self.carac["quality"])

        return new_obj

    def is_hast(self):
        """
        Method called to know if the weapon is a hast weapon of not

        :return: None
        """
        return self.carac["hast"]

    def newquali(self, quality=""):
        """
        Method called to change the quality of the item

        :param quality: number to apply
        :return: None
        """
        self.carac["quality"] = quality

    def upstats(self, hand, tr, ctd, estoc, vit):
        """
        Method called to set the statistics of the weapon

        :param hand: number of hands needed to use the weapon
        :param tr: cutting damages of the weapon
        :param ctd: blunt damages of the weapon
        :param estoc: pointing damages of the weapon
        :param vit: effect of using the weapon on turn speed
        :return: None
        """
        self.carac["dgt_tr"] = tr
        self.carac["dgt_ctd"] = ctd
        self.carac["estoc"] = estoc
        self.carac["hand"] = hand
        if self.carac["hast"]:
            self.carac["hast_bonus"] = vit
        else:
            self.carac["vit"] = vit

    def upmastery(self, mastery):
        """ Méthode qui permet de modifier la maitrise du personnage avec cette arme """
        if self.carac["mastery"] + mastery >= 0:
            self.carac["mastery"] += mastery


class ThrowEquip(Equip):
    """ Class for throwable and shooting weapons """

    def __init__(self, name="", description="", stackable=False, throw_type="Tir"):
        Equip.__init__(self, name, description, stackable)
        self.carac["type"] = throw_type  # spécifie s'il s'agit d'une arme de lancer ou de tir
        self.carac["hand"] = 0  # nombre de mains nécessaires à l'utilisation
        self.carac["dgt"] = 0  # dégâts infligés
        self.carac["pa"] = 0  # pénétration d'armure
        if self.carac["type"] == "Tir":
            """ Les armes de tir sont équipées de cordes """
            self.carac["cord"] = [0, 0]
        else:
            self.carac["cord"] = None
        self.carac["mastery"] = 0  # maitrise du personnage sur cet objet
        self.carac["solid"] = 0  # solidité restante de l'objet
        self.carac["scope"] = []  # bonus/malus aux dés en fonction de la distance

    def copy(self):
        """
        Method called to create a duplicate of the instance

        :return: the duplicate instance
        """
        new_obj = ThrowEquip()
        new_obj.__dict__ = self.__dict__.copy()
        new_obj.del_cord()
        return new_obj

    def del_cord(self):
        """
        Method called to remove cord objects from the weapon

        :return: None
        """
        if self.carac["cord"]:
            self.carac["cord"] = [0, 0]

    def load_cord(self, obj: Cord):
        """
        Method called to add a string to the weapon (if it is a shooting weapon)

        :param obj: Cord object
        :return: None
        """
        if self.carac["cord"]:  # on vérifie qu'il s'agit d'une arme de tir
            if obj.perc == self.carac["cord"][1] or self.carac["cord"][1] == 0:
                self.carac["cord"][0] += 1
                self.carac["cord"][1] = obj.perc
            else:
                """ Si on passe à une corde de pourcentage différent, on retire les autres """
                self.carac["cord"] = [1, obj.perc]

    def newscope(self, scope):
        """
        Method called to set the table representing the statistics of the weapon in function of the range

        :param scope: list of lists for the scope. A sublist is [max range, speed, accuracy]
        :return:None
        """
        self.carac["scope"] = scope

    def upmastery(self, mastery):
        """
        Method called to modify the characters affinity with this weapon

        :param mastery: number to change the affinity by
        :return: None
        """
        if self.carac["mastery"] + mastery >= 0:
            self.carac["mastery"] += mastery

    def upstats(self, hand, dgt, pa):
        """
        Method called to set the statistics of the weapon

        :param hand: number of hands needed to use the weapon
        :param dgt: damages of the weapon
        :param pa: armor-piercing
        :return: None
        """
        self.carac["hand"] = hand
        self.carac["dgt"] = dgt
        self.carac["pa"] = pa


class ShieldEquip(Equip):
    """ Class for Shield items """

    def __init__(self, name="", description="", stackable=False):
        Equip.__init__(self, name, description, stackable=stackable)
        self.carac["hand"] = 0  # nombre de mains nécessaires à l'utilisation
        self.carac["close"] = 0  # capactié à défendre au corps à corps
        self.carac["dist"] = 0  # capacité à défendre contre les tirs
        self.carac["mastery"] = 0  # maitrise du personnage sur cet objet
        self.carac["mobi"] = 0  # influence du bouclier sur la mobilité
        self.carac["vit"] = 0  # influence du bouclier sur la vitesse
        self.carac["quality"] = ""  # qualité de l'équipement (influence la perte de solidité)
        self.carac["solid"] = 0  # solidité restante de l'objet

    def copy(self):
        """
        Method called to create a duplicate of the instance

        :return: the duplicate instance
        """
        new_obj = ShieldEquip(self.name, self.description, self.is_stackable)
        new_obj.upstats(self.carac["hand"], self.carac["close"], self.carac["dist"], self.carac["mobi"],
                        self.carac["vit"])
        new_obj.upsolid(self.carac["solid"])
        new_obj.newquali(self.carac["quality"])

        return new_obj

    def upmastery(self, mastery):
        """
        Method called to modify the characters affinity with this weapon

        :param mastery: number to change the affinity by
        :return: None
        """
        if self.carac["mastery"] + mastery >= 0:
            self.carac["mastery"] += mastery

    def upstats(self, hand, close, dist, mobi, vit):
        """
        Method called to set the statistics of the weapon

        :param hand: number of hands used to use the weapon
        :param close: defense against physical close-range attacks
        :param dist: defense against physical long-range attacks
        :param mobi: effect of carrying the item on mobility
        :param vit: effect of using the item on turn speed
        :return: None
        """
        self.carac["hand"] = hand
        self.carac["close"] = close
        self.carac["dist"] = dist
        self.carac["mobi"] = mobi
        self.carac["vit"] = vit

    def newquali(self, quality=""):
        """
        Method called to change the quality of the item

        :param quality: number to apply
        :return: None
        """
        self.carac["quality"] = quality


class Spell(object):
    """ Class for spells """

    def __init__(self, elem="", subcateg="", name="", effect="", description="", cost=0):
        object.__init__(self)
        self.elem = elem
        self.subcateg = subcateg
        self.name = name
        self.effect = effect
        self.description = description
        self.cost = cost

    def copy(self):
        """
        Method called to create a duplicate of the instance

        :return: the duplicate instance
        """
        new_spell = Spell()
        new_spell.__dict__ = self.__dict__.copy()
        return new_spell

    def get_stat(self, key):
        """
        Getter for any attribute

        :param key: string representing the attribute to get
        :return: None
        """
        if key in self.__dict__.keys():
            return self.__dict__[key]

    def get_stats_aslist(self, keys):
        """
        Getter for any list of attributes

        :param keys: list of strings representing an attribute to get
        :return: None
        """
        valuelist = []

        for key in keys:
            if key in self.__dict__.keys():
                valuelist.append(self.__dict__[key])

        return valuelist

    def __str__(self):
        """
        Method called when printing an instance

        :return: string representing the instance
        """
        return "Sort (élément {}) {} : {}".format(self.elem, self.name, self.effect)
