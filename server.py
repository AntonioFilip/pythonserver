from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(f'{page_name}.html')


def write_to_file(data):
    with open('C:/Users/Antonio/SDN/PythonMastery/web/database.txt', mode='a') as file:
        name, email, message = data['name'], data['email'], data['message']
        try:
            file.write(f'\n{name} : {email} : {message}')
        except IOError as err:
            print("I/O error({0})".format(err))


def write_to_csv(data):
    with open('C:/Users/Antonio/SDN/PythonMastery/web/database.csv', mode='a', newline='') as csv_file:
        name, email, message = data['name'], data['email'], data['message']
        try:
            writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([name, email, message])
        except IOError as err:
            print("I/O error({0})".format(err))


@app.route('/contact', methods=['POST'])
def contact():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thanks')
    else:
        return 'Not good, it failed'


if __name__ == "__main__":
    app.run(debug=True)