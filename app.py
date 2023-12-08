# Basic Website Template
import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    dt = datetime.datetime.utcnow()
    return render_template_string(
        '''
        <html><body>
        <h4>UTC --> Local Time</h4>
        Datetime right now is:
        <p>{{ dt | datetimefilter }} (utc)</p>
        <p><span id="timeNow"></span> (local)</p>
        <script>
        var elem = document.getElementById("timeNow")
        var now = new Date();
        var options = { month: 'short', day: '2-digit',
                        hour: 'numeric', minute: '2-digit' };
        elem.innerHTML = now.toLocaleString('en-us', options);
        </script>
        </body></html>
        ''',
        dt=dt)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
