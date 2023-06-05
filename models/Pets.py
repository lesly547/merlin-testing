class Pets:
    def __init__(self, data):
        self.data = data

    def count_similar_pets_name(self):
        names = [item["name"] for item in self.data if "name" in item]
        count = {}

        for name in names:
            if name in count:
                count[name] += 1
            else:
                count[name] = 1
        return count
