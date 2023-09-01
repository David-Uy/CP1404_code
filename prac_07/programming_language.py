class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic=False):
        """
        Construct a ProgrammingLanguage from the given values.

        :param name: The name of the programming language.
        :param typing: The typing system of the language (e.g., 'Dynamic' or 'Static').
        :param reflection: True if the language supports reflection, False otherwise.
        :param year: The year when the language first appeared.
        :param pointer_arithmetic: True if the language supports pointer arithmetic, False otherwise.
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}, Pointer Arithmetic={self.pointer_arithmetic}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a user-friendly string representation of a ProgrammingLanguage."""
        pointer_info = "Supports Pointer Arithmetic" if self.pointer_arithmetic else "Does not support Pointer Arithmetic"
        return f"Name: {self.name}\nTyping: {self.typing}\nReflection: {self.reflection}\nYear: {self.year}\n{pointer_info}"

def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, True)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    run_tests()
