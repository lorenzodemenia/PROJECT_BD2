from struttura_db import *


@app.route('/s', methods=['POST'])
@login_required
def search():
    if request.method == 'POST':
        print('yuppi')

        search = request.form['search']
        print(search)

    return render_template('Home/search.html', search=search)
