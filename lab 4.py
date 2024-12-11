class Item:
    def __init__(self, name, code, weight, value):
        self.name = name
        self.code = code
        self.weight = weight
        self.value = value


def knapsack(items, capacity, mandatory_items):


    def knapsack_recursive(i, current_weight, current_value, inventory):
        nonlocal max_value, best_inventory
        if current_weight > capacity or i == len(items):
            return

        if current_value > max_value and all(m in [x.code for x in inventory] for m in mandatory_items):
            max_value = current_value
            best_inventory = inventory[:]

        knapsack_recursive(i + 1, current_weight, current_value, inventory)

        if current_weight + items[i].weight <= capacity:
            inventory.append(items[i])
            knapsack_recursive(i + 1, current_weight + items[i].weight, current_value + items[i].value, inventory)
            inventory.pop()

    mandatory_objects = [item for item in items if item.code in mandatory_items]
    mandatory_weight = sum(item.weight for item in mandatory_objects)
    mandatory_value = sum(item.value for item in mandatory_objects)

    if mandatory_weight > capacity:
        return None, None

    items = [item for item in items if item.code not in mandatory_items]

    max_value = float('-inf')
    best_inventory = []
    knapsack_recursive(0, mandatory_weight, mandatory_value, mandatory_objects)
    return best_inventory, max_value


if __name__ == '__main__':
    items = [
        Item("Винтовка", "r", 3, 25),
        Item("Пистолет", "p", 2, 15),
        Item("Боекомплект", "a", 2, 15),
        Item("Аптечка", "m", 2, 20),
        Item("Ингалятор", "i", 1, 5),
        Item("Нож", "k", 1, 15),
        Item("Топор", "x", 3, 20),
        Item("Оберег", "t", 1, 25),
        Item("Фляжка", "f", 1, 15),
        Item("Антидот", "d", 1, 10),
        Item("Еда", "s", 2, 20),
        Item("Арбалет", "c", 2, 20),
    ]

    initial_points = 20
    capacity = 8
    mandatory = ["i"]

    best_items, final_points = knapsack(items, capacity, mandatory)
    if best_items is None:
        print("Обязательные предметы не помещаются в рюкзак!")
    else:
        final_points += initial_points

        inventory_grid = [["[ ]" for _ in range(4)] for _ in range(2)]
        position = 0

        for item in best_items:
            for _ in range(item.weight):
                row, col = divmod(position, 4)
                inventory_grid[row][col] = f"[{item.code}]"
                position += 1

        print("Рюкзак:")
        for row in inventory_grid:
            print(" ".join(row))
        print(f"\nИтоговые очки выживания: {final_points}")
