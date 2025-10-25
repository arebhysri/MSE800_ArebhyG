from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templete')

def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15
def f_to_k(f): return (f - 32) * 5/9 + 273.15
def k_to_f(k): return (k - 273.15) * 9/5 + 32

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        value = float(request.form.get('temperature', ''))
        frm = request.form.get('from_unit')
        to = request.form.get('to_unit')
    except Exception:
        return render_template('index.html', error='Invalid number')

    if frm == to:
        result = value
    else:
        if frm == 'C' and to == 'F':
            result = c_to_f(value)
        elif frm == 'F' and to == 'C':
            result = f_to_c(value)
        elif frm == 'C' and to == 'K':
            result = c_to_k(value)
        elif frm == 'K' and to == 'C':
            result = k_to_c(value)
        elif frm == 'F' and to == 'K':
            result = f_to_k(value)
        elif frm == 'K' and to == 'F':
            result = k_to_f(value)
        else:
            return render_template('index.html', error='Unsupported conversion')

    result = round(result, 4)
    return render_template('index.html',
                           value=value, frm=frm, to=to, result=result)

if __name__ == '__main__':
    app.run(debug=True)