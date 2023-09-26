import openai
import time

# Set your OpenAI API key here
api_key = "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"

def chat_with_gpt3(prompt, max_retries=3, retry_delay=5):
    for _ in range(max_retries):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=150,
                api_key=api_key,
            )
            return response.choices[0].text.strip()
        except openai.error.RateLimitError as e:
            print(f"Rate limit exceeded. Retrying in {retry_delay} seconds.")
            time.sleep(retry_delay)
        except Exception as e:
            return str(e)

def read_input_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except Exception as e:
        return str(e)

def main(input_data):
    print("Welcome to the GPT-3 Chatbot!")

    while True:
        try:
            Data = input_data  # Use the provided input_data

            # Rest of your code remains the same
            FileHistory = open("Brain\\HistoryChat.txt", "r")
            DataHistory = FileHistory.read()
            FileHistory.close()

            if str(Data) == str(DataHistory):
                time.sleep(0.5)
                pass
            else:
                Result = chat_with_gpt3(Data)  # Call chat_with_gpt3 function
                print(Result)

                FileHistory = open("Brain\\HistoryChat.txt", "w")
                FileHistory.write(Data)
                FileHistory.close()

        except Exception as e:
            print(e)

if __name__ == "__main__":
    user_input = read_input_from_file("Body\\SpeechRecognition.txt")
    main(user_input)  # Call the main function with user_input
