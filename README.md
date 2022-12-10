<h1>remote_debug</h1>
<h2>Automating ADB Remote Debugging Over WiFi for Android</h2>
<h3>Description</h3>
<p>This project provides a Python program for automating the process of remote debugging an Android device over WiFi using the Android Debug Bridge (ADB). The program uses the <code>argparse</code> module to parse command line arguments and the <code>scanner</code> module from the <code>services</code> folder to scan the network for devices. It then connects to the target device using the IP address and enables remote debugging using ADB. The program also includes a simple graphical user interface (GUI) using the <code>tkinter</code> module.</p>
<h3>Usage</h3>
<ol>
  <li>Clone the repository:
  <pre><code>git clone https://github.com/adinortey360/remote_debug.git</code></pre></li>
  <li>Install the required modules:
  <pre><code>pip install -r requirements.txt</code></pre></li>
  <li>Run the program and specify the IP address of the target Android device:
  <pre><code>python main.py -t &lt;target_ip&gt;</code></pre></li>
</ol>
<h3>Contributing</h3>
<p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p>
<h3>License</h3>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
