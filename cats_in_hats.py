def cats_in_hats(num_cats):
    cats = ["off"] * num_cats  # Initialize the list of cats with hats off
    for round in range(1, num_cats + 1):
        for cat in range(round, num_cats + 1, round):
            if cats[cat - 1] == "on":
                cats[cat - 1] = "off"
            else:
                cats[cat - 1] = "on"

    cats_with_hats = [index + 1 for index, hat_status in enumerate(cats) if hat_status == "on"]
    return cats_with_hats

num_cats = 100
cats_with_hats = cats_in_hats(num_cats)
print("Cats with hats:", cats_with_hats)

# Time complexity = O(n^2), because of two loops
# Space complexity = O(n) according to the number of cats in the circle