import abc
from abc import ABC, abstractmethod

# Product: SoftwareProject (The object being built)
class SoftwareProject:
    """Represents the final software project product."""
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.steps = []
        print(f"- Initiating Project: {self.project_name} -")

    def add_step(self, part: str):
        """Adds a construction step to the project."""
        self.steps.append(part)

    def display(self):
        """Prints the completed construction process and links to the traits."""
        print("\n- Project Construction Complete -")
        print(f"Project Name: {self.project_name}")
        print("Completed Steps (Detail-Oriented Sequence):")
        for i, step in enumerate(self.steps, 1):
            print(f"  {i}. {step}")
        print("\n- Developer Traits Reflected in Design -")
        print(
            "1. Attention to Detail:** The Director enforced a strict, methodical build sequence.\n"
            "2. Continuous Learning:** The Abstract Builder allows for new build methodologies to be quickly adopted.\n"
            "3. Collaboration:** Each step is a well-defined phase, promoting clear communication and handoffs."
        )


# Abstract Builder: AbstractProjectBuilder (The Interface)
class AbstractProjectBuilder(ABC):
    """Abstract interface defining the steps required to build a software project."""

    # Abstract methods must be overridden by any concrete builder.
    @abstractmethod
    def build_requirements(self):
        pass

    @abstractmethod
    def build_design(self):
        pass

    @abstractmethod
    def build_implementation(self):
        pass

    @abstractmethod
    def build_testing(self):
        pass

    @abstractmethod
    def get_result(self) -> SoftwareProject:
        pass


# Concrete Builder: DetailOrientedBuilder (The Worker)
class DetailOrientedBuilder(AbstractProjectBuilder):
    """A concrete builder focusing on meticulous, high-quality development steps."""
    def __init__(self, name: str):
        # Composition: The builder creates and holds the product instance
        self.project = SoftwareProject(name)

    def build_requirements(self):
        self.project.add_step("Requirements: Conducted in-depth analysis and drafted comprehensive documentation (Trait: Attention to Detail).")

    def build_design(self):
        self.project.add_step("Design: Created detailed UML diagrams and established a robust architectural foundation (Trait: Collaboration).")

    def build_implementation(self):
        self.project.add_step("Implementation: Wrote clean, well-commented code, adhering strictly to style guides.")

    def build_testing(self):
        self.project.add_step("Testing: Executed full suite of Unit, Integration, and Regression tests.")

    def get_result(self) -> SoftwareProject:
        """Returns the fully constructed project."""
        # Implements the + get_result : SoftwareProject method.
        return self.project


# Director: ProjectDirector (The Enforcer)
class ProjectDirector:
    """The Director enforces the correct, methodical sequence of the build process."""

    def construct(self, builder: AbstractProjectBuilder):
        """
        Enforces the standard, detail-oriented construction sequence.
        (Requirements -> Design -> Implementation -> Testing)
        """
        # Implements the + construct(builder : AbstractProjectBuilder) method.
        # Enforces the "Attention to Detail" trait.
        builder.build_requirements()
        builder.build_design()
        builder.build_implementation()
        builder.build_testing()


# Client Code (Main Application Logic)
if __name__ == "__main__":
    # Instance the Concrete Builder (the worker)
    # The Client knows the specific builder needed.
    builder = DetailOrientedBuilder("Fantasy Football Automatic Manager")

    # Instance the Director (the process enforcer)
    director = ProjectDirector()

    # The Client tells the Director to use the Builder to construct the project.
    # The Director only interacts with the Abstract Builder interface (Dependency).
    director.construct(builder)

    # The Client retrieves the final Product from the Builder
    final_project = builder.get_result()

    # Display the final result
    final_project.display()