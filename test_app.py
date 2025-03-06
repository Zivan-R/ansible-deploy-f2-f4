def test_output():
   result = subprocess.run(["python3", "app.py"], capture_output=True, text=True)
   assert "Hello world" in result.stdout
