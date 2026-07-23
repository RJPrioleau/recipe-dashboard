Recipe Dashboard helps a household decide what to cook next by combining recipes, preferences, pantry awareness, and cooking history into a single decision-support application.

## Status

Product discovery is complete, and Recipe Dashboard is preparing to enter implementation. The approved initial direction is Python, Django, SQLite, Django templates, HTML, CSS, and limited JavaScript. Detailed architecture, dependency versions, project structure, and deployment remain open.

## First Usable Version

The first usable version helps one operator decide what their household should cook next through a dashboard that suggests complete saved or imported meals and explains each suggestion.

The first usable workflow includes:

- Creating or importing recipes
- Organizing recipes into meals
- Scaling individual recipes
- Reviewing combined ingredients
- Exporting missing ingredients as a shopping list
- Moving freely through recipes and cooking steps
- Explicitly completing a cooking session
- Recording cooking history and optional meal ratings

Recipes are reusable building blocks, and meals are assembled from multiple recipes. The first version does not invent new recipe combinations, track pantry inventory automatically, or require artificial intelligence.

## Documentation

- [Product definition](docs/PRODUCT.md)
- [Plain-English data dictionary](docs/DATA_DICTIONARY.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)
- [Collaboration workflow](docs/COLLABORATION.md)

## Development

The run command and verification command are not established yet. Read `AGENTS.md` and the repository documentation before making implementation or architectural decisions.
