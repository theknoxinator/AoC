# Determine which aunt sent the package to you based on information gleaned from the package

class AuntInfo:
    def __init__(self, items=None):
        self.children = None
        self.cats = None
        self.samoyeds = None
        self.pomeranians = None
        self.akitas = None
        self.vizslas = None
        self.goldfish = None
        self.trees = None
        self.cars = None
        self.perfumes = None
        if items:
            self.id = items[1]
            self.set_prop(items[2], items[3])
            self.set_prop(items[4], items[5])
            self.set_prop(items[6], items[7])

    def set_prop(self, key, value):
        if key == "children":
            self.children = value
        elif key == "cats":
            self.cats = value
        elif key == "samoyeds":
            self.samoyeds = value
        elif key == "pomeranians":
            self.pomeranians = value
        elif key == "akitas":
            self.akitas = value
        elif key == "vizslas":
            self.vizslas = value
        elif key == "goldfish":
            self.goldfish = value
        elif key == "trees":
            self.trees = value
        elif key == "cars":
            self.cars = value
        elif key == "perfumes":
            self.perfumes = value

    def matches(self, other_info):
        if other_info.children is not None and other_info.children != self.children:
            return False
        if other_info.cats is not None and other_info.cats != self.cats:
            return False
        if other_info.samoyeds is not None and other_info.samoyeds != self.samoyeds:
            return False
        if other_info.pomeranians is not None and other_info.pomeranians != self.pomeranians:
            return False
        if other_info.akitas is not None and other_info.akitas != self.akitas:
            return False
        if other_info.vizslas is not None and other_info.vizslas != self.vizslas:
            return False
        if other_info.goldfish is not None and other_info.goldfish != self.goldfish:
            return False
        if other_info.trees is not None and other_info.trees != self.trees:
            return False
        if other_info.cars is not None and other_info.cars != self.cars:
            return False
        if other_info.perfumes is not None and other_info.perfumes != self.perfumes:
            return False
        return True

    def matches_part2(self, other_info):
        if other_info.children is not None and other_info.children != self.children:
            return False
        if other_info.cats is not None and other_info.cats <= self.cats:
            return False
        if other_info.samoyeds is not None and other_info.samoyeds != self.samoyeds:
            return False
        if other_info.pomeranians is not None and other_info.pomeranians >= self.pomeranians:
            return False
        if other_info.akitas is not None and other_info.akitas != self.akitas:
            return False
        if other_info.vizslas is not None and other_info.vizslas != self.vizslas:
            return False
        if other_info.goldfish is not None and other_info.goldfish >= self.goldfish:
            return False
        if other_info.trees is not None and other_info.trees <= self.trees:
            return False
        if other_info.cars is not None and other_info.cars != self.cars:
            return False
        if other_info.perfumes is not None and other_info.perfumes != self.perfumes:
            return False
        return True


def which_aunt(values, use_part2=False):
    # First, create the standard to compare each aunt against
    expected = AuntInfo()
    expected.set_prop("children", "3")
    expected.set_prop("cats", "7")
    expected.set_prop("samoyeds", "2")
    expected.set_prop("pomeranians", "3")
    expected.set_prop("akitas", "0")
    expected.set_prop("vizslas", "0")
    expected.set_prop("goldfish", "5")
    expected.set_prop("trees", "3")
    expected.set_prop("cars", "2")
    expected.set_prop("perfumes", "1")

    # Now create a list of all the aunts and their information
    aunts = []
    for val in values:
        items = val.replace(':','').replace(',','').split()
        aunts.append(AuntInfo(items))

    # Now iterate and try to find a match
    package_aunt = None
    for aunt in aunts:
        if use_part2 and expected.matches_part2(aunt):
            package_aunt = aunt
            break
        elif not use_part2 and expected.matches(aunt):
            package_aunt = aunt
            break

    return package_aunt.id


def part1(values):
    return which_aunt(values)


def part2(values):
    return which_aunt(values, True)
