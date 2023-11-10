import sqlite3

connection = sqlite3.connect("base.sqlite")
cur = connection.cursor()


def create_team(t_name):
    f = cur.execute("""SELECT id FROM teams WHERE name = ?""", (t_name,)).fetchone()
    if f:
        return False
    cur.execute("""INSERT INTO teams (name, score) VALUES (?, 0)""", (t_name,))
    connection.commit()
    return True


def add_team_member(user_id, name, t_name):
    f = cur.execute("""SELECT id FROM teams WHERE name = ?""", (t_name,)).fetchone()
    if not f:
        return False
    f = cur.execute("""SELECT name FROM users WHERE user_id = ?""", (user_id,)).fetchone()
    if f:
        cur.execute("""DELETE FROM users WHERE user_id = ?""", (user_id,))
        connection.commit()
    recv = """INSERT INTO users SELECT ?, ?, (
    SELECT id FROM teams WHERE name = ?)"""
    cur.execute(recv, (user_id, name, t_name))
    connection.commit()
    return True


def update_score(user_id, sc_change):
    recv = """UPDATE teams 
    SET score = score + ?
    WHERE id = (
    SELECT team FROM users 
    WHERE user_id = ?)"""

    cur.execute(recv, (sc_change, user_id))
    connection.commit()

