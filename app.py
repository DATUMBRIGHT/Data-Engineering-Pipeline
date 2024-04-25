from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # List of paths to the saved plot images and their corresponding titles
    plot_data = [
        {'path': 'output1.png', 'title': 'Most Frequently Occurring Words - Top 30'},
        {'path': 'output2.png', 'title': 'The Polarity Index of Dataset'},
        {'path': 'output3.png', 'title': 'The Negative Words Word Cloud'},
        {'path': 'output4.png', 'title': 'The Neutral Words Word Cloud'},
        {'path': 'output5.png', 'title': 'Variation vs Length Plot'},
        {'path': 'output6.png', 'title': 'Positive Words Word Cloud'},
        {'path': 'output7.png', 'title': 'Vocabulary Words Word Cloud'}
    ]
    
    # Render the template with the plot images and their titles
    return render_template('index.html', plot_data=plot_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
