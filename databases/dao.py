import sqlite3


class AuthorDTO(object):
    def __init__(self, pk, name):
        self.id = pk
        self.name = name

    def __str__(self):
        return 'Author <id: %i, name: %s>' % (self.id, self.name)


class AuthorDAO(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def find(self, pk):
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM author WHERE id=?', (pk,))
            pk, name = cur.fetchone()
            return AuthorDTO(pk, name)

    def update(self, pk, name):
        raise NotImplementedError

    def insert(self, name):
        raise NotImplementedError

    def delete(self, pk):
        raise NotImplementedError


if __name__ == '__main__':
    dao = AuthorDAO('myLibrary.db')
    a1 = dao.find(2)
    print(a1)
    print(dao.find(1))
    # dao.update(2, 'new name')
