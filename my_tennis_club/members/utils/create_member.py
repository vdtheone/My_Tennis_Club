from members.models import Member


def create_random_member():
    names = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Emma",
        "Frank",
        "Grace",
        "Hannah",
        "Isaac",
        "Jack",
        "Katie",
        "Liam",
        "Mia",
        "Nathan",
        "Olivia",
        "Peter",
        "Quinn",
        "Rachel",
        "Samuel",
        "Taylor",
        "Ursula",
        "Victor",
        "Wendy",
        "Xander",
        "Yvonne",
        "Zachary",
    ]

    last_names = [
        "Smith",
        "Johnson",
        "Brown",
        "Taylor",
        "Wilson",
        "Davis",
        "Miller",
        "Jones",
        "Garcia",
        "Rodriguez",
        "Martinez",
        "Hernandez",
        "Lopez",
        "Gonzalez",
        "Perez",
        "Williams",
        "Lee",
        "Chen",
        "Kim",
        "Nguyen",
        "Singh",
        "Patel",
        "Ali",
        "Muller",
        "Schmidt",
        "Meyer",
        "Schneider",
        "Fischer",
        "Weber",
        "Schulz",
        "Schwarz",
        "Wong",
        "Chang",
        "Wang",
        "Li",
        "Chen",
        "Wu",
        "Liu",
        "Huang",
        "Li",
        "Kumar",
        "Rao",
        "Sharma",
        "Das",
        "Sen",
        "Choudhury",
        "Jha",
        "Banerjee",
    ]

    print(len(names))
    print(len(last_names))
    for i in range(25):
        slug = f"{names[i]}-{last_names[i]}"
        new_member = Member(
            first_name=names[i], last_name=last_names[i], phone=7854127854, slug=slug
        )
        new_member.save()
