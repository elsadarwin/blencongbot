## User Guide
### Command List
**/quote** - Get random quote from [our database](https://github.com/elsadarwin/blencong-quotes)

**/who** - BlencongBot short intro

## Development Guide

### How to set up your machine

1. Setup your Python virtual environment. There are two ways to do this. One is via [virtualenvwrapper][virtualenvwrapper] and the other one is via [pyenv][pyenv]. If you decided to use [virtualenvwrapper][virtualenvwrapper], here are the steps you may follow:

    1. Make sure you have Python on your system.

    1. Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) to make it easier working with [virtualenv](https://virtualenv.pypa.io/en/latest/). We need virtualenv because Blencongbot uses Python 3, whereas most systems still use Python 2. Virtualenv makes it easy to manage different Python versions along with their libraries. There are many ways to install virtualenvwrapper. One of the easiest ways is to use Pip.
       ```bash
       pip install virtualenvwrapper
       ```

       [Pip](https://pip.pypa.io/en/latest/) is the default package manager for Python. It should already be installed if you have Python >= 2.7.9 or Python >= 3.4 on your system.

    1. Configure your virtualenvwrapper as described in [their docs](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#shell-startup-file).

    1. Make sure you have Python 3 installed on your system. This can be done in many ways. For instance, in OSX, you may install it with Homebrew
       ```bash
       brew install python3
       ```

       **UPDATE**:
       Homebrew's `python3` is already updated to Python 3.5. Since we're using Python 3.4, you might want to use [pyenv][pyenv] instead.

    1. [Create a Python 3 virtual environment](https://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#mkvirtualenv) and clone this repository.
       ```bash
       mkvirtualenv -p /path/to/python3/binary name_of_your_virtualenv
       git clone git@github.com:blencong/blencongbot.git /path/to/your/blencongbot/project/directory
       ```

    1. Activate the virtual environment you've just created.
       ```bash
       workon name_of_your_virtualenv
       ```

    If you'd like to use [pyenv][pyenv] instead, here are the steps you may follow:

    1. Install [pyenv][pyenv] and its [pyenv-virtualenv][pyenv-virtualenv] plugin. Configure them as written in their docs.

    1. Install Python 3.4 with `pyenv`, create virtual environment, and clone this repository.
       ```bash
       pyenv install 3.4.3
       pyenv virtualenv 3.4.3 name_of_your_virtualenv
       git clone git@github.com:blencong/blencongbot.git /path/to/your/blencongbot/project/directory
       ```

    1. Activate the virtual environment you've just created.
       ```bash
       pyenv activate name_of_your_virtualenv
       ```

1. Navigate to the directory where you've cloned this repo and install all its dependencies.
   ```bash
   cd /path/to/your/blencongbot/project/directory
   pip install -r requirements.txt
   ```

   Dependencies are all listed in `requirements.txt`. To re-generate this file (after you've installed new packages), simply run `pip freeze > requirements.txt`. For Linux users, if you have a problem installing the dependencies (PyYaml in particular), install the package `python3-dev` or `python3-devel` first.

1. Create `.env` file under the project root directory. It contains the configuration variables for the application. Sample `.env` file can be found in `.env.example`.

1. Run the app
   ```bash
   python manage.py runserver
   # or
   ./manage.py runserver
   ```

1. The app is now running! Try to play around with it by simulating a webhook request. For instance, try this:
   ```bash
   curl --data '{"update_id": 12345,"message":{"text":"/who","chat":{"id":-12345},"message_id":1}}' --header "Content-Type: application/json" http://127.0.0.1:5000/<YOUR TELEGRAM BOT TOKEN IN .ENV>
   ```

   You should get an OK response.

   As you can see, the url endpoint is determined by the `TELEGRAM_BOT_TOKEN` config variable. This is actually [recommended by Telegram](https://core.telegram.org/bots/api#setwebhook).

[virtualenvwrapper]: https://pypi.python.org/pypi/virtualenvwrapper
[pyenv]: https://github.com/yyuu/pyenv
[pyenv-virtualenv]: https://github.com/yyuu/pyenv-virtualenv

### How to run the tests/linters

1. Make sure you already installed [pytest][pytest] and [flake8][flake8]. Both are listed in `requirements.txt` so if you followed the instructions to setup your machine above then they should already be installed.

1. Put `.env` file under your `tests` directory.

1. You can run the tests and linters with `python manage.py test` and `python manage.py lint` respectively. If you remember that `manage.py` is actually executable, you may run it with `./manage.py COMMAND`.

1. To run both linters and tests in one command, you can use `python manage.py check`. This is useful to check your code before making a pull request.

1. For more info on what you can do with `manage.py`, run `python manage.py --help`.

[pytest]: http://pytest.org/latest/
[flake8]: https://pypi.python.org/pypi/flake8
