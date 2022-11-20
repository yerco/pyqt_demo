# pyQt demo

Bootstrapping the db

```python
import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    customer_type text,
    customer_name text,
    phone_number text,
    bill_amount text,
    bill_date text,
    address text
        CHECK(
            typeof("address") = "text" AND
            length("address") <= 30
        )
    )
''')
con.commit()
```

