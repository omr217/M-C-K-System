import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


class SystemVisualization:

    def __init__(self, positions=None, velocities=None, sampling_frequency=0):

        self.positions = positions if positions is not None else []
        self.velocities = velocities if velocities is not None else []
        self.sampling_frequency = sampling_frequency
        self.time = []  # Will store time points if needed

    def visualize_results(self, euler_type='Runge-Kutta'):

        if not self.time:
            print("No time data to visualize.")
            return

        fig, ax = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
        fig.suptitle(f'{euler_type} Simulation Results')

        ax[0].plot(self.time, self.positions, label='Displacement', color='blue')
        ax[0].set_ylabel('Displacement')
        ax[0].legend()
        ax[0].grid(True)

        ax[1].plot(self.time, self.velocities, label='Velocity', color='red')
        ax[1].set_xlabel('Time (s)')
        ax[1].set_ylabel('Velocity')
        ax[1].legend()
        ax[1].grid(True)

        plt.tight_layout()
        plt.show()


class SystemWriter(SystemVisualization):

    def __init__(self, positions=None, velocities=None, sampling_frequency=0):

        super().__init__(positions, velocities, sampling_frequency)

        # Default system parameters
        self.mass = 10.0
        self.damping_coefficient = 1.0
        self.spring_constant = 5.0
        self.force = 1.0
        self.total_time = 10.0

    def store_parameters(
            self,
            mass=1.0,
            damping_coefficient=1.0,
            spring_constant=1.0,
            force=1.0,
            sampling_frequency=100,
            total_time=10.0
    ):

        self.mass = mass
        self.damping_coefficient = damping_coefficient
        self.spring_constant = spring_constant
        self.force = force
        self.sampling_frequency = sampling_frequency
        self.total_time = total_time

    def write_to_excel(self, filename="simulation_data.xlsx"):

        if not self.time or not self.positions or not self.velocities:
            print("No simulation data to write to Excel.")
            return

        df = pd.DataFrame({
            'time': self.time,
            'position': self.positions,
            'velocity': self.velocities
        })
        df.to_excel(filename, index=False)
        print(f"Simulation data written to Excel: {filename}")

    def write_parameters_to_excel(self, filename="simulation_data.xlsx"):

        param_dict = {
            'mass': [self.mass],
            'damping_coefficient': [self.damping_coefficient],
            'spring_constant': [self.spring_constant],
            'force': [self.force],
            'sampling_frequency': [self.sampling_frequency],
            'total_time': [self.total_time]
        }
        param_df = pd.DataFrame(param_dict)

        with pd.ExcelWriter(filename, mode='a', if_sheet_exists='replace') as writer:
            param_df.to_excel(writer, sheet_name='Parameters', index=False)
        print(f"System parameters written to Excel (sheet: Parameters): {filename}")

    def write_results_to_excel(self, filename="simulation_data.xlsx"):

        if not self.time or not self.positions or not self.velocities:
            print("No simulation results to write to Excel.")
            return

        df = pd.DataFrame({
            'time': self.time,
            'position': self.positions,
            'velocity': self.velocities
        })
        with pd.ExcelWriter(filename, mode='a', if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name='Results', index=False)
        print(f"Simulation results written to Excel (sheet: Results): {filename}")

    def read_excel_file(self, filename="simulation_data.xlsx"):

        try:
            df = pd.read_excel(filename)
            self.time = df['time'].tolist()
            self.positions = df['position'].tolist()
            self.velocities = df['velocity'].tolist()
            print(f"Simulation data read from Excel: {filename}")
        except Exception as e:
            print(f"Error reading Excel file: {e}")

    def write_to_text(self, filename="simulation_data.txt"):

        if not self.time or not self.positions or not self.velocities:
            print("No simulation data to write to text.")
            return

        df = pd.DataFrame({
            'time': self.time,
            'position': self.positions,
            'velocity': self.velocities
        })
        df.to_csv(filename, index=False, sep=' ')
        print(f"Simulation data written to text file: {filename}")

    def write_to_dat(self, filename="simulation_data.dat"):

        if not self.time or not self.positions or not self.velocities:
            print("No simulation data to write to dat.")
            return

        df = pd.DataFrame({
            'time': self.time,
            'position': self.positions,
            'velocity': self.velocities
        })
        df.to_csv(filename, index=False, sep=' ')
        print(f"Simulation data written to dat file: {filename}")

    def read_text_file(self, filename="simulation_data.txt"):

        try:
            df = pd.read_csv(filename, delim_whitespace=True)
            self.time = df['time'].tolist()
            self.positions = df['position'].tolist()
            self.velocities = df['velocity'].tolist()
            print(f"Simulation data read from text file: {filename}")
        except Exception as e:
            print(f"Error reading text file: {e}")

    def read_dat_file(self, filename="simulation_data.dat"):

        try:
            df = pd.read_csv(filename, delim_whitespace=True)
            self.time = df['time'].tolist()
            self.positions = df['position'].tolist()
            self.velocities = df['velocity'].tolist()
            print(f"Simulation data read from dat file: {filename}")
        except Exception as e:
            print(f"Error reading dat file: {e}")

    def write_to_database(self, database_url="sqlite:///simulation_data.db"):

        engine = create_engine(database_url)

        # Write parameters
        param_dict = {
            'mass': [self.mass],
            'damping_coefficient': [self.damping_coefficient],
            'spring_constant': [self.spring_constant],
            'force': [self.force],
            'sampling_frequency': [self.sampling_frequency],
            'total_time': [self.total_time]
        }
        param_df = pd.DataFrame(param_dict)
        param_df.to_sql('Parameters', con=engine, if_exists='replace', index=False)

        # Write results
        if self.time and self.positions and self.velocities:
            results_df = pd.DataFrame({
                'time': self.time,
                'position': self.positions,
                'velocity': self.velocities
            })
            results_df.to_sql('Results', con=engine, if_exists='replace', index=False)
        print(f"Simulation data written to database: {database_url}")

    def read_from_database(self, database_url="sqlite:///simulation_data.db"):

        try:
            engine = create_engine(database_url)
            # Read parameters
            param_df = pd.read_sql_table('Parameters', con=engine)
            if not param_df.empty:
                self.mass = param_df['mass'].iloc[0]
                self.damping_coefficient = param_df['damping_coefficient'].iloc[0]
                self.spring_constant = param_df['spring_constant'].iloc[0]
                self.force = param_df['force'].iloc[0]
                self.sampling_frequency = param_df['sampling_frequency'].iloc[0]
                self.total_time = param_df['total_time'].iloc[0]

            # Read results
            results_df = pd.read_sql_table('Results', con=engine)
            if not results_df.empty:
                self.time = results_df['time'].tolist()
                self.positions = results_df['position'].tolist()
                self.velocities = results_df['velocity'].tolist()

            print(f"Simulation data read from database: {database_url}")
        except Exception as e:
            print(f"Error reading from database: {e}")


class SystemSolver(SystemWriter):

    def __init__(
            self,
            mass=1.0,
            damping_coefficient=1.0,
            spring_constant=1.0,
            force=1.0,
            sampling_frequency=100,
            total_time=10.0
    ):

        super().__init__(positions=[], velocities=[], sampling_frequency=sampling_frequency)
        self.store_parameters(
            mass=mass,
            damping_coefficient=damping_coefficient,
            spring_constant=spring_constant,
            force=force,
            sampling_frequency=sampling_frequency,
            total_time=total_time
        )
        self.time = []

    def solve_system_runge_kutta(self):

        # Time step
        dt = self.total_time / self.sampling_frequency

        # Initial conditions (x=0, x'=0)
        y1 = 0.0  # displacement
        y2 = 0.0  # velocity

        def f1(t, y1, y2):
            return y2

        def f2(t, y1, y2):
            return (self.force - self.damping_coefficient * y2 - self.spring_constant * y1) / self.mass

        t = 0.0
        self.time.append(t)
        self.positions.append(y1)
        self.velocities.append(y2)

        for _ in range(self.sampling_frequency):
            # 4th order Runge-Kutta steps
            k1_1 = f1(t, y1, y2)
            k1_2 = f2(t, y1, y2)

            k2_1 = f1(t + dt/2, y1 + dt*k1_1/2, y2 + dt*k1_2/2)
            k2_2 = f2(t + dt/2, y1 + dt*k1_1/2, y2 + dt*k1_2/2)

            k3_1 = f1(t + dt/2, y1 + dt*k2_1/2, y2 + dt*k2_2/2)
            k3_2 = f2(t + dt/2, y1 + dt*k2_1/2, y2 + dt*k2_2/2)

            k4_1 = f1(t + dt, y1 + dt*k3_1, y2 + dt*k3_2)
            k4_2 = f2(t + dt, y1 + dt*k3_1, y2 + dt*k3_2)

            dy1 = (k1_1 + 2*k2_1 + 2*k3_1 + k4_1) / 6.0
            dy2 = (k1_2 + 2*k2_2 + 2*k3_2 + k4_2) / 6.0

            y1 = y1 + dy1 * dt
            y2 = y2 + dy2 * dt

            t += dt
            self.time.append(t)
            self.positions.append(y1)
            self.velocities.append(y2)


if __name__ == "__main__":
    # Create solver instance
    solver = SystemSolver(
        mass=1.0,
        damping_coefficient=0.2,
        spring_constant=2.0,
        force=1.0,
        sampling_frequency=100,
        total_time=10.0
    )

    # Solve the system using Runge-Kutta
    solver.solve_system_runge_kutta()
    print("Solving completed.")

    # Visualize
    solver.visualize_results()

    # Write to Excel
    solver.write_to_excel("simulation_data_runge_kutta.xlsx")
    solver.write_parameters_to_excel("simulation_data_runge_kutta.xlsx")
    solver.write_results_to_excel("simulation_data_runge_kutta.xlsx")

    # Write to Text and Dat
    solver.write_to_text("simulation_data_runge_kutta.txt")
    solver.write_to_dat("simulation_data_runge_kutta.dat")

    # Write to Database
    solver.write_to_database("sqlite:///simulation_data_runge_kutta.db")

    # Demonstrate reading back from Excel
    solver.read_excel_file("simulation_data_runge_kutta.xlsx")

    # Demonstrate reading back from Text
    solver.read_text_file("simulation_data_runge_kutta.txt")

    # Demonstrate reading back from Database
    solver.read_from_database("sqlite:///simulation_data_runge_kutta.db")
    print("Reading completed.")
