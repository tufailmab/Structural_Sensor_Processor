</head>
<body>
  <h1>Structural Sensor Processor</h1>

  <p>
    This Python-based project automates the processing and visualization of structural sensor data. It reads force values from a master file and displacement values from multiple sensor Excel files, trims them to the same length, saves the merged data, and generates corresponding plots for analysis. Both the main force-displacement curve and the sensor displacement histories were extracted from the FEA model, with the latter organized in a separate folder for processing. This code was developed as part of a PhD research project focused on bridge pier analysis at a university in Pakistan (name withheld for confidentiality).
  </p>

  <h2>Features</h2>
  <ul>
    <li><strong>Automated Processing:</strong> Reads and aligns force and displacement data from Excel files.</li>
    <li><strong>Batch Handling:</strong> Supports processing multiple sensor files at once.</li>
    <li><strong>Excel Output:</strong> Saves processed data in a new Excel file per sensor.</li>
    <li><strong>Plot Generation:</strong> Creates clean, high-resolution Force vs. Displacement plots.</li>
    <li><strong>Organized Outputs:</strong> Stores plots and Excel files in dedicated folders.</li>
  </ul>

  <h2>Usage Instructions</h2>
  <ol>
    <li>Place your main file (<code>GlobalResponse_FDCurve.xlsx</code>) in the root directory.</li>
    <li>Create a folder named <code>Sensor Data</code> and place all sensor Excel files inside it.</li>
    <li>Run the script using:
      <pre><code>python Process_All_Sensor_Data.py</code></pre>
    </li>
    <li>Processed Excel files will appear in <code>Processed Excel Sheets</code>.</li>
    <li>Plots will be saved in <code>All Sensor Plots</code> as PNG images.</li>
  </ol>

  <h2>Requirements</h2>
  <p>The following Python libraries are required:</p>
  <ul>
    <li>pandas</li>
    <li>matplotlib</li>
    <li>os (built-in)</li>
  </ul>
  <p>Install dependencies using:</p>
  <pre><code>pip install pandas matplotlib</code></pre>

  <h2>License</h2>
  <p>This project is licensed under the <strong>MIT License</strong>.</p>
  <p>You are free to use, modify, and distribute this software under the terms of the MIT License. Please give appropriate credit if used in published work.</p>

  <h2>Developer Information</h2>
  <ul>
    <li><strong>Developer:</strong> Engr. Tufail Mabood</li>
    <li><strong>Contact:</strong> <a href="https://wa.me/+923440907874">WhatsApp</a></li>
    <li><strong>Note:</strong> This is an open-source project. Contributions and improvements are welcome.</li>
  </ul>
</body>
</html>
