@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username=? AND password=?"
    c.execute(query, (username, password))
    result = c.fetchone()
    conn.close()
    if result:
        return "Login successful!"
    else:
        return "Login failed!"
