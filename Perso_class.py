class player(object):

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

        self.playerequipment: dict[str, ArmorEquip] = {"Heaume": None, "Spallières": None, "Brassards": None, "Avant-bras": None,
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

    def upstats(self, stat: str, number: int=0, location: str=None):
        """ Méthode qui permet de consommer des points d'expérience afin d'augmenter les points dans une statistique de tier 1, ou consommer des
        statistiques de Tier 2 pour augmenter celles de Tier 3"""

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
        """ Méthode qui fait gagner des points d'expérience au personnage """
        if self.xp + number >= 0:
            self.xp = self.xp + number
            self.totalxp = self.totalxp + number

    def clearstats(self):
        """ Méthode pour réinitialiser le personnage """
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

    def calculate(self, stat):
        """ Méthode qui calcule les stats de Tier 2 après avoir augmenté celle de Tier 1 """

        if stat in ["hands", "light", "medium", "heavy", "throw", "shield", "training"]:
            possible_strength = self.basestats["hands"][0] // 5 + self.basestats["light"][0] // 10 + \
                                self.basestats["medium"][0] // 10 + self.basestats["heavy"][0] // 10 + \
                                self.basestats["throw"][0] // 10 + self.basestats["shield"][0] // 10
            possible_strength += min(10, self.basestats["training"][0] // 2) + min(10, max(0,
                                                                                           self.basestats["training"][
                                                                                               0] - 40) // 2) + min(10,
                                                                                                                    max(
                                                                                                                        0,
                                                                                                                        self.basestats[
                                                                                                                            "training"][
                                                                                                                            0] - 80) // 2) + min(
                10, max(0, self.basestats["training"][0] - 120) // 2) + min(10, max(0, self.basestats["training"][
                0] - 160) // 2)
            possible_strength += 5 * (
                        (self.basestats["training"][0] >= 30) + (self.basestats["training"][0] >= 70) + 2 * (
                            self.basestats["training"][0] >= 110) + 2 * (self.basestats["training"][0] >= 150))
            possible_strength -= self.thirdstats["phys-res"][0]
            self.secondstats["symb-strength"][0] = min(possible_strength, self.secondstats["symb-strength"][1])
            self.secondstats["symb-strength"][2] = max(0, possible_strength - self.secondstats["symb-strength"][1])

            if not stat in ["shield", "training"]:
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
            self.secondstats["symb-strength"][1] = 5 + 5 * min(4, self.thirdstats[stat][0] // 20) + 5 * min(4, max(0,
                                                                                                                   self.thirdstats[
                                                                                                                       stat][
                                                                                                                       0] - 90) // 20)

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
                stat][0] - 60) // 4) + min(8, max(0, self.basestats[stat][0] - 100) // 5) + min(10, max(0,
                                                                                                        self.basestats[
                                                                                                            stat][
                                                                                                            0] - 140) // 4)
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
            self.secondstats["symb-mobility"] = min(4, self.basestats[stat][0] // 5) + min(10, max(0,
                                                                                                   self.basestats[stat][
                                                                                                       0] - 30) // 5) + min(
                5, max(0, self.basestats[stat][0] - 80) // 4) + min(7,
                                                                    max(0, self.basestats[stat][0] - 105) // 5) + min(5,
                                                                                                                      max(
                                                                                                                          0,
                                                                                                                          self.basestats[
                                                                                                                              stat][
                                                                                                                              0] - 160) // 4)
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
            self.secondstats["symb-T"] = 5 * (
                        (self.basestats["reflex"][0] >= 90) + (self.basestats["reflex"][0] >= 110) + (
                            self.basestats["reflex"][0] >= 160) + (self.basestats["reflex"][
                                                                       0] >= 170))  # - ce qui a été consommé (T et S), + la magie, +les autres carac
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
            self.secondstats["symb-light"] = min(15, max(0, self.basestats[stat][0] - 10) // 2) + min(25, max(0,
                                                                                                              self.basestats[
                                                                                                                  stat][
                                                                                                                  0] - 50) // 2) + min(
                20, max(0, self.basestats[stat][0] - 110) // 2) + min(15, max(0, self.basestats[stat][0] - 160) // 2)
            self.secondstats["symb-light"] += self.GMstats["symb-light"]


        elif stat == "mental-res":
            # symbole
            self.secondstats["symb-mental"] = min(20, max(0, self.basestats[stat][0] - 10) // 2) + min(10, max(0,
                                                                                                               self.basestats[
                                                                                                                   stat][
                                                                                                                   0] - 60) // 4) + min(
                10, max(0, self.basestats[stat][0] - 110) // 4) + min(8, max(0, self.basestats[stat][0] - 158) // 4)
            self.secondstats["symb-mental"] += self.GMstats["symb-mental"]


        elif stat == "trading":
            # symbole 3 cubes empilés
            self.secondstats["symb-trading"] = min(40, max(0, self.basestats[stat][0] - 10) // 2) + min(40, max(10,
                                                                                                                self.basestats[
                                                                                                                    stat][
                                                                                                                    0] - 100) // 2) + min(
                40, max(15, self.basestats[stat][0] - 130) // 2) + min(40, max(10, self.basestats[stat][0] - 160) // 3)
            self.secondstats["symb-trading"] += 10 * (
                        (self.basestats[stat][0] >= 170) + (self.basestats[stat][0] >= 190))
            self.secondstats["symb-trading"] += self.GMstats["symb-trading"]


        elif stat in ["power", "mastery"]:
            # symbole
            self.secondstats["symb-lightning"] = min(10, self.basestats["power"][0] // 2) + min(10, max(0,
                                                                                                        self.basestats[
                                                                                                            "power"][
                                                                                                            0] - 20) // 3) + min(
                25, max(0, self.basestats["power"][0] - 60) // 4)
            self.secondstats["symb-lightning"] += (min(20, self.basestats["mastery"][0]) + min(15, max(0,
                                                                                                       self.basestats[
                                                                                                           "mastery"][
                                                                                                           0] - 20) // 2) + min(
                40, max(0, self.basestats["power"][0] - 60) // 2) + min(10,
                                                                        max(0, self.basestats["power"][0] - 150) // 4))
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
        """ Méthode qui calcule les nouveaux pourcentages aux dés après avoir augmenté les stats """

        if stat in ["hands", "light", "medium", "heavy", "throw", "shield", "charisma", "trading", "power"]:

            if stat == "power":
                self.percentages["spell"] = min(20, self.basestats[stat][0]) + 5 * (
                            self.basestats[stat][0] >= 50) + min(4, max(0, self.basestats[stat][0] - 130) // 5)
            else:
                self.percentages[stat] = min(20, self.basestats[stat][0]) + 5 * (self.basestats[stat][0] >= 50) + min(4,
                                                                                                                      max(
                                                                                                                          0,
                                                                                                                          self.basestats[
                                                                                                                              stat][
                                                                                                                              0] - 130) // 5)

        elif stat in ["mobility", "perception", "stealth", "sensitivity"]:
            self.percentages[stat] = min(20, self.basestats[stat][0]) + min(10, max(0, self.basestats[stat][
                0] - 40) // 2) + min(4, max(0, self.basestats[stat][0] - 130) // 5)

        elif stat == "dexterity":
            self.percentages[stat] = min(10, self.basestats[stat][0] // 2) + min(5, max(0, self.basestats[stat][
                0] - 20) // 4)
            self.percentages[stat] += 5 * ((self.basestats[stat][0] >= 50) + (self.basestats[stat][0] >= 70))

        elif stat == "phys-res":
            self.percentages[stat] = min(20, self.thirdstats[stat][0]) + min(10, max(0, self.thirdstats[stat][
                0] - 30) // 2) + min(5, max(0, self.thirdstats[stat][0] - 80) // 4) + min(5, max(0,
                                                                                                 self.thirdstats[stat][
                                                                                                     0] - 110) // 4) + min(
                5, max(0, self.thirdstats[stat][0] - 140) // 4)
            self.percentages[stat] += 5 * (self.thirdstats[stat][0] >= 70)

        elif stat == "mental-res":
            self.percentages[stat] = min(20, self.basestats[stat][0]) + min(10, max(0, self.basestats[stat][
                0] - 30) // 2) + min(4, max(0, self.basestats[stat][0] - 70) // 5) + min(8, max(0, self.basestats[stat][
                0] - 110) // 5)

    def change_invent_number(self, obj, number):
        """ Méthode qui permet de modifier le nombre d'objets obj que le personnage possède """
        if self.inventory[obj] + number >= 0:
            self.inventory[obj] += number

    def invent_suppr(self, obj):
        """ Methode qui supprime l'objet spécifié de l'inventaire """
        self.inventory.pop(obj)

    def equip_obj(self, obj, where=""):
        """ Méthode qui équipe un objet de l'inventaire (copie la référence dans playerequipment), si on en a au moins 1 """
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
                            self.playerequipment["right" * (where == "left") + "left" * (where == "right") + "_melee"] = \
                            self.playerequipment[where + "_melee"]

                    else:
                        if self.playerequipment[
                            "right" * (where == "left") + "left" * (where == "right") + "_melee"] == obj and \
                                self.inventory[obj] <= 1:
                            self.playerequipment[
                                "right" * (where == "left") + "left" * (where == "right") + "_melee"] = None

                    self.playerequipment[where + "_melee"] = obj
                else:
                    self.playerequipment["left_melee"] = self.playerequipment["right_melee"] = obj

    def unequip_obj(self, obj):
        """ Méthode pour déséquiper un objet du personnage """
        if type(obj) == ArmorEquip:
            self.playerequipment[obj.location] = None
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

    def GM_gain(self, stat, number):
        """ Méthode pour gérer les gains accordés par le MJ """
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
        """ Méthode pour réinitialiser les gains accordés par le MJ """

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

    def use_lightning(self, spell, number):
        """ Méthode qui attribue les éclairs aux sorts """

        if self.spells[spell] + number >= 0 and self.secondstats["symb-lightning"] >= number:
            self.spells[spell] += number
            self.secondstats["symb-lightning"] -= number

    def change_passive(self, stat, number):
        """ Méthode pour modifier les statistiques passives du personnage """
        if self.passivestats[stat][1] <= number <= self.passivestats[stat][2]:
            self.passivestats[stat][0] = number

    def convert_init(self, number):
        """ Méthode pour convertir l'initiative en habileté """
        if self.secondstats["symb-init"] - number >= self.secondstats["symb-ability"][1] + number:
            self.secondstats["symb-init"] -= number
            self.secondstats["symb-ability"][1] += number
            self.secondstats["symb-ability"][0] += number

    def get_armor_level(self):
        """ Méthode pour récupérer le niveau de palier d'armure """
        return self.secondstats["armor-level"]

    def get_basestats(self):

        return self.basestats

    def get_competences(self):

        return self.competences

    def get_current_armor(self, location):
        """ Méthode pour récupérer un des objets équipés"""
        return self.playerequipment[location]

    def get_gmstats(self):
        return self.GMstats

    def get_inventory(self):
        return self.inventory

    def get_invested_armor(self, location):
        """
        :param location: armor piece location
        :return: corresponding points of armor invested in the requested armor piece location
        """

        return self.thirdstats["invested_armor"][location]

    def get_lightnings(self,spell):

        return self.spells[spell]

    def get_name(self):

        return self.name

    def get_passivestats(self):
        return self.passivestats

    def get_percentages(self):
        return self.percentages

    def get_secondstats(self):

        return self.secondstats

    def get_spelllist(self):

        return self.spells.keys()

    def get_thirdstats(self):

        return self.thirdstats

    def get_weapon(self, side: str, weapontype: str):
        """
        :param weapontype: "melee" or "throw" weapon
        :param side: "left" or "right" hand weapon
        :return: corresponding weapon
        """
        return self.playerequipment[side+"_"+weapontype]

    def ismage(self):

        return self.mage

    def pop_spell(self,spell):
        """
        :param spell: name of the spell to remove from the player's set
        :return:
        """

        if self.spells[spell]>0:
            self.use_lightning(spell,-self.spells[spell])

        self.spells.pop(spell)


    def __setstate__(self, dict_attr):
        """Méthode appelée lors de la désérialisation de l'objet"""
        test_char = player()
        for key in test_char.__dict__.keys():
            if (not (key in dict_attr.keys())) or type(dict_attr[key]) != type(test_char.__dict__[key]):
                dict_attr[key] = test_char.__dict__[key]

        poplist = []

        for key in dict_attr.keys():
            if not (key in test_char.__dict__.keys()):
                poplist.append(key)

        for key in poplist:
            dict_attr.pop(key)

        self.__dict__ = dict_attr

    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        return "Personnage {}, a accumulé au total {} points d'xp, il lui en reste {} à répartir.".format(
            self.name, self.totalxp, self.xp)


## inventaire


class Obj(object):
    """ Objet de base """

    def __init__(self, name="", description="", stackable=False):
        self.name = name
        self.description = description
        self.is_stackable = stackable

    def get_stat(self, key):

        if key in self.__dict__.keys():
            return self.__dict__[key]

    def get_stats_aslist(self, keylist):
        valuelist = []

        for key in keylist:
            valuelist.append(self.get_stat(key))

        return valuelist


class Cord(Obj):
    """ Corde pour les armes de tir """

    def __init__(self, name="", description="", stackable="False", pourcentage=0):
        Obj.__init__(self, name, description, stackable)
        self.perc = pourcentage  # chance de ne pas casser en cas d'échec

    def set_perc(self,newval):

        self.perc = newval


class ArmorEquip(Obj):
    """ Classe de pièce d'équipement d'armure """

    def __init__(self, name="", description="", stackable=False, location=""):
        Obj.__init__(self, name, description, stackable)
        self.location = location
        self.carac = {}
        self.carac["prot"] = 0  # protection, pour les dégats du tranchant
        self.carac["amort"] = 0  # amortissement, pour les dégâts d'armes contondantes
        self.carac["mobi"] = 0  # mobilité offerte par l'armure (influence le jet de dés)
        self.carac["vit"] = 0  # ralentissement créé par l'armure
        self.carac["solid"] = 0  # solidité restante de l'objet

    def upstats(self, prot, amort, mobi, vit):
        """ Méthode qui permet de modifier les statistiques de la pièce d'armure """
        self.carac["prot"] = prot
        self.carac["amort"] = amort
        self.carac["mobi"] = mobi
        self.carac["vit"] = vit

    def upsolid(self, solid):
        """ Méthode de remise à neuf de la pièce d'armure """
        if self.carac["solid"] + solid >= 0:
            self.carac["solid"] += solid

    def get_stat(self,key):

        if key in self.carac.keys():
            return self.carac[key]

        else:
            return Obj.get_stat(self,key)

    def get_stats_aslist(self, keylist):
        valuelist = []

        for key in keylist:
            valuelist.append(self.get_stat(key))

        return valuelist


class MeleeEquip(Obj):
    """ Classe d'arme de mélée """

    def __init__(self, name="", description="", stackable=False, weight="", hast=False):
        """ Si c'est une arme de hast, l'objet fournit un bonus particulier.
        Sinon, l'objet possède une caractéristique de vitesse d'utilisation. """
        Obj.__init__(self, name, description, stackable)
        self.carac = {}
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

    def upstats(self, hand, tr, ctd, estoc, vit):
        """ Méthode qui permet de modifier les statistiques de l'arme """
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

    def upsolid(self, solid):
        """ Méthode de remise à neuf de l'arme """
        if self.carac["solid"] + solid >= 0:
            self.carac["solid"] += solid

    def newquali(self, quality=""):
        """ Méthode pour changer la qualité de l'arme """
        self.carac["quality"] = quality

    def get_stat(self, key):

        if key in self.carac.keys():
            return self.carac[key]

        else:
            return Obj.get_stat(self, key)

    def get_stats_aslist(self, keylist):
        valuelist = []

        for key in keylist:
            valuelist.append(self.get_stat(key))

        return valuelist

    def is_hast(self):

        return self.carac["hast"]

class ThrowEquip(Obj):
    """ Classe d'arme de jet et tir """

    def __init__(self, name="", description="", stackable=False, throw_type="Tir"):
        Obj.__init__(self, name, description, stackable)
        self.carac = {}
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

    def upstats(self, hand, dgt, pa):
        """ Méthode qui permet de modifier les statistiques de l'arme """
        self.carac["hand"] = hand
        self.carac["dgt"] = dgt
        self.carac["pa"] = pa

    def upmastery(self, mastery):
        """ Méthode qui permet de modifier la maitrise du personnage avec cette arme """
        if self.carac["mastery"] + mastery >= 0:
            self.carac["mastery"] += mastery

    def upsolid(self, solid):
        """ Méthode de remise à neuf de l'arme """
        if self.carac["solid"] + solid >= 0:
            self.carac["solid"] += solid

    def newscope(self, scope):
        """ Méthode pour définir le nouveau champ de caractéristiques pour la portée """
        self.carac["scope"] = scope

    def load_cord(self, obj):
        """ Méthode pour ajouter une corde à l'arme de tir """
        if self.carac["cord"]:  # on vérifie qu'il s'agit d'une arme de tir
            if obj.perc == self.carac["cord"][1] or self.carac["cord"][1] == 0:
                self.carac["cord"][0] += 1
                self.carac["cord"][1] = obj.perc
            else:
                """ Si on passe à une corde de pourcentage différent, on retire les autres """
                self.carac["cord"] = [1, obj.perc]

    def del_cord(self):
        """ Méthode pour retirer les cordes d'une arme """
        if self.carac["cord"]:
            self.carac["cord"] = [0, 0]

    def copy(self):
        """ Méthode pour copier l'arme. On retire les cordes car la copie n'en a pas """
        new_obj = ThrowEquip()
        new_obj.__dict__ = self.__dict__
        new_obj.del_cord()
        return new_obj

    def get_stat(self, key):

        if key in self.carac.keys():
            return self.carac[key]

        else:
            return Obj.get_stat(self, key)

    def get_stats_aslist(self, keylist):
        valuelist = []

        for key in keylist:
            valuelist.append(self.get_stat(key))

        return valuelist


class ShieldEquip(Obj):
    """ Classe de bouclier """

    def __init__(self, name="", description="", stackable=False):
        Obj.__init__(self, name, description, stackable=False)
        self.carac = {}
        self.carac["hand"] = 0  # nombre de mains nécessaires à l'utilisation
        self.carac["close"] = 0 # capactié à défendre au corps à corps
        self.carac["dist"] = 0 # capacité à défendre contre les tirs
        self.carac["mastery"] = 0 # maitrise du personnage sur cet objet
        self.carac["mobi"] = 0 # influence du bouclier sur la mobilité
        self.carac["vit"] = 0 # influence du bouclier sur la vitesse
        self.carac["quality"] = ""  # qualité de l'équipement (influence la perte de solidité)
        self.carac["solid"] = 0 # solidité restante de l'objet

    def upmastery(self, mastery):
        """ Méthode qui permet de modifier la maitrise du personnage avec cette arme """
        if self.carac["mastery"] + mastery >= 0:
            self.carac["mastery"] += mastery

    def upsolid(self, solid):
        """ Méthode de remise à neuf de l'arme """
        if self.carac["solid"] + solid >= 0:
            self.carac["solid"] += solid

    def upstats(self, hand, close, dist, mobi, vit):
        """ Méthode qui permet de modifier les statistiques de l'arme """
        self.carac["hand"] = hand
        self.carac["close"] = close
        self.carac["dist"] = dist
        self.carac["mobi"] = mobi
        self.carac["vit"] = vit

    def newquali(self, quality=""):
        """ Méthode pour changer la qualité de l'arme """
        self.carac["quality"] = quality

    def get_stat(self, key):

        if key in self.carac.keys():
            return self.carac[key]

        else:
            return Obj.get_stat(self, key)

    def get_stats_aslist(self, keylist):
        valuelist = []

        for key in keylist:
            valuelist.append(self.get_stat(key))

        return valuelist


class Competence(object):
    """ classe objet de compétence de personnage """

    def __init__(self, categ="", subcateg="", name="", effect=""):
        object.__init__(self)
        self.categ = categ
        self.subcateg = subcateg
        self.name = name
        self.effect = effect

    def copy(self):
        """ Méthode pour dupliquer la compétence """
        new_comp = Competence()
        new_comp.__dict__ = self.__dict__.copy()
        return new_comp

    def __str__(self):
        return "Compétence (catégorie {}) {} : {}".format(self.categ, self.name, self.effect)


class Spell(object):
    """ classe objet de sort de personnage """

    def __init__(self, elem="", subcateg="", name="", effect="", description="", cost=0):
        object.__init__(self)
        self.elem = elem
        self.subcateg = subcateg
        self.name = name
        self.effect = effect
        self.description = description
        self.cost = cost

    def copy(self):
        """ Méthode pour dupliquer le sort """
        new_spell = Spell()
        new_spell.__dict__ = self.__dict__.copy()
        return new_spell

    def get_stats_aslist(self,keys):
        valuelist=[]

        for key in keys:
            if key in self.__dict__.keys():
                valuelist.append(self.__dict__[key])

        return valuelist

    def __str__(self):
        return "Sort (élément {}) {} : {}".format(self.elem, self.name, self.effect)
