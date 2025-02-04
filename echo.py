#echo.py


def echo(text: str, repetitions: int = 3) -> str:
  """Imitate a real world echo"""
  if len(text) >= repetitions:
    for i in range(repetitions):
      i = -1*(i-repetitions)
      echo = ""
      for j in range(i):
        echo = echo + text[len(text) - i + j]
      print(echo)
  return "."


if __name__ == "__main__":
  text = input ("Yell something at a mountain: ")
  print(echo(text))
