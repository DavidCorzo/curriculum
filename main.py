from flask import Flask, render_template
import func_dgcm

master = func_dgcm.read_yaml_and_writing_to_about()[0]

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('curriculum_template.html', title=master['Title'])


@app.route('/personal_info')
def personal_info():
    return render_template('personal_info.html', name=master['Name'], age=master['Age'], nationality=master['Nationality'], schooling=master['schooling'], carrer=master['career'], academic=master['academic'], work=master['schooling_schools'], schooling_schools=master['schooling_schools'])


@app.route('/about')
def about():
    return render_template('about.html', about=master['About_me'])


@app.route('/contact')
def contact():
    return render_template('contact.html', telephone=master['Telephone'], nationality=master['Nationality'], email=master['E-mail'], fb=master['fb'], tw=master['tw'], ig=master['ig'], link_in=master['link_in'], )


@app.route('/work')
def work():
    return render_template('work.html', work=master['work'])


if __name__ == "__main__":
    app.run()
