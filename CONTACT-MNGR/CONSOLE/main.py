import sqlite3

conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    tef TEXT NOT NULL,
    email TEXT
)
''')
conn.commit()

def add_contact():
    while True:
        name = input("Enter Name (required): ").strip()
        if name:
            break
        print("Name is required. Please try again.")

    while True:
        tef = input("Enter TEF (required): ").strip()
        if tef:
            break
        print("TEF is required. Please try again.")

    email = input("Enter E-Mail (optional): ").strip() or None

    cursor.execute('INSERT INTO contacts (name, tef, email) VALUES (?, ?, ?)', (name, tef, email))
    conn.commit()
    print("Contact added successfully!")

def view_contacts():
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    print("\nContacts:")
    for contact in contacts:
        print(f"ID: {contact[0]}, Name: {contact[1]}, TEF: {contact[2]}, E-Mail: {contact[3] if contact[3] else 'N/A'}")
    print()

def remove_contact():
    view_contacts()
    contact_id = input("Enter the ID of the contact to remove: ").strip()
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    print("Contact removed successfully!")

def search_contact():
    search_term = input("Enter a name or TEF to search: ").strip()
    cursor.execute('SELECT * FROM contacts WHERE name LIKE ? OR tef LIKE ?', (f'%{search_term}%', f'%{search_term}%'))
    results = cursor.fetchall()
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"ID: {contact[0]}, Name: {contact[1]}, TEF: {contact[2]}, E-Mail: {contact[3] if contact[3] else 'N/A'}")
    else:
        print("No contacts found.")
    print()

def main():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            remove_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
    conn.close()