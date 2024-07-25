# Zampulse
visit my finished project about here: https://about-zampulse.my.canva.site/
![Zampulse](https://via.placeholder.com/728x90.png?text=ZambiaCanCode+Header+Image)
Try my application here
![Link to deployed app]((https://conservation-zampulse-1.onrender.com/))

Zampulse is a Django-based web application, It is a new initiative aimed at unifying community efforts in freshwater conservation. It will act as a central platform where users can share and access information about freshwater issues in Zambia and The stories will be used to mobilise support for policy reforms and community-based conservation efforts in Chingola, Zambia. The goal is to raise awareness, strengthen local communities, and promote sustainable solutions.. 

This documentation provides an overview of the project structure, setup instructions, and key features.

## Features

- User Authentication
- Admin Dashboard
- Database Management
- Template Rendering
- Session Management

## Project Structure

Zampulse/ │ ├── Zampulse/ │ ├── init.py │ ├── settings.py │ ├── urls.py │ ├── asgi.py │ ├── wsgi.py │ ├── manage.py │ └── templates/


## Getting Started

### Prerequisites

- Python 3.12
- Django 5.0.6

### Installation

1. Clone the repo

    ```sh
    git clone https://github.com/David3D-AndweM/Zampulse.git
    ```
2. Navigate to Zampulse directory # Create a New Virtual Environment

# Open your terminal or command prompt and navigate to the root of your project directory (if you haven't already).
# Then, create a new virtual environment using the following command:
python -m venv env

# Activate the virtual environment:
# On Windows:
```sh
env\Scripts\activate
```
# On macOS and Linux:
```sh
source env/bin/activate
```
# Navigate to Zampulse Directory and Modify ALLOWED_HOSTS Setting

# Open the `settings.py` file located in the `Zampulse` directory.
# Find the line that sets the `ALLOWED_HOSTS` variable. It should look like this:
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(" ")

# Change the `ALLOWED_HOSTS` setting to allow `localhost` by default. Replace the current line with:
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Install Dependencies

# If you haven't installed Django and other project dependencies in the new environment, run:

# Restart Your Django Server

# If your Django development server is running, restart it to apply the changes. You can do this by stopping the server (usually with `Ctrl+C` in the terminal) and then starting it again with:


3. Install dependencies

    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations

    ```sh
    python manage.py migrate
    ```

5. Run the server

    ```sh
    python manage.py runserver 
    ```

## Usage

1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. You'll see the admin dashboard and other features in action.

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

![Footer Image](https://via.placeholder.com/728x90.png?text=Footer+Image)


Fully developed by 
David Mwape <d.mwape@alustudent.com>
