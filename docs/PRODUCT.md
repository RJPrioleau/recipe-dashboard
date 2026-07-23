# Product Definition

## Core Product Principle

Recipe Dashboard manages meals, not just recipes.

Recipes are reusable building blocks that each represent one prepared item.

Meals combine multiple recipes into a complete dining experience.

The dashboard, cooking history, meal suggestions, and future planning features operate primarily on meals.

## Product Philosophy

Recipe Dashboard is a decision-support application.

It recommends and organizes information, but the operator always decides what to cook.

Recommendations should assist decision-making rather than replace it.

Recipe Dashboard organizes cooking the way people naturally think about meals—not the way recipes are traditionally stored.

Recipe Dashboard is an assistant, not an autopilot.

The application helps the operator decide what to cook, organize recipes into meals, prepare ingredients, and track cooking progress.

At every stage, the cook remains in control.

The application never forces a cooking order, locks navigation, or assumes there is only one correct way to prepare a meal. The operator can move between recipes and cooking steps at any time.

The application provides organization, memory, and guidance while respecting the cook's experience and preferences.

## Purpose

Recipe Dashboard is a personal recipe discovery and pantry intelligence application that helps users find meals they will enjoy, reduce food waste, manage evolving recipes, and make better cooking decisions.

## Intended User

Recipe Dashboard has one operator and is used for the benefit of that operator's household.

Multi-user accounts and independent household-member access are not approved requirements.

## Primary Interface

The application's primary interface is a dashboard that helps the operator decide what to cook next. The dashboard presents recent cooking history, a suggested next meal, and the reasoning behind that suggestion.

## Home Dashboard

The application's primary interface is a dashboard intended to help the operator quickly decide what to cook next.

The dashboard displays:

- The most recently cooked meal.
- The date the meal was cooked.
- A suggested next meal.
- The last date the suggested meal was cooked.
- A brief explanation of why the meal was suggested.

## Cooking History

Opening or viewing a meal or recipe does not count as cooking it.

The operator explicitly records that a meal was cooked through an action such as `Mark as Cooked`.

Each cooking-history entry records at least:

- The meal that was cooked.
- The date it was cooked.

The information used to generate and explain meal suggestions will be defined during later product and technical planning.

## First Usable Outcome

The first usable version provides one complete workflow:

1. Open the dashboard and receive an explainable suggestion for a complete saved or imported meal.
2. Accept the suggestion, request another eligible suggestion, browse saved meals, or assemble a custom meal.
3. Review the recipes and variants included in the selected meal.
4. Scale individual recipes when needed without changing the saved recipes.
5. Review combined ingredients and mark which ones are already available.
6. Export the missing ingredients as a shopping list.
7. Start a cooking session and move freely among the included recipes and cooking steps.
8. Explicitly complete the cooking session, record the meal in cooking history, and optionally rate it.
9. Decide whether a custom or modified meal should be saved for future use.

The first usable version also allows the operator to browse and filter recipes, open complete recipe details, create recipes manually, and import recipes from PDF or Word documents through a review-and-correct workflow.

The application suggests complete meals that already exist as approved meal combinations. It does not invent new combinations of recipes in the first usable version.

## Approved Meal Behavior

- Meals are assembled from multiple reusable recipes.
- Each meal contains one entrée and at least one additional recipe.
- A saved meal may be modified for one cooking session without immediately changing the saved meal.
- The completed cooking record reflects the recipes and variants actually cooked.
- After cooking and review, the operator may approve saving a custom or modified combination as a reusable meal or updating an existing meal.
- Custom meals are never saved automatically.

## Approved Recipe Organization

- Every recipe belongs to exactly one primary recipe collection.
- Secondary organization uses tags rather than additional primary collections.
- Every recipe has one required default variant.
- Additional variants are optional.
- Meaningful improvements to a variant create revisions, while intentionally different preparations create variants.
- Prior revisions remain viewable.

## Approved Recipe Scaling

Scaling operates on individual recipes rather than automatically scaling an entire meal.

The operator may select a percentage or target yield. The same scale factor is applied consistently to all scalable ingredients in that recipe so its proportions remain balanced.

Calculated quantities are converted into practical standard kitchen measurements after scaling. Scaling creates a temporary cooking view and does not overwrite the saved recipe.

Some ingredients require special scaling behavior, including whole-unit ingredients, ingredients used to taste or as needed, and non-scalable ingredients. The exact normalization and exception rules remain open product decisions.

## Approved Ingredient Review and Shopping Behavior

- Ingredient review combines the requirements from every selected recipe variant in the meal.
- The operator manually marks ingredients as already available or still needed; automatic pantry inventory is not required.
- Compatible duplicate ingredients are combined into one shopping total while preserving a breakdown showing which recipe uses each amount.
- Meaningfully different forms of an ingredient remain separate.
- Required seasonings always appear in ingredient review and shopping lists.

## Approved Cooking Session Behavior

- A cooking session represents the active preparation of one selected meal.
- Cooking steps are displayed in a suggested order, but the operator may move freely among recipes and steps.
- Completing every checkbox is not required.
- The operator may complete a cooking session while steps remain unchecked.
- Cooking history is created only when the operator explicitly completes the session.

## Approved Recipe Import Behavior

The first usable version supports manual recipe creation and import from PDF and Word documents.

An imported document is a source used to create a draft structured recipe. The operator reviews and corrects extracted names, yields, ingredients, instructions, notes, equipment, times, and source information before approving the recipe as ready to cook.

Perfect automatic extraction is not required. The original document remains attached or referenced for comparison.

## Approved Recipe Sources

The first usable version includes:

- A personal recipe collection
- External recipe sources

The external source and its access method have not been selected.

## Personal Recipe Capabilities

The first usable version allows the operator to:

- Add a personal recipe
- View a personal recipe
- Edit a personal recipe
- Create optional variants
- Access prior revisions after a recipe variant is meaningfully edited

Archiving and deletion behavior have not been approved.

## Approved Discovery Filters

The first usable version supports filtering based on:

- Household likes and dislikes
- Previous ratings or cooking history
- Preparation time or effort

The way this information is captured and stored remains undecided.

## Approved Later Phases

### Pantry Tracking

Add basic pantry tracking after the first usable recipe-discovery version.

### Food-Waste Guidance

After basic pantry tracking, help the operator identify ingredients that should be used soon.

## Not Required in the First Usable Version

- Multiple user accounts
- Independent household-member access
- Automatic recipe ranking
- Pantry tracking
- Food-waste guidance
- Artificial intelligence
- Automatically generated recipe combinations
- Coordinated cooking timelines
- Forced sequential cooking steps
- Automatic timers
- Grocery-store integration
- Apple Notes integration
- Nutrition tracking
- Ingredient cost analysis
- Meal calendars
- Automatic ingredient substitutions
- Dietary-restriction or allergy filters
- Cuisine filters
- Meal-context filters

Items in this section are not automatically approved for later development.

## Open Product Decisions

- Detailed user-interface and interaction design
- External recipe source
- External recipe access method
- Recipe archiving behavior
- Recipe deletion behavior
- Meal rating scale and whether recipe-level ratings belong in a later version
- Exact suggestion-selection and cold-start behavior
- Recipe scaling normalization and exception rules
- Exact imported-document extraction and review behavior
- How an external or imported source becomes a complete suggestible meal and its component recipes
- Shopping-list export formats

## Open Technical Decisions

- Application architecture
- Detailed data model
- Exact dependency versions
- Project and application structure
- Document-extraction libraries
- Recipe-scaling implementation
- Deployment approach
- Run command
- Verification command

Technical decisions require explicit approval after the repository documentation has been reviewed.

## Approved Initial Technical Direction

- Language: Python
- Web framework: Django
- Initial database: SQLite
- Frontend: Django templates, HTML, CSS, and limited JavaScript
- Primary development environment: PyCharm
- Version control: Git and GitHub

SQLite is the initial local database. Moving to PostgreSQL may be considered later if deployment, concurrency, or multiple-user requirements justify it.

## Parking Lot

Items added here are ideas only. They are not approved requirements or roadmap commitments.

- Walmart integration
- ingredient cost tracking
- equipment awareness
- shopping optimization
- ingredient substitutions
- expiration awareness
- repeat cooldowns
- leftovers
- guided cooking mode
- coordinated meal timelines
- generated meal combinations
