class AIStudyAssistant:
    """Basic rule-based AI Study Assistant Agent."""

    def __init__(self):
        self.name = "AI Study Assistant"
        self.running = True

    def welcome(self):
        print("*** AI STUDY ASSISTANT AGENT ***\n")
        print("Available actions:")
        print("• Explain a topic")
        print("• Generate quiz questions")
        print("• Summarize a topic")
        print("• Create a study plan")
        print("• Give study tips")
        print("• Ask for help")
        print("• Exit the agent")

    def process_request(self, user_input):
        request = user_input.lower().strip()
        clean_request = request.replace("!", "").replace(".", "")

        if clean_request in ["exit", "quit", "bye"]:
            self.running = False
            return "Thank you for using AI Study Assistant!"

        if clean_request in ["hi", "hii", "hello", "hey", "good morning",
                             "good afternoon", "good evening"]:
            return self.greeting()

        if "thank" in clean_request or clean_request == "thanks":
            return "You're welcome! Happy studying! 😊"

        if clean_request in ["help", "help me", "what can you do"]:
            return self.help_response()

        if "explain" in request:
            return self.explain_topic(user_input)

        if "quiz" in request or "question" in request:
            return self.generate_quiz(user_input)

        if "summary" in request or "summarize" in request:
            return self.summarize_topic(user_input)

        if "study plan" in request or "schedule" in request:
            return self.study_plan(user_input)

        if "tip" in request or "tips" in request:
            return self.study_tips()

        return self.general_response()

    def get_topic(self, text):
        phrases = [
            "explain", "summarize", "summary of",
            "create a summary of", "make a summary of",
            "quiz about", "quiz on", "quiz questions about",
            "quiz questions on", "generate quiz questions about",
            "generate a quiz about", "generate a quiz on",
            "create a study plan for", "study plan for",
            "plan my study for", "schedule for"
        ]

        topic = text.strip()

        for phrase in phrases:
            if topic.lower().startswith(phrase):
                topic = topic[len(phrase):].strip()
                break

        return topic if topic else "the requested topic"

    def greeting(self):
        return (
            "\n👋 Hello! I am your AI Study Assistant.\n\n"
            "How can I help you with your studies today?"
        )

    def help_response(self):
        return (
            "\n🆘 Help\n\n"
            "You can ask me to:\n"
            "• Explain a topic\n"
            "• Generate quiz questions\n"
            "• Summarize a topic\n"
            "• Create a study plan\n"
            "• Give study tips\n"
            "• Say hello or ask for help"
        )

    def explain_topic(self, user_input):
        topic = self.get_topic(user_input)
        return (
            f"\n📚 Explanation: {topic}\n\n"
            f"{topic.capitalize()} is an important concept that can be "
            "understood through its principles, features, applications, "
            "and practical examples."
        )

    def generate_quiz(self, user_input):
        topic = self.get_topic(user_input)
        return (
            f"\n❓ Quiz Questions: {topic}\n\n"
            "1. What is the main purpose of this topic?\n"
            "2. What are its important features?\n"
            "3. Give one practical example.\n"
            "4. What are its advantages?\n"
            "5. What are its limitations?"
        )

    def summarize_topic(self, user_input):
        topic = self.get_topic(user_input)
        return (
            f"\n📝 Summary: {topic}\n\n"
            f"{topic.capitalize()} can be understood through its "
            "definition, key concepts, features, applications, "
            "advantages, limitations, and examples."
        )

    def study_plan(self, user_input):
        topic = self.get_topic(user_input)
        return (
            f"\n📅 Study Plan: {topic}\n\n"
            "Day 1: Learn the basic concepts.\n"
            "Day 2: Study important definitions and features.\n"
            "Day 3: Practice examples and questions.\n"
            "Day 4: Revise difficult concepts.\n"
            "Day 5: Review the topic and take a self-test."
        )

    def study_tips(self):
        return (
            "\n💡 Study Tips\n\n"
            "1. Set clear study goals.\n"
            "2. Make short and useful notes.\n"
            "3. Practice questions regularly.\n"
            "4. Take short breaks while studying.\n"
            "5. Revise important topics frequently."
        )

    def general_response(self):
        return (
            "\n💬 I could not understand that request.\n\n"
            "Try asking:\n"
            "• Explain machine learning\n"
            "• Generate quiz questions about Python\n"
            "• Summarize DBMS\n"
            "• Create a study plan for OS\n"
            "• Give me study tips\n"
            "• Help"
        )

    def run(self):
        self.welcome()

        while self.running:
            user_input = input("\nEnter your study request: ")

            if not user_input.strip():
                print("\n⚠️ Please enter a request.")
                continue

            response = self.process_request(user_input)
            print("\nAgent Response:")
            print(response)


def main():
    agent = AIStudyAssistant()
    agent.run()


if __name__ == "__main__":
    main()
