from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

"""
@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'
"""


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
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome to Search4Letters!")

@app.route('/viewlog')
def view_the_log() -> 'html':
    with open('vsearch.log') as log:
        contents = []
        for line in log:
            #print(line)
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(item)
        titles = ('Form_Data', 'Remote_Addr', 'User_Agent', 'Results')
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents)


if __name__ == "__main__":
    app.run(debug=True)
