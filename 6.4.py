class Build(Exception):
    def __str__(self):
        return f"With that amount of material we cant build a house"
def checkmaterial(material1, limit):
    if material1 >= limit:
        print("We can start building")
    else:
        raise Build()

materials = 400
limits = 450
checkmaterial(materials, limits)
