import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect("""
password=postgres dbname=postgres user=postgres port=38746 host=localhost
""", cursor_factory=RealDictCursor)


class StorageCell:
    def __init__(self, id: int, code: str, capacity: int):
        self.id = id
        self.code = code
        self.capacity = capacity


class Holder:
    def __init__(self, id: int, name: str, phone: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.storage_cells = []

    def show_info(self):
        print(f"""Имя: {self.name}, телефон: {self.phone}, id: {self.id}""")


def print_holders():
    cur = conn.cursor()

    cur.execute("""
select holder_id, h.name, h.phone, c.id cell_id, c.code, c.capacity
from holder h
         join storage_cell c on h.id = c.holder_id;
    """)
    rows = cur.fetchall()

    holders_dict = {}
    for row in rows:
        holder_id = row['holder_id']
        if holder_id not in holders_dict:
            holder = Holder(row['holder_id'], row['name'], row['phone'])
            holders_dict[holder_id] = holder
        else:
            holder = holders_dict[holder_id]

        storage_cell = StorageCell(row['cell_id'], row['code'], row['capacity'])
        holder.storage_cells.append(storage_cell)

    print()


print_holders()
