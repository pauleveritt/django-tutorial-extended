
# Django Tutorial Extended

The official Django tutorial, extended for PyCharm demo uses.

## Installation

1. Clone this repo, open in PyCharm Professional, which should:
   - Make a virtual environment
   - Prompt to install dependencies from `requirements.txt`
   - Configure the settings that recognize this as a Django project
   - Make a Django run configuration
2. `npm install` to get JS dependencies.
3. Open PyCharm's `manage.py` console via `Tools | Run manage..py task`
4. `makemigrations` and press enter
5. `migrate` and press enter
6. `createsuperuser` (and answer the questions)
7. Run the created run config (probably named `django_tutorial`)
8. Visit `http://127.0.0.1:8000/admin/` and add a question
9. Visit `http://127.0.0.1:8000/polls/`

Other steps:

- `Mark as Templates Folder` for `polls/templates`
- `Settings | Languages & Frameworks | JavaScript | Prettier` and set it up to run on save/reformat
- Ensure Django support and pytest are configured in settings
- 

## Main Demo

We're going to talk about the "I" in "IDE".

### Project Setup

- PyCharm eliminates some cumbersome setup steps
- Show that you could use PyCharm's bundled `Django` template in `New Project`
  - Makes and sets a virtual env
  - Installs Django into it
  - Makes a sample Django project
  - Creates run config
  - Configures Django support
- Or, clone https://github.com/pauleveritt/django-tutorial-extended from VCS

### Running Django Server

- Starts in reload mode (not a big deal)
  - Change a template, reload browser
  - Make a change to `polls/views.py` number of returned questions
  - See that Django restarts the process
- Use `Run manage.py` tool window to `makemigrations`
  - Nice to have that open all the time
- Run server under the debugger
  - Always run it under the debugger, not a huge speed hit
  - Set breakpoints in: 
    - `polls.views.IndexView.get_queryset`
    - Also in `polls.templates/polls/index.html`
      - Inside `{% for question in latest_question_list %}`
  - Issue a request to `/polls/`
  - Show stepping through Python and Django
  - Clear the breakpoints and resume

### IDE Features for Django

- Autocomplete
- Navigate
- Refactor

### Template Support

### Test-First

- `polls/tests.py`
- In debug mode

### Git Pull Request Integration

### Fullstack: HTTP Files against Django Rest Framework

### Fullstack: Tailwind

### Fullstack: React frontend

### Fullstack: Prettier and eslint

### Fullstack: React testing

### Fullstack: Database tool


## Extended Demo

This goes before the full-stack part and covers material from [Adam's "Boost Your Django DX" book](https://adamchainz.gumroad.com/l/byddx).

### Inline documentation

### Virtual environments (covered)

### Package management

### ipython

### EditorConfig

### pre-commit

### Black

### .env

### Testing (covered)

This will be used in the sponsor talk at PyCon US 2023.
It emphasizes points made in Adam Johnson's Django DX book.

