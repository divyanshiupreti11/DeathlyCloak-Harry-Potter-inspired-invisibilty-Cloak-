🧙‍♂️ Deathly Cloak (OpenCV + Python)
This project creates a Harry Potter-style invisibility cloak using OpenCV and Python.
It works by detecting a red cloak in front of the webcam and replacing it with a pre-captured background, making the person appear invisible.
🚀 How It Works

Capture the background image (without you in the frame).

Detect the red color cloak in the live video using HSV color space.

Replace the red cloak area with the saved background.

Display the final output → you look invisible 🎥✨
📂 Project Structure
📁 Invisibility-Cloak
│-- background.py   # Captures and saves background as image.jpg
│-- test.py         # Runs the invisibility cloak effect
│-- image.jpg       # Saved background (auto-generated)
│-- README.md       # Project documentation

⚙️ Requirements

Python 3.x

OpenCV

NumPy

🏆 Credits

Built with ❤️ using OpenCV & NumPy.

Inspired by the Harry Potter invisibility cloak 🪄
