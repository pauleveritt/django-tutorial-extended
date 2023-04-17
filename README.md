
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
- (Optional) Install the BlackConnect plugin and set it up to run on reformat/save
- Add the SQLite instance in the database tool

For the extended demo:

- Have the `BlackConnect` plugin installed
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

#### Auto-completion from CDN

If you’re using Bootstrap/Tailwind/DaisyUI or another CSS library linked 
from a CDN, you can get completion for the class names 
from that library – no need to add its sources to the project.

Reference: [https://www.jetbrains.com/webstorm/guide/tips/library-completion/](https://www.jetbrains.com/webstorm/guide/tips/library-completion/)

### Running Django Server

- Starts in reload mode (not a big deal)
  - Change a template, reload browser
  - Make a change to `polls/views.py` number of returned questions
  - See that Django restarts the process
- Use `Run manage.py` tool window to `makemigrations`
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
  - Navigate to `INSTALLED_APPS` in `mysite/settings.py`
  - Autocomplete any package names in strings
  - Open `polls/results.html` and autocomplete `.question_text`
- Navigate
  - Same spot in `polls/results.html`, navigate to `question_text`
  - Same for `INSTALLED_APPS`
  - In `polls/index.html` navigate back and forth, view/template, via icon
- Autoimport
  - `polls/urls.py` and auto-import a `view.`
- Refactor
  - Navigate to `IndexView`
  - Refactor Rename `index.html` to `djindex.html`
  - Point out the filename has changed
  - Undo

### Template Support

- In `polls/index.html`
- Recreate the `<img src` with Emmet, then template for `static`
- Autocomplete the path
- Show yellow squiggly on typo
- Navigate to the PNG

### Test-First

- `polls/tests.py`
- In debug mode

### Git Pull Request Integration

### Fullstack: HTTP Files against Django Rest Framework

- Make sure Django Server is running *in debug mode*
- Open `run-apis.http`
- Run the first URL
- Put a breakpoint in `IndexView.get_queryset` on the `return`
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

### EditorConfig

- Make sure `BlackConnect` is off!
- Open `.editorconfig`
- Change `4` to `14`
- Open `conftest.py`
- Reformat Code
- Change `14` back to `4`
- Reformat Code

### pre-commit

### Black

### .env

### Testing (covered)

This will be used in the sponsor talk at PyCon US 2023.
It emphasizes points made in Adam Johnson's Django DX book.

