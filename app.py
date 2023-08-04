from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Dhaka, Bangladesh',
  'salary': '1000000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Rajshahi, Bangladesh',
  'salary': '1500000'
}, {
  'id': 3,
  'title': 'Front End Developer',
  'location': 'Remote',
}, {
  'id': 4,
  'title': 'Back End Developer',
  'location': 'Khulna, Bangladesh',
  'salary': '1800000'
}]


@app.route("/")
def hello_shohel():
  return render_template('home.html', jobs=JOBS)


# # print(__name__)
if __name__ == "__main__":
  #   # print("Im inside now")
  app.run(host='0.0.0.0', debug=True)
