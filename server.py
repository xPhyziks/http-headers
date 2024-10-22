from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    formatted_headers = None
    if request.method == 'POST':
        raw_headers = request.form.get('headers')
        if raw_headers:
            lines = raw_headers.split('\n')
            formatted_headers = []
            i = 0

            while i < len(lines):
                stripped_line = lines[i].strip()

                if ':' in stripped_line:  # It's a key line
                    key_line = stripped_line
                    i += 1

                    # If the next line does NOT contain a colon, it's the value, append it to the key
                    if i < len(lines) and ':' not in lines[i]:
                        value_line = lines[i].strip()
                        key_line = f"{key_line} {value_line}"

                    formatted_headers.append(key_line)
                else:
                    formatted_headers.append(stripped_line)

                i += 1

            formatted_headers = '\n'.join(formatted_headers)

    return render_template('index.html', formatted_headers=formatted_headers)

if __name__ == '__main__':
    app.run(debug=True)
