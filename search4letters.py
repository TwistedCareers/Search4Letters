import mysql.connector

from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

"""
@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'
"""

dbconfig = {
    'host': 'localhost',
    'user': 'vsearch',
    'password': 'vsearchpasswd',
    'database': 'vsearchlogdb'
}


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results: "
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


def log_request(req: 'flask_request', res: str) -> None:   
    conn = mysql.connector.connect(**dbconfig) 
    cursor = conn.cursor()

    _SQL = """insert into log(phrase, letters, ip, browser_setting, results)
            values(%s, %s, %s, %s, %s)"""
    
    cursor.execute(_SQL, (
        req.form['phrase'],
        req.form['letters'],
        req.remote_addr,
        req.user_agent.browser,
        res,
    ))

    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome to Search4Letters!")

@app.route('/viewlog')
def view_the_log() -> 'html':
    conn = mysql.connector.connect(**dbconfig) 
    cursor = conn.cursor()

    _SQL = """select phrase, letters, ip, browser_setting, results from log"""

    cursor.execute(_SQL)

    
    contents = []
    for row in cursor.fetchall():
        contents.append([])
        for item in row:
            contents[-1].append(item)
    titles = ('Phrase', 'Letters', 'Remote_Addr', 'Browser', 'Results')
    cursor.close()
    conn.close()
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents)


if __name__ == "__main__":
    app.run(debug=True)
