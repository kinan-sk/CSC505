class Khader:
    def __init__(self, project_name="Untitled Project"):
        self.project_name = project_name
        self.communication_data = {}
        self.planning_data = {}
        self.iterations = []
        self.final_deployment_date = None

    def run_project_simulation(self):
        print("-" * 50)
        print(f"** {self.project_name.upper()}: KHADER MODEL **")
        print("-" * 50)

        self._get_linear_phase_data()
        num_iterations = self._get_num_iterations()
        
        for i in range(1, num_iterations + 1):
            self._get_iteration_data(i)

        self.final_deployment_date = input("\n[FINAL DEPLOYMENT] Enter the final deployment date (MM-DD-YYYY): ")
        self.generate_report()

    def _get_linear_phase_data(self):
        print("\n--- PHASE 1: COMMUNICATION (Define Scope) ---")
        self.communication_data['Goal'] = input("Project Goal/High-Level Requirement: ")
        self.communication_data['Stakeholders'] = input("Key Stakeholders Identified (names/roles): ")
        
        print("\n--- PHASE 2: PLANNING (Initial Architecture & Risk) ---")
        self.planning_data['Architecture'] = input("Planned Technical Architecture (Python, Java, etc.): ")
        self.planning_data['KeyRisks'] = input("Identified Key Risks: ")
        self.planning_data['InitialEstimate'] = input("Initial Overall Time Estimate (in weeks): ")

    def _get_num_iterations(self):
        while True:
            try:
                num = int(input("\n[ITERATIVE LOOP] Enter the total number of sprints/iterations planned: "))
                if num > 0:
                    return num
                else:
                    print("Please enter a number greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def _get_iteration_data(self, iteration_num):
        iteration_data = {
            'Sprint': iteration_num,
            'Features': '', 'DesignTime': '', 'ConstructionTime': '', 
            'TestCoverage': '', 'Feedback': ''
        }
        
        print(f"\n--- SPRINT {iteration_num}: ITERATIVE CYCLE ---")
        
        iteration_data['Features'] = input(f"[MODELING] Features planned for Sprint {iteration_num}: ")
        iteration_data['DesignTime'] = input(f"[MODELING] Design time spent (in weeks): ")
        
        iteration_data['ConstructionTime'] = input(f"[CONSTRUCTION] Coding/Model Training time spent (in weeks): ")
        
        iteration_data['TestCoverage'] = input(f"[DEPLOYMENT] Test/UAT coverage score (in %): ")
        iteration_data['Feedback'] = input(f"[DEPLOYMENT] Key Stakeholder Feedback/Adjustments identified: ")
        
        self.iterations.append(iteration_data)

    def generate_report(self):
        print("\n" + "=" * 70)
        print(f"KHADER MODEL PROJECT REPORT: {self.project_name.upper()}")
        print("=" * 70)

        print("\n--- I. LINEAR FOUNDATION (COMMUNICATION & PLANNING) ---")
        print(f"  Overall Project Goal: {self.communication_data.get('Goal', 'N/A')}")
        print(f"  Key Stakeholders: {self.communication_data.get('Stakeholders', 'N/A')}")
        print(f"  Initial Estimate: {self.planning_data.get('InitialEstimate', 'N/A')}")
        print(f"  Architecture: {self.planning_data.get('Architecture', 'N/A')}")
        print(f"  Identified Risks: {self.planning_data.get('KeyRisks', 'N/A')}")

        print("\n--- II. ITERATIVE DEVELOPMENT CYCLES ---")
        if self.iterations:
            for data in self.iterations:
                print(f"\n  > SPRINT {data['Sprint']}:")
                print(f"    - Features Developed: {data['Features']}")
                print(f"    - Modeling Time: {data['DesignTime']}")
                print(f"    - Construction Time: {data['ConstructionTime']}")
                print(f"    - Test Coverage: {data['TestCoverage']}")
                print(f"    - **Feedback for Next Sprint:** {data['Feedback']}")
        else:
            print("  No iterations were executed.")

        print("\n--- III. FINAL ROLLOUT ---")
        print(f"  Final Deployment Date: {self.final_deployment_date}")
        print("=" * 70 + "\n")


if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    khader_project = Khader(project_name=project_name)
    khader_project.run_project_simulation()
