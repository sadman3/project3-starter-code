import os
import PIL
import google.generativeai as genai

# do not reveal your api key when submitting the assignment
GOOGLE_API_KEY="YOUR_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)


def list_genai_models():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)


def read_file_as_string(filename):
  with open(filename, "r") as f:
    content = f.read()
  return content


def detect_object(model, filepath):
    img = PIL.Image.open(filepath)
    prompt = "list objects in the image in this way: 1. ing 2. ing 3. ing etc"
    response = model.generate_content([prompt, img])
    print(response.text)

if __name__ == "__main__":
   list_genai_models()
#    model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
#    filepath = "pic1.png"
#    detect_object(model, filepath)
# #   prompt = read_file_as_string("prompt.txt")
# #   response = model.generate_content(prompt)
# #   print(response.text)