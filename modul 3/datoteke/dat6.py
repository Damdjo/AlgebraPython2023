class Contact:
    def __init__(self, id, fn, ln, phone):
        self.id = id
        self.fn = fn
        self.ln = ln
        self.phone = phone
        
    def print_contact(self):
        print(f"ID: {self.id}, Ime: {self.fn}, Prezime: {self.ln}, Mob: {self.phone}")



address_book = {}

try:
    with open("m3/datoteke/adresar.txt", "r") as fr:
        for line in fr:
            line = line.rstrip()
            line_part = line.split(";")
            contact = Contact(line_part[0], line_part[1], line_part[2], line_part[3])
            address_book[contact.id] = contact

except Exception as e:
    print(f"Greška: {e}")

for key, value in address_book.items():
    print(key, end = "\t")
    value.print_contact()