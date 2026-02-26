class Flower:
    def __init__(self, name, color, stem_length, price, days_old, lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.days_old = days_old
        self.lifespan = lifespan

    @property
    def remaining_life(self):
        return max(0, self.lifespan - self.days_old)

    def __repr__(self):
        return (f"{self.name} ({self.color}, длина={self.stem_length}см, "
                f"цена={self.price}р., осталось={self.remaining_life} дн.)")


class Rose(Flower):
    def __init__(self, color, stem_length, price, days_old, lifespan=10):
        super().__init__("Роза", color, stem_length, price, days_old, lifespan)


class Tulip(Flower):
    def __init__(self, color, stem_length, price, days_old, lifespan=7):
        super().__init__("Тюльпан", color, stem_length, price, days_old, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(f.price for f in self.flowers)

    def average_wilting_time(self):
        if not self.flowers:
            return 0
        return sum(f.remaining_life for f in self.flowers) / len(self.flowers)

    def sort_by_freshness(self, reverse=False):
        self.flowers.sort(key=lambda f: f.remaining_life, reverse=not reverse)

    def sort_by_color(self, reverse=False):
        self.flowers.sort(key=lambda f: f.color, reverse=reverse)

    def sort_by_stem_length(self, reverse=False):
        self.flowers.sort(key=lambda f: f.stem_length, reverse=reverse)

    def sort_by_price(self, reverse=False):
        self.flowers.sort(key=lambda f: f.price, reverse=reverse)

    def search(self, stem_length_range=None, remaining_life_range=None):
        result = self.flowers[:]
        if stem_length_range is not None:
            min_len, max_len = stem_length_range
            result = [f for f in result if min_len <= f.stem_length <= max_len]
        if remaining_life_range is not None:
            min_life, max_life = remaining_life_range
            result = [f for f in result if min_life <= f.remaining_life <= max_life]
        return result

    def __repr__(self):
        return f"Букет из {len(self.flowers)} цветов: {self.flowers}"


if __name__ == "__main__":
    rose1 = Rose("красный", 50, 150, 2)
    rose2 = Rose("белый", 60, 200, 1, lifespan=12)
    tulip1 = Tulip("желтый", 40, 80, 3)
    tulip2 = Tulip("розовый", 35, 90, 0)

    bouquet = Bouquet()
    bouquet.add_flower(rose1)
    bouquet.add_flower(rose2)
    bouquet.add_flower(tulip1)
    bouquet.add_flower(tulip2)

    print("Исходный букет:")
    print(bouquet)

    print(f"\nОбщая стоимость букета: {bouquet.total_cost()} руб.")
    print(f"Среднее оставшееся время жизни букета: {bouquet.average_wilting_time():.2f} дн.")

    bouquet.sort_by_freshness()
    print("\nПосле сортировки по свежести (от свежих к увядающим):")
    print(bouquet)

    bouquet.sort_by_stem_length()
    print("\nПосле сортировки по длине стебля (возрастание):")
    print(bouquet)

    found = bouquet.search(stem_length_range=(40, 60), remaining_life_range=(5, 10))
    print("\nЦветы с длиной стебля 40-60 см и остаточным временем 5-10 дней:")
    for f in found:
        print(f"  {f}")
        