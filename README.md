<h1 align="center">🗂️ Automatic File Sorter</h1>

<p align="center">
  <b>A simple yet powerful Python script to automatically organize your files by extension.</b><br>
  This program scans a selected directory, identifies file types by their extensions, 
  creates folders if they don't exist, and moves each file into its corresponding folder.
</p>

<h2>⚙️ How It Works</h2>
<p>
  Simply provide the <b>path</b> to the folder you want to organize — the script does the rest for you!  
  It will analyze all files inside that directory, detect their extensions (e.g. <code>.jpg</code>, <code>.pdf</code>, <code>.mp3</code>), 
  automatically create folders for each file type if they don’t exist, and move every file into its respective folder.
</p>

<h2>📋 Features</h2>
<ul>
  <li>Automatic folder creation based on file extension</li>
  <li>Moves files to their respective folders</li>
  <li>Prevents overwriting existing files</li>
  <li>Lightweight and easy to customize</li>
</ul>

<h2>🚀 How to Use</h2>
<ol>
  <li>Clone this repository or download the <code>.py</code> file.</li>
  <li>Run the script and enter the path of the folder you want to organize when prompted.</li>
  <li>The files will be sorted automatically into folders by type.</li>
  <li>Example command:
    <pre><code>Automatic_File_Sorter.py</code></pre>
  </li>
</ol>

<h2>💡 Example</h2>
<p>
  Before running the script:
</p>
<pre>
Downloads/
├── photo1.jpg
├── song.mp3
├── document.pdf
</pre>

<p>
  After running:
</p>
<pre>
Downloads/
├── Images/
│   └── photo1.jpg
├── Audio/
│   └── song.mp3
├── Documents/
│   └── document.pdf
</pre>

<h2>🧠 Notes</h2>
<p>
  You can easily extend the script by adding more file type categories or customizing destination paths.
</p>

<h2>📄 License</h2>
<p>
  This project is released under the MIT License. Feel free to modify and share.
</p>

