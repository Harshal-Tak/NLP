import speech_recognition as sr
import pyttsx3

# predefined questions and answers
qa_pairs = {
    "What does NLP stand for?": "Natural Language Processing",
    "Which library in Python is commonly used for NLP tasks?": "NLTK",
    "What is the process of breaking text into individual words called?": "Tokenization",
    "What is the process of reducing words to their base or root form called?": "Stemming",
    "What does TF-IDF stand for?":"Term Frequency Inverse Document Frequency"
}

# points system
total_questions = len(qa_pairs)
points_per_question = 1
total_points = total_questions * points_per_question

# Initialize Text-to-Speech engine
engine = pyttsx3.init()


# function to speak out the question
def speak_question(question):
    engine.say(question)
    engine.runAndWait()


# function to recognize speech from the microphone
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        answer = recognizer.recognize_google(audio).lower()
        print("You said:", answer)
        return answer
    except Exception as e:
        print("Sorry, I couldn't understand what you said.")
        return ""


def quiz():
    score = 0
    for question in qa_pairs.keys():
        speak_question(question)
        user_answer = listen()
        correct_answer = qa_pairs[question].lower()
        if user_answer == correct_answer:
            score += points_per_question
            print("Correct!")
            pyttsx3.speak("Correct!")
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")
            pyttsx3.speak(f"Sorry, the correct answer is {correct_answer}.")

    print(f"Your total score is: {score} out of {total_points}")


if __name__ == "__main__":
    quiz()
