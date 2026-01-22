from flask import Flask # pyright: ignore[reportMissingImports]

# Create an instance of the Flask class.
# __name__ tells Flask where to look for resources like templates and static files.
app = Flask(__name__)

# Define a route using the @app.route() decorator.
# This tells Flask which URL should trigger the associated function.
@app.route("/")
def hello_world():
    # The function returns the content to be displayed in the user's browser.
    return "<p>Hello, World!</p>"

# Run the application if the script is executed directly.
if __name__ == "__main__":
    app.run()