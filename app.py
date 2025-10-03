from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# --- ROUTES FOR DETAIL PAGES ---
@app.route('/discover-scuba-details')
def discover_scuba_details():
    return render_template('discover-scuba-details.html')

@app.route('/average-deep-dive-details')
def average_deep_dive_details():
    return render_template('average-deep-dive.html')

@app.route('/shallow-scuba-dive-details')
def shallow_scuba_dive_details():
    return render_template('shallow-scuba-dive.html')
    
@app.route('/watersports-package-details')
def watersports_package_details():
    return render_template('watersports-package.html')

# Routes for policy pages
@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/refund-policy')
def refund_policy():
    return render_template('refund-policy.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

@app.route('/return-cancellation-policy')
def return_cancellation_policy():
    return render_template('return-cancellation-policy.html')

# Route to handle the booking form submission
@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    email = request.form.get('email')
    activity = request.form.get('activity')
    date = request.form.get('date')
    people = request.form.get('people')
    with open('bookings.txt', 'a') as f:
        f.write(f"Name: {name}, Email: {email}, Activity: {activity}, Date: {date}, People: {people}\n")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
    