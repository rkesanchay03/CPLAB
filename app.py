from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
expenses = []

@app.route('/')
def home():
    total_expense = sum(expense['amount'] for expense in expenses)
    return render_template('home.html', expenses=expenses, total=total_expense)


@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = int(request.form['amount'])
        category = request.form['category']
        new_expense = {
            'description': description,
            'amount': amount,
            'category': category
        }
        expenses.append(new_expense)
        return redirect(url_for('home'))

    return render_template('add_expense.html')
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
