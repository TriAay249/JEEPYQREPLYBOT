from flask import Flask, request, redirect
from form_validator import validate_form
from form_parser import parse_form
from urllib.parse import quote

app = Flask(__name__)


@app.route('/form_submit', methods=['POST'])
def form_submit():
    form_data = dict(request.form)
    is_valid_form, err_msg = validate_form(form_data)
    base_url = form_data.get("url").split("index.html")[0].removesuffix("/")

    if is_valid_form:
        # TODO: implement github integration
        print(parse_form(form_data))
        redirect_url = base_url + "/submitted.html"
        return redirect(redirect_url)
    else:
        base_url = form_data.get("url").split("index.html")[0].removesuffix("/")
        redirect_url = base_url + "/invalid-form.html?err=" + quote(err_msg)
        return redirect(redirect_url)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
