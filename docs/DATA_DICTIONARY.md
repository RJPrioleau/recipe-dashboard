# Data Dictionary

## Purpose

This document defines the core product information used by Recipe Dashboard.

The definitions describe product concepts rather than database tables, framework models, or implementation details.

---

## Core Relationships

- One household manages many meals, recipes, suggestions, cooking sessions, and cooking-history entries.
- One recipe collection contains many recipes, and each recipe belongs to exactly one primary collection.
- One recipe has one required default variant and may have additional variants.
- One recipe variant has one or more revisions.
- One recipe revision contains ingredients and cooking steps.
- One meal contains multiple meal components.
- Each meal component references one recipe and the variant normally used in that meal.
- One ingredient review evaluates the selected variants and scales for one saved or custom meal and produces one shopping list.
- One cooking session prepares one saved or custom meal and tracks step completions.
- Completing one cooking session creates one cooking-history entry.
- One meal suggestion references one complete existing meal and may receive one suggestion response.

These relationships describe the product domain. They do not prescribe database tables or Python classes.

---

## Household

The household represents the people whose meals, cooking history, ratings, and preferences are managed by Recipe Dashboard.

The first usable version supports one household through one operator. Separate household-member accounts and individual preference profiles are not required.

The household default serving quantity is six adult plates unless a recipe specifies otherwise.

---

## Recipe

A recipe is a reusable set of ingredients and preparation instructions for one prepared item.

Examples include an entrée, side dish, sauce, condiment, drink, dessert, bread, or seasoning blend.

A recipe is a building block used to assemble meals. A recipe is not itself a meal.

A recipe includes at least:

- A name
- One primary recipe collection
- Ingredients
- Preparation instructions
- Serving quantity
- Preparation time or effort
- Household preference information
- One required default variant
- Current revision information for each variant

A recipe may originate from:

- The operator’s personal collection
- An external recipe source

Questions still requiring product decisions:

- Whether external recipes are copied into the personal collection or referenced from their original source
- Whether photographs are included
- Exact archive and deletion behavior

---

## Meal

A meal is a planned dining experience composed of multiple recipes.

A meal includes at least:

- One entrée
- One additional recipe

Additional recipes may include:

- Side dishes
- Sauces or condiments
- Drinks
- Breads
- Desserts

The meal is the primary object used for:

- Dashboard suggestions
- Cooking history
- Meal planning
- Household recommendations

Recipes remain reusable building blocks.

Meals combine recipes into something the household actually cooks.

A meal references its recipes rather than copying their ingredients and instructions.

A meal may include:

- A name
- Description
- Meal components
- Default serving quantity
- Image
- Tags
- Notes
- Estimated preparation effort
- Estimated total time
- Favorite status
- Active or archived status

Questions still requiring product decisions:

- Which meal details are required beyond its name and included recipes

---

## Meal Component

A meal component connects one recipe variant to a meal.

A meal component identifies:

- The recipe included in the meal
- The normally selected recipe variant
- The recipe's role in that meal
- Display order
- Optional serving adjustment
- Optional meal-specific note

The recipe and variant remain reusable outside the meal.

A saved meal may use a different variant or scale for one cooking session without immediately changing the saved meal.

---

## Custom Meal

A custom meal is assembled by the operator for a specific cooking occasion instead of being selected from an existing saved meal.

A custom meal may be used once or saved as a reusable meal after cooking and review.

Custom meals are never saved automatically. The operator must explicitly approve saving one.

---

## Personal Recipe

A personal recipe is a recipe controlled and maintained by the operator.

The operator can:

- Add it
- View it
- Edit it
- View its prior revisions

Improving or correcting a personal recipe variant creates a new revision rather than permanently replacing its earlier content.

Creating an intentionally different style or use creates a variant rather than a revision.

---

## External Recipe

An external recipe is discovered through a source outside Recipe Dashboard.

An external recipe should include enough information to:

- Identify the recipe
- Display it in recipe discovery
- Open or access the complete recipe
- Distinguish it from a personal recipe

The external recipe provider and access method have not been selected.

Questions still requiring product decisions:

- Whether an external recipe can be included in a meal without first being saved
- Whether edits create a personal copy
- Whether external recipes remain available if the outside source removes them
- How an external or imported source becomes a complete meal and its component recipes

---

## Recipe Variant

A recipe variant is an intentionally different style or use of a recipe.

A variant does not replace another variant. Each variant remains valid for a different cooking situation or desired result.

Examples include:

- Weeknight garlic mashed potatoes
- Holiday garlic mashed potatoes
- Wing ranch
- Salad ranch

A variant may differ in:

- Ingredients
- Preparation instructions
- Equipment
- Preparation time or effort
- Intended use

Every recipe has one required default variant. Additional variants are optional and may be added as the operator discovers different cooking experiences.

Questions still requiring product decisions:

- Whether the default variant's label is always visible
- Whether a new variant begins as a copy of an existing variant or as a blank recipe

---

## Recipe Revision

A recipe revision is a preserved snapshot of a specific recipe variant at a point in time.

A revision improves or corrects an existing variant without creating a different cooking experience. Meaningful saved changes create a revision; minor display corrections may not require one.

A recipe revision includes at least:

- The variant's content at that time
- The date the revision was created
- Its relationship to the recipe and variant
- Its order within the variant's revision history

Prior revisions remain viewable after edits.

A revision improves an existing recipe variant. A variant creates a deliberately different experience.

Questions still requiring product decisions:

- Whether the operator can restore an older revision
- Whether a revision note is required or optional
- Whether revisions can be compared

---

## Ingredient

An ingredient is an item used to prepare a recipe.

An ingredient includes at least:

- Ingredient name
- Quantity
- Unit of measurement
- Preparation note when needed

Examples of preparation notes include:

- Diced
- Divided
- Room temperature
- Minced
- Optional

Ingredient pantry quantities and expiration information are not required in the first usable version.

---

## Cooking Step

A cooking step is one actionable instruction within a recipe variant.

A cooking step includes at least:

- Its sequence position
- The instruction text

A cooking step may also include:

- Section
- Estimated duration
- Optional note
- Related equipment
- Optional warning

Steps are displayed in a suggested order but may be completed in any order during a cooking session.

Questions still requiring product decisions:

- Whether instructions may be grouped into stages
- Whether linked recipes such as sauces can appear as instruction components

---

## Serving Quantity

Serving quantity represents how much food a recipe is intended to produce.

For Recipe Dashboard:

- One serving represents one adult plate.
- The household default is six servings unless the recipe specifies otherwise.

The default six-serving model supports:

- Two dinner servings on the first day
- One lunch serving on the second day
- Two dinner servings on the second day
- One lunch serving on the third day

Questions still requiring product decisions:

- Whether every recipe must use the adult-plate definition
- Whether drinks, sauces, spices, and dressings need different serving units

---

## Scale Request

A scale request describes how the operator wants to change one recipe's yield for a cooking session.

The operator may request:

- A percentage of the original recipe
- A target number of servings
- A common batch size such as half or double

Scaling applies to an individual recipe, not automatically to every recipe in a meal.

---

## Scaled Recipe

A scaled recipe is a temporary cooking view generated from one recipe revision and a scale request.

The same scale factor is applied consistently to all proportional ingredients so the recipe remains balanced. The scaled view does not overwrite the saved recipe or create a revision.

---

## Measurement Normalization

Measurement normalization converts calculated ingredient quantities into practical standard kitchen measurements after the scale factor has been applied.

For example, the application should prefer a usable combination of cups, tablespoons, and teaspoons over an impractical fraction such as `1/64 cup`.

Normalization should preserve the recipe's proportions as closely as practical. Exact rounding tolerances and unit-conversion rules remain open product decisions.

---

## Ingredient Scaling Rule

An ingredient scaling rule describes how one ingredient behaves when its recipe is scaled.

Possible behaviors include:

- Proportional
- Whole-unit
- To taste
- As needed
- Non-scalable

Proportional is the normal default. Exact handling for eggs, package sizes, frying oil, garnishes, salt, and strong seasonings remains an open product decision.

---

## Recipe Collection

A recipe collection organizes recipes by the role they play in a meal, not by cuisine or occasion.

Discussed collections include:

- Entrées
- Side dishes
- Sauces and condiments
- Drinks
- Desserts
- Breads
- Seasonings and spice blends

Every recipe belongs to exactly one primary recipe collection. Tags provide secondary organization, and a meal component may assign a context-specific role without changing the recipe's primary collection.

Questions still requiring product decisions:

- Which collections are approved for the first usable version
- Whether collections are fixed or operator-created

---

## Preparation Effort

Preparation effort helps the operator filter recipes based on how demanding they are to make.

It represents more than elapsed time. It may account for:

- Active preparation
- Number of cooking stages
- Cleanup
- Specialized equipment
- Attention required during cooking

The exact format has not been approved.

Possible future formats include:

- Low, medium, or high effort
- A numerical effort score
- Separate active-time and total-time values

---

## Household Preference

A household preference records whether a meal, recipe, ingredient, flavor, or other food characteristic is liked or disliked by the household.

The first usable version uses household preferences when filtering recipes.

Questions still requiring product decisions:

- Whether preferences are stored for the household as a whole or separately for household members
- Whether preferences apply to complete meals, recipes, ingredients, or some combination
- Whether preferences use like, neutral, and dislike
- Whether a dislike should completely exclude a recipe or only warn the operator

Independent household-member accounts are not required.

---

## Meal Rating

A meal rating records the operator’s assessment of a cooked meal.

Ratings may support:

- Meal filtering
- Cooking history
- Meal suggestions
- The explanation for why a meal was suggested

Questions still requiring product decisions:

- Rating scale
- Whether ratings are required
- Whether each cooking event can have its own rating
- Whether the meal also has an overall calculated rating

The first usable version rates meals only. Rating individual recipes or variants is a possible later capability.

---

## Ingredient Review

Ingredient review is the process of checking what is needed before cooking a selected meal.

The application combines ingredient requirements from every selected and scaled recipe variant in the meal. The operator marks each ingredient as:

- Already available
- Still needed

Automatic pantry inventory is not required in the first usable version.

Compatible duplicate ingredients are combined into one total while preserving a breakdown by recipe. Meaningfully different forms remain separate.

Required seasonings always appear during ingredient review, even when their exact remaining household quantity is not tracked.

---

## Shopping List

A shopping list contains the ingredients still needed after ingredient review.

A shopping-list entry may include:

- Ingredient
- Combined required quantity when compatible
- Unit
- Breakdown by recipe
- Checked or purchased status

The first usable version exports the list without requiring grocery-store or Apple Notes integration. Exact export formats remain an open product decision.

---

## Cooking Session

A cooking session represents the active process of preparing one selected saved or custom meal.

A cooking session may track:

- The meal being prepared
- The recipes, variants, revisions, and scale requests actually used
- Start and completion time
- Completed cooking steps
- Current progress
- Cooking notes
- Serving quantity

The operator may scroll freely, open any included recipe, complete steps in any order, return to earlier sections, and move between recipes.

The application may focus the next incomplete step but never requires every step to be checked before the session can be completed.

---

## Step Completion

Step completion records whether one cooking step was completed during a particular cooking session.

It tracks session progress without modifying the saved recipe or revision.

The first usable version supports incomplete and completed states. A cooking session may be completed while steps remain unchecked.

---

## Cooking History Entry

A cooking history entry is the permanent record created when the operator explicitly completes a cooking session.

Opening or viewing a meal or recipe does not create a cooking history entry.

Each entry includes at least:

- The meal that was cooked
- The date it was cooked
- The recipes, variants, revisions, and scales actually used

Potential additional information includes:

- Rating
- Notes
- Serving quantity
- Whether the household would cook it again

Cooking history supports:

- Displaying the last cooked meal
- Displaying the last time a suggested meal was cooked
- Filtering based on prior cooking history
- Generating future meal suggestions

---

## Last Cooked Meal

The last cooked meal is the most recent meal recorded in cooking history.

The dashboard displays:

- The meal
- The date it was cooked

This information comes from an explicit cooking history entry.

---

## Meal Suggestion

A meal suggestion is a meal presented by the application as a possible next dining experience.

The suggestion assists the operator but does not make the cooking decision.

A meal suggestion includes at least:

- The suggested meal
- The last date it was cooked, when applicable
- A brief explanation of why it was suggested

The first usable version suggests complete saved or imported meals. It does not invent new combinations of recipes.

Questions still requiring product decisions:

- How a single suggestion is selected
- Whether the operator can request another suggestion
- Whether dismissed suggestions are remembered
- What happens when no cooking history exists

---

## Suggestion Response

A suggestion response records what the operator did with a meal suggestion.

Possible responses include:

- Accepted
- Skipped
- Viewed
- Replaced with another suggestion

Skipping a suggestion means it was not selected for that occasion. It does not mean the household dislikes the meal.

---

## Suggestion Explanation

A suggestion explanation describes the information that caused a meal to be suggested.

Possible explanation factors include:

- The meal has not been cooked recently
- The household previously rated it highly
- It differs from recently cooked meals
- Its preparation effort fits the operator’s current preference
- It matches household likes
- It avoids known dislikes

Pantry availability and food-waste factors are later-phase capabilities and are not required in the first usable version.

---

## Mark as Cooked

Mark as Cooked is the explicit operator action that completes a cooking session and records the meal in cooking history.

Viewing a meal or one of its recipes does not imply that the meal was cooked.

The action should allow the operator to confirm at least:

- The meal
- The cooking date

Questions still requiring product decisions:

- Whether the date defaults to today
- Whether the operator can enter past meals
- Whether rating and notes are collected immediately
- Whether accidental entries can be corrected or removed

---

## Recipe Source

Recipe source identifies where a recipe came from.

Examples include:

- Personal
- External provider
- Imported document
- Adapted from another recipe

The first usable version requires distinction between personal and external recipes.

---

## Imported Recipe Source

An imported recipe source is a PDF, Word document, or other source document used to create a structured recipe draft.

The import process attempts to extract:

- Recipe name
- Yield
- Ingredients
- Preparation instructions
- Notes
- Equipment
- Preparation and cooking times
- Source information

The operator reviews and corrects the extracted information before approving the recipe as ready to cook. Perfect automatic extraction is not required.

The original source document remains attached or referenced so the operator can compare it with the structured recipe.

---

## Recipe Status

Recipe status describes where a recipe is in the creation and review workflow.

Discussed statuses include:

- Imported
- Needs review
- Ready to cook
- Archived

An imported recipe is not assumed to be accurate until the operator reviews and approves it.

---

## Tag

A tag provides flexible secondary organization without changing a recipe's primary collection.

Tags may describe:

- Protein or entrée type
- Cuisine
- Cooking method
- Effort
- Occasion
- Flavor
- Equipment
- Dietary style

Exact initial tags and whether tags are fixed or operator-created remain open product decisions.

---

## Equipment

Equipment represents a cooking tool used by a recipe variant.

Examples include a Dutch oven, Blackstone, air fryer, crockpot, pressure cooker, blender, or dehydrator.

Equipment may support recipe filtering and later meal suggestions. Equipment-aware suggestions are not required in the first usable version.

---

## Archived Recipe

An archived recipe is unavailable during normal recipe discovery but remains preserved.

Archiving behavior has not yet been approved.

Meals and recipe variants may also need archival behavior. Archived items referenced by cooking history must remain identifiable so earlier records remain meaningful.

---

## Deleted Recipe

A deleted recipe is removed from normal application use.

Deletion behavior has not yet been approved.

Important unresolved questions include:

- Whether deletion is permanent
- Whether recipes referenced by a meal's cooking history can be deleted
- Whether prior revisions remain available
- Whether archived recipes should be used instead of deletion
