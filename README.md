
# Django Tutorial Extended

The official Django tutorial, extended for PyCharm demo uses.

## Installation

- Clone this repo, open in PyCharm Professional, which should:
   - Make a virtual environment
   - Prompt to install dependencies from `requirements.txt`
   - Configure the settings that recognize this as a Django project
   - Make a Django run configuration
- `npm install` to get JS dependencies.
- Open PyCharm's `manage.py` console via `Tools | Run manage..py task`
- `makemigrations` and press enter
- `migrate` and press enter
- `createsuperuser` (and answer the questions)
- For preloading questions into DB, make sure to run `python manage.py load_questions`
- Run the created run config (probably named `django_tutorial`)
- Visit `http://127.0.0.1:8000/admin/` and add a question
- Visit `http://127.0.0.1:8000/polls/`

Other steps:

- `Mark as Templates Folder` for `polls/templates`
- `Settings | Languages & Frameworks | JavaScript | Prettier` and set it up to run on save/reformat
- Ensure Django support and pytest are configured in settings
- In the main template, find the `<script>` for Tailwind, Alt-Enter on the URL, and "Download" as a library
- Add the SQLite instance in the database tool

For the extended demo:

- Have the `BlackConnect` plugin installed
  - Have `blackd` installed somewhere, e.g. via pipx or add to the venv
  - But NOT set up to run on Reformat/Save
- Install `.env` and `requirements` plugins

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

- Shift-Shift `tem/bas` to open `templates/base.html`
- Run the `Django Server` run configuration
- Click on link in the run window
- Navigate to `View Polls`
  - Delete the `img` with `PyCharm.svg`
  - Reload browser
  - Cmd-Alt-O IndV to `polls/views.py` number of returned questions
    by changing `[0:10]` to `[0:1]`
  - See that Django restarts the process
- Use `Run manage.py` tool window to `makemigrations`
  - Cmd-Shift-A mana to bring up manage.py tool
  - Type in `makemigrations`
- Run server under the debugger, not a big speed hit
  - Stop the running server
  - Restart it with the debugger
  - Set breakpoints in:
    - `polls.views.IndexView.get_queryset`
    - Also in `polls.templates/polls/index.html`
      - Inside `{% for question in latest_question_list %}`
  - Reload the page at `/polls/`
  - Show stepping through Python and Django
  - Clear the breakpoints and resume

### IDE Features for Django

- Autocomplete
  - `Shift-Shift INS` to navigate to `INSTALLED_APPS` in `mysite/settings.py`
  - Autocomplete any package names in strings
  - Make a typo, show the warning
  - Open `Shift-Shift pol/ind` to open `polls/index.html`
  - Autocomplete `latest_question_list` on line 9
- Navigate
  - Same spot in `polls/index.html`, navigate to `latest_question_list`
  - Same for `INSTALLED_APPS`
  - In `polls/index.html` navigate back and forth, view/template, via icons
- Autoimport
  - `Cmd-Alt-O urlpa` to open `polls/urlpatterns.py`
  - Change `views.ResultsView.as_view()` to `ReVi` and `Cmd-Space-Space` to autocomplete
  - Show that it generated the import
- Refactor
  - `Shift-Shift IndV` to navigate to `polls.views.IndexView`
  - Refactor Rename `index.html` to `djindex.html`
  - Point out the filename has changed
  - Undo

### Template Support

- `Shift-Shift pol/ind` to open `polls/index.html`
- On Line 12, insert new line and recreate the `<img src` with Emmet
  - `img tab` to start the `<img>` LiveTemplate
  - template for `{% s` to start the `static` Django tag
  - Autocomplete the part of the `polls/images/jb_beam.png` path
  - Make a typo to show squiggly
  - Fix typo
  - Cursor in the `jb_beam.png` segment
  - Cmd-B to navigate to the PNG

### Test-First

- `Cmd-Shift-A Spl Ri` to split right
- On left: `Cmd-Alt-O IndV` to navigate to IndexView
- On right: `Cmd-Alt-O t_p` to navigate to `tests/test_base_functions.test_polls_index`
- Click the gutter icon to run just that test
- On left: put a breakpoint in `IndexView.get_queryset`
- In test, click gutter icon and run in debug mode

### Git Pull Request Integration

TODO We need to file a PR.

### Fullstack: HTTP Files against Django Rest Framework

- Make sure Django Server is running *in debug mode*
- Open `run-apis.http`
- Run the first URL
- Put a breakpoint in `IndexView.get_queryset` on the `return`
- Click that URL again
- Continue, clear breakpoint

### Fullstack: Tailwind

- `base.html` and `<script src="https://cdn.tailwindcss.com">`
- We downloaded the "library" with Alt-Enter
- Go to `<div class="navbar` and autocomplete `navbar`
- Then, navigate to `navbar` to see definition

### Fullstack: React frontend

- In `package.json`, run the `dev` script
- Click the URL
- See the React app
- Navigate to Symbol `App`
- Remove the import of `Index`
- Autocomplete the usage and show the import, then navigate to it

### Fullstack: Prettier and eslint

- Mention `package.json` and npm integration
  - You get a popup with link for installing
  - Autocomplete in package.json
- In preferences, show Prettier integration
- Make sure prettier on save and reformat are checked
- In `Index.jsx` mess up spacing, indentation
- Reformat Code
- Show preferences for eslint

### Fullstack: React testing

- In `Index.jsx` put a breakpoint on `{question.question_text}`
- Split Right
- Shift-Shift `Index.tes` to navigate to the test file
- Use gutter icon to run test under the debugger

### Fullstack: Database tool

- Open the database tool
- Double-click on the `polls_question` table

## Extended Demo

This goes before the full-stack part and covers material from [Adam's "Boost Your Django DX" book](https://adamchainz.gumroad.com/l/byddx).

### Inline documentation

- In `IndexView.get_queryset` mouse over:
  - `import` for Python code
  - `filter` for Django code
- Mouseover an `h1` to show MDN-integrated docs

### Virtual environments (covered)

### Package management

- Open `requirements.txt`
- Add another package
- Mention the community plugin
- Show it in action

### ipython

- Cmd-Shift-A Py Con
- Opens Python Console, with Django imports, using ipython
- Note the different repl
- `print(2+2)` with syntax highlighting, autocomplete

### EditorConfig

- Make sure `BlackConnect` is off!
- Open `.editorconfig`
- Change `4` to `14`
- Open `conftest.py`
- Reformat Code
- Change `14` back to `4`
- Reformat Code

### Black

- Enable BlackConnect

### pre-commit

- Note the `.pre-commit-config.yaml`
- Commit window, gear icon at bottom, show the checkbox for git hooks

### Testing (covered)

This will be used in the sponsor talk at PyCon US 2023.
It emphasizes points made in Adam Johnson's Django DX book.
