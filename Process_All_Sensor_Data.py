import os
import pandas as pd
import matplotlib.pyplot as plt

# Configuration
# Number of rows to skip in each sensor data file
# Rows to skip in the "Sensor Data" is because it counts the first step
# While the main_file has no data of first step but only cyclic
# If you are facing trouble in the processing, ask me on WhatsApp: +923440907874

rows_to_skip = 12
main_file = "GlobalResponse_FDCurve.xlsx"
sensor_data_folder = "Sensor Data"
plot_output_folder = "All Sensor Plots"
excel_output_folder = "Processed Excel Sheets"

# Create output folders if they don't exist
os.makedirs(plot_output_folder, exist_ok=True)
os.makedirs(excel_output_folder, exist_ok=True)

# Read the main Excel file and extract the second column for y-axis (Force in kN)
main_df = pd.read_excel(main_file, usecols=[1])  # Second column (index 1)
y_force_kn = main_df.iloc[:, 0]  # Extract the column as a Series

# Loop through all Excel files in the "Sensor Data" folder
for filename in os.listdir(sensor_data_folder):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(sensor_data_folder, filename)

        # Read the first column for x-axis (Displacement), skipping the defined number of rows
        sensor_df = pd.read_excel(file_path, usecols=[1], skiprows=rows_to_skip)
        x_displacement = sensor_df.iloc[:, 0]  # Extract the column as a Series

        # Ensure both x and y have the same length
        min_length = min(len(x_displacement), len(y_force_kn))
        x_displacement = x_displacement.iloc[:min_length]  # Trim x to match y
        y_force_trimmed = y_force_kn.iloc[:min_length]  # Trim y to match x

        # Save processed data to a new Excel file
        processed_data = pd.DataFrame({"Displacement": x_displacement, "Force (kN)": y_force_trimmed})
        excel_save_path = os.path.join(excel_output_folder, f"{filename}")
        processed_data.to_excel(excel_save_path, index=False)

        # Plot Displacement vs. Force (Line Plot without Markers)
        plt.figure(figsize=(8, 5))
        plt.plot(x_displacement, y_force_trimmed, linestyle='-', label="Force vs Displacement", color='b')
        plt.xlabel("Displacement")
        plt.ylabel("Force (kN)")
        plt.title(filename)  # Title is the sensor file name
        plt.legend()
        plt.grid(True)

        # Save plot
        plot_save_path = os.path.join(plot_output_folder, f"{filename}.png")
        plt.savefig(plot_save_path, dpi=300)
        plt.close()

print(f"All plots have been saved in the '{plot_output_folder}' folder.")
print(f"All processed Excel sheets have been saved in the '{excel_output_folder}' folder.")
