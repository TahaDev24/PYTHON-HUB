# PYTHON HUB Web Interface

This directory contains the first responsive web interface foundation.

## Run locally

~~~bash
python -m http.server 5173 --directory apps/web
~~~

## Current behavior

- Responsive dark-first dashboard layout.
- English and Persian interface toggle.
- Right-to-left layout direction for Persian.
- Search across the ecosystem category directory.
- Local favorites stored in browser local storage.
- Mobile navigation drawer.
- Keyboard shortcut Ctrl/Command + K to focus search.

## Current limitations

This is a static interface foundation. It is not yet connected to the Python API, has no authentication, and does not execute or install tools. Favorites are stored only in the current browser.

## Frontend conventions

- Keep user-facing strings in the locale dictionaries.
- Use CSS logical properties for bidirectional layouts.
- Preserve keyboard access and visible focus states.
- Respect the reduced-motion preference.
- Do not represent planned integrations as working tools.
