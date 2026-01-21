# password-generator
Features
Guaranteed Complexity: Every password includes at least one lowercase letter, one uppercase letter, and one number.

Randomized Structure: Uses random.shuffle to ensure required characters don't always appear in the same position.

Input Validation: Handles basic errors to ensure the user provides numeric inputs for quantity and length.

Flexible Length: Automatically adjusts the minimum length to 3 to satisfy character requirements.

🛠️ How It Works
Requirement Seeding: The script picks one character from abc..., ABC..., and 123... immediately.

Filling: It fills the remaining slots (based on your chosen length) with a mix of alphanumeric characters.

Shuffling: It scrambles the list to prevent predictable patterns.
