class Party:
    def __init__(self):
        self.people = []

party = Party()

while True:
    person_name = input()
    if person_name == "End":
        break
    party.people.append(person_name)

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')



